pipeline {
    agent any
    triggers {
        pollSCM('H/30 * * * *')
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }
    environment {
        registry = "toby4all/tobby_pipeline"  // The name of your user and repository (which can be created manually)
        DOCKERHUB_CREDENTIALS = credentials('dockerhub') // The credentials used for your repo
        IMAGE_VERSION = "${BUILD_NUMBER}"  // Use the build number as the image version
    }
    stages {
        stage('Checkout') {
            steps {
                git([url: 'https://github.com/toby4all/My_third_project.git', branch: 'master'])
            }
        }
        stage('Build') {
            steps {
                bat "docker build -t ${registry}:${IMAGE_VERSION} ."
            }
        }
        stage('Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerhubPassword', usernameVariable: 'dockerhubUser')]) {
                    bat "docker login -u ${env.dockerhubUser} -p ${env.dockerhubPassword}"
                }
            }
        }
        stage('Push') {
            steps {
                bat "docker push ${registry}:${IMAGE_VERSION}"
            }
        }
        stage('Set image version') {
            steps {
                bat "echo IMAGE_TAG=${IMAGE_VERSION} > .env"
            }
        }
        stage('Run docker compose') {
            steps {
                bat 'docker compose up -d'
            }
        }
        stage('Test docker compose') {
            steps {
                bat 'python docker_backend_testing.py'
            }
        }
        stage('Deploy helm chart') {
            steps {
                bat "helm upgrade --install my-release. --set image.tag=${registry}:${IMAGE_VERSION}"
            }
        }
    }
    post {
        always {
            bat "docker compose down"
            bat "rmi ${registry}:${IMAGE_VERSION}"
            bat "helm delete my-release"
        }
    }
}

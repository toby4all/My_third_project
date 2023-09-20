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
    DOCKERHUB_CREDENTIALS = credentials('dockerhub') // The credentials used to your repo
    }
    stages {
        stage('Checkout') {
            steps {
               git([url: 'https://github.com/toby4all/My_third_project.git', branch: 'master'])
            }
        }
        stage('Build') {
            steps {
                bat 'docker build -t toby4all/tobby_pipeline:${BUILD_NUMBER} .'
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
                bat 'docker push toby4all/tobby_pipeline:${BUILD_NUMBER}'
            }
        }
        stage('Set image version') {
            steps {
                bat "echo IMAGE_TAG=${BUILD_NUMBER} > .env"
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
    }
     post {
        always {
            bat "docker compose down"
            bat "rmi ${registry}:${BUILD_NUMBER}"
        }
    }
}
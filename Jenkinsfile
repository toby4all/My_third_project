pipeline {
    agent any
    triggers {
        pollSCM('H/30 * * * *')
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }
    environment {
        registry = "toby4all/tobby_pipeline"
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        IMAGE_VERSION = "${BUILD_NUMBER}"
        IMAGE_TAG = "${BUILD_NUMBER}"
        PYTHON_PATH = "C:\\Users\\Toby\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
        HELM_CHART_PATH = "./TobbyOnK8S"
    }
    stages {
        stage('Checkout') {
            steps {
                git([url: 'https://github.com/toby4all/My_third_project.git', branch: 'master'])
            }
        }
        stage('Build') {
            steps {
                script {
                    def buildCommand = "docker build -t ${registry}:${IMAGE_VERSION} ."
                    bat(buildCommand)
                }
            }
        }
        stage('Login to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerhubPassword', usernameVariable: 'dockerhubUser')]) {
                        def loginCommand = "docker login -u ${env.dockerhubUser} -p ${env.dockerhubPassword}"
                        bat(loginCommand)
                    }
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    def pushCommand = "docker push ${registry}:${IMAGE_VERSION}"
                    bat(pushCommand)
                }
            }
        }
        stage('Set image version') {
            steps {
                script {
                    def createEnvFile = "echo IMAGE_TAG=${IMAGE_VERSION} > .env"
                    bat(createEnvFile)
                }
            }
        }
        stage('Install request module') {
            steps {
                script {
                    def installRequestsCommand = "\"C:\\Users\\Toby\\AppData\\Local\\Programs\\Python\\Python311\\python.exe\" -m pip install requests"
                    def installPymysqlCommand = "\"C:\\Users\\Toby\\AppData\\Local\\Programs\\Python\\Python311\\python.exe\" -m pip install pymysql"
                    bat(installRequestsCommand)
                    bat(installPymysqlCommand)
                }
            }
        }
        stage('Deploy Helm Chart') {
            steps {
                script {
                    // Separate the helm upgrade command and its arguments
                    def helmUpgradeCommand = "helm upgrade --install my-release ${HELM_CHART_PATH}"
                    def helmUpgradeArgs = "--set image.tag=${IMAGE_VERSION} --namespace=tobby-dev --debug"

                    // Concatenate the command and arguments and execute
                    def helmDeployCommand = "${helmUpgradeCommand} ${helmUpgradeArgs}"
                    bat(helmDeployCommand)
                }
            }
        }
        stage('Test Deployed Helm Chart') {
            steps {
                script {
                    def testCommand = "\"C:\\Users\\Toby\\AppData\\Local\\Programs\\Python\\Python311\\python.exe\" K8S_backend_testing.py"
                    bat(testCommand)

                    def minikubeServiceCommand = "minikube service python-flask-service --url > k8s_url.txt"
                    bat(minikubeServiceCommand)
                }
            }
        }
    }
    post {
        always {
            script {
                def rmiCommand = "docker rmi ${registry}:${IMAGE_VERSION}"
                def helmDeleteCommand = "helm delete my-release"

                bat(rmiCommand)
                bat(helmDeleteCommand)
            }
        }
    }
}


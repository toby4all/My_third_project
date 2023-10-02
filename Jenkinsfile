pipeline {
    agent any
    triggers {
        pollSCM('H/30 * * * *')
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }
    environment {
        registry = "toby4all/tobby_pipeline"  // Replace with your Docker Hub username and repository
        DOCKERHUB_CREDENTIALS = credentials('dockerhub') // Replace with your Jenkins credentials ID for Docker Hub
        IMAGE_VERSION = "${BUILD_NUMBER}"  // Use the build number as the image version
        IMAGE_TAG = "${BUILD_NUMBER}"  // Define IMAGE_TAG here
        PYTHON_PATH = "C:\\Users\\Toby\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"  // Replace with the correct path to Python on your Jenkins agent
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
                    // Build the Docker image
                    def buildCommand = "docker build -t ${registry}:${IMAGE_VERSION} ."
                    bat(buildCommand)
                }
            }
        }
        stage('Login to Docker Hub') {
            steps {
                script {
                    // Log in to Docker Hub
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
                    // Push the Docker image to Docker Hub
                    def pushCommand = "docker push ${registry}:${IMAGE_VERSION}"
                    bat(pushCommand)
                }
            }
        }
        stage('Set image version') {
            steps {
                script {
                    // Create an environment file to store the image version
                    def createEnvFile = "echo IMAGE_TAG=${IMAGE_VERSION} > .env"
                    bat(createEnvFile)
                }
            }
        }
        stage('Run Docker Compose') {
            steps {
                script {
                    // Start Docker Compose
                    def composeUpCommand = "docker-compose up -d"
                    bat(composeUpCommand)
                }
            }
        }
        stage('install request module') {
            steps {
                script {
                     // Install the 'requests' module
                    def installRequestsCommand = "\"C:\\Users\\Toby\\AppData\\Local\\Programs\\Python\\Python311\\python.exe\" -m pip install requests"
                    bat(installRequestsCommand)
                }
            }
        }
        stage('Test Docker Compose') {
            steps {
                script {
                    // Add Python to the PATH and run the testing script
                    def testCommand = "\"C:\\Users\\Toby\\AppData\\Local\\Programs\\Python\\Python311\\python.exe\" docker_backend_testing.py"
                    bat(testCommand)
                }
            }
        }
        stage('Deploy Helm Chart') {
            steps {
                script {
                    // Deploy the Helm chart
                    def helmDeployCommand = "helm upgrade --install my-release. --set image.tag=${registry}:${IMAGE_VERSION}"
                    bat(helmDeployCommand)
                }
            }
        }
        stage('Test Deployed Helm Chart') {
            steps {
                script {
                    // Test the deployed Helm chart
                    def testCommand = "\"C:\\Users\\Toby\\AppData\\Local\\Programs\\Python\\Python311\\python.exe\" K8S_backend_testing.py"
                    bat(testCommand)

                    // Run the minikube service command and save the URL to a file
                    def minikubeServiceCommand = "minikube service python-flask-service -url > k8s_url.txt"
                    bat(minikubeServiceCommand)
                }
            }
        }
    }
    post {
        always {
            script {
                // Cleanup after the pipeline run
                def downCommand = "docker-compose down"
                def rmiCommand = "docker rmi ${registry}:${IMAGE_VERSION}"
                def helmDeleteCommand = "helm delete my-release"

                bat(downCommand)
                bat(rmiCommand)
                bat(helmDeleteCommand)
            }
        }
    }
}


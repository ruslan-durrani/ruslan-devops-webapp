pipeline {
    agent any

    stages {
        stage('Build Backend Docker Image') {
            steps {
                script {
                    docker.build("ruslan-devops-backend", ".")
                }
            }
        }
        stage('Run Backend Docker Container') {
            steps {
                script {
                    docker.image("ruslan-devops-backend").run("-p 5000:5000")
                }
            }
        }
        stage('Build Frontend Docker Image') {
            steps {
                script {
                    docker.build("ruslan-devops-frontend", ".")
                }
            }
        }
        stage('Run Frontend Docker Container') {
            steps {
                script {
                    docker.image("ruslan-devops-frontend").run("-p 3000:3000")
                }
            }
        }
    }
}

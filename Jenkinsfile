pipeline{
    agent any
    environment {
        DATABASE_URI = credentials("database_uri")
        }
    stages{
        stage('Build images'){
            steps{
                sh "docker-compose build"
            }
        }
        stage('Test'){
            steps{
                sh "python3 -m venv venv"
                sh ". ./venv/bin/activate"
                sh "pip install -r test_requirements.txt"
                sh "pytest --cov"
            }
        }
        stage('Deploy application'){
            steps{
                sh "docker-stack deploy something or other"
            }
        }
    }
}
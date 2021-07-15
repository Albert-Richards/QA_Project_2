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
                sh "pip3 install -r test_requirements.txt"
                sh "python3 -m pytest class_api --cov=app --cov-report html"
                sh "python3 -m pytest species_api --cov=app --cov-report html"
                sh "python3 -m pytest stats_api --cov=app --cov-report html"
                sh "python3 -m pytest server --cov=app --cov-report html"
            }
        }
        stage('Deploy application'){
            steps{
                sh "docker stack deploy --compose-file docker-compose.yaml project_stack"
            }
        }
    }
}

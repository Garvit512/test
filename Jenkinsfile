pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/Garvit512/test.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install requests'
            }
        }
        stage('Run API Test') {
            steps {
                sh 'python job.py https://jsonplaceholder.typicode.com/todos/1 --key userId'
            }
        }
    }
}

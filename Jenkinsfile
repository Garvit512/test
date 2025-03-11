pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Garvit512/test.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install requests'
            }
        }
        stage('Run API Test') {
            steps {
                sh 'python3 job.py https://jsonplaceholder.typicode.com/todos/1 --key userId'
            }
        }
    }
}

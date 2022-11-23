pipeline{
    agent any
    stages {
        stage('Install Python3') {
            steps {
                sh 'sudo apt-get install python3'
                sh 'sudo apt-get install python3-venv'
            }
        }
        stage('Setup Python Virtual ENV'){
        steps  {
            sh '''
            chmod +x envsetup.sh
            ./envsetup.sh
            '''}
        }
        stage('Setup Gunicorn Setup'){
            steps {
                sh '''
                chmod +x gunicorn.sh
                ./gunicorn.sh
                '''
            }
        }
        stage('setup NGINX'){
            steps {
                sh '''
                chmod +x nginx.sh
                ./nginx.sh
                '''
            }
        }
    }
}
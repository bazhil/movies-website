pipeline{
    agent any
    stages {
        stages {
            stage('build') {
                steps {
                    sh 'python --version'
                }
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
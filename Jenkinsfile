pipeline{
    agent any
    stages {
        stage('Install Python3') {
            steps {
                sh 'sudo -i apt-get --assume-yes install python3'
                sh 'sudo -i apt-get --assume-yes install python3-venv'
                sh 'sudo -i apt-get --assume-yes install python3-pip'

            }
        }
        stage('Setup Python Virtual ENV'){
        steps  {
            sh '''
            chmod +x ./scripts/envsetup.sh
            ./scripts/envsetup.sh
            '''}
        }
// TODO: не запускается Gunicorn, поэтому сборка падает. Особо не нужно, но если будет время - разберись!
//         stage('Setup Gunicorn'){
//             steps {
//                 sh '''
//                 chmod +x ./scripts/gunicorn.sh
//                 ./scripts/gunicorn.sh
//                 '''
//             }
//         }
        stage('setup NGINX'){
            steps {
                sh '''
                chmod +x ./scripts/nginx.sh
                ./scripts/nginx.sh
                '''
            }
        }
    }
}
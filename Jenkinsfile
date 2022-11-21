pipeline{
    agent any
    stages {
        stage('Plug Jenkins'){
            steps{
                echo '''
                   Hello Jenkins!
                '''
            }
        }
        stage('Install pip'){
            steps{
                sh '''
                   sudo apt install pip3
                '''
            }
        }
    }
}
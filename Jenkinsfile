pipeline{
    agent any
    stages {
        stage('Plug Jenkins'){
            steps{
                sh '''
                   echo 'Hello Jenkins!'
                '''
            }
        }
        stage('Run pytests'){
            steps{
                sh '''
                   pytest
                '''
            }
        }
    }
}
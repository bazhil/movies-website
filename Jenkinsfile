pipeline{
    agent any
    stages {
        stage('Setup Python Virtual ENV')
        {
            sh '''
            chmod +x envsetup.sh
            ./envsetup
            '''
        }
    }
}
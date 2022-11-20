pipeline{
    agent any
    stages {
        stage('Setup Python Virtual ENV'){
            steps  {
                sh '''
                if [ -d "env" ]
                then
                    echo "Python virtual environment exists."
                else
                    python3 -m venv env
                fi
                '''
            }
        }
        stage('Setup Gunicorn Setup'){
            steps {
                sh '''
                source env/bin/activate

                cd /var/lib/jenkins/workspace/movies-website/

                python3 manage.py makemigrations
                python3 manage.py migrate
                python3 manage.py collectstatic -- no-input

                echo "Migrations done"

                cd /var/lib/jenkins/workspace/movies-website

                sudo cp -rf gunicorn.socket /etc/systemd/system/
                sudo cp -rf gunicorn.service /etc/systemd/system/

                echo "$USER"
                echo "$PWD"

                sudo systemctl daemon-reload
                sudo systemctl start gunicorn

                echo "Gunicorn has started."

                sudo systemctl enable gunicorn

                echo "Gunicorn has been enabled."

                sudo systemctl restart gunicorn


                sudo systemctl status gunicorn
                '''
            }
        }
    }
}
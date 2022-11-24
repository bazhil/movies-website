#!/bin/bash

source env/bin/activate

cd /var/lib/jenkins_home/workspace/movies-website-ci-cd/

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic -- no-input

echo "Migrations done"

cd /var/lib/jenkins_home/workspace/movies-website-ci-cd/

sudo cp -rf gunicorn.socket /etc/systemd/system/
sudo cp -rf gunicorn.service /etc/systemd/system/

echo "$USER"
echo "$PWD"

echo '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'

sudo systemctl status gunicorn

echo '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'

sudo systemctl daemon-reload
sudo systemctl start gunicorn

echo "Gunicorn has started."

sudo systemctl enable gunicorn

echo "Gunicorn has been enabled."

sudo systemctl restart gunicorn


sudo systemctl status gunicorn
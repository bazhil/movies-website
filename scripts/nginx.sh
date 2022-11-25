
#!/bin/bash

sudo apt install nginx

sudo cp -rf movies-website.conf /etc/nginx/sites-available/movies-website
chmod 710 /var/lib/jenkins/workspace/movies-website

sudo ln -s /etc/nginx/sites-available/movies-website /etc/nginx/sites-enabled
sudo nginx -t

sudo systemctl start nginx
sudo systemctl enable nginx

echo "Nginx has been started"

sudo systemctl status nginx
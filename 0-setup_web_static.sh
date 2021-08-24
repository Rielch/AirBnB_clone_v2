#!/usr/bin/env bash
# script that set ups web servera
sudo apt-get update
sudo apt-get install -y nginx
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared
sudo echo "<html>
  <head>
  </head>
  <body>
    <p>Hello World</p>
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ data/web_static/current/
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo service nginx restart
exit 0

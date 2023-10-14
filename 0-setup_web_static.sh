#!/usr/bin/env bash

apt-get update
apt-get -y install nginx

directories=("/data/web_static/releases/test" "/data/web_static/shared/")

for directory in "${directories[@]}"; do
  mkdir -p "$directory"
done

echo "<html>
  <head>
  </head>
  <body>
    <h1>Holberton School</h1>
  </body>
</html>" >/data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to /data/web_static/releases/test/ folder.
ln --symbolic --force /data/web_static/releases/test /data/web_static/current

# Apply ownership recursively to the /data/ folder
chown -R ubuntu:ubuntu /data/

sed -i '/listen 80 default_server;/a \ \n    location /hbnb_static {\n        alias /data/web_static/current/;\n        index index.html;\n    }' /etc/nginx/sites-available/default

sudo service nginx restart
#!/bin/bash

# Configure Nginx to listen on port 80
sed -i 's/80 default_server;/80;/g' /etc/nginx/sites-available/default

# Create a custom HTML file with "Hello World!" content
echo "<html><body>Hello World!</body></html>" > /var/www/html/index.html

# Restart Nginx to apply the changes
service nginx restart

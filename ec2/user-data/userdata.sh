#! /bin/bash
# Update system package repo
sudo yum update -y

# install Apache (httpd)
sudo yum intall -y httpd

# Start Apacher service
sudo systemctl start httpd

# Enable Apache to start at boot
sudo systemctl enable httpd

# Create a customer HTML file
cat <<EoF > /var/www/html/index.html
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to My Website</title>
</head>
<body>
    <h1>Hello World</h1>
    <p>This is a custom HTML page served from my Apache server on EC2.</p>
</body>
</html>
EoF

# Restart Apache to apply changes
sudo systemctl restart httpd
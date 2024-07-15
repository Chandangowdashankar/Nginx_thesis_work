markdown
Copy code
# Dockerized Nginx with fail2ban Integration

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Project Structure](#project-structure)
3. [Setup and Configuration](#setup-and-configuration)
   - [Dockerfile](#dockerfile)
   - [Nginx Configuration](#nginx-configuration)
   - [fail2ban Configuration](#fail2ban-configuration)
   - [Custom Python Script](#custom-python-script)
4. [Build and Run](#build-and-run)
5. [Monitoring Tools](#monitoring-tools)
6. [Accessing the Services](#accessing-the-services)
7. [Conclusion](#conclusion)

---

## Prerequisites

Ensure you have the following installed on your system:

- Docker
- Docker Compose

---

## Project Structure

.
├── Dockerfile
├── docker-compose.yml
├── nginx.conf
├── fail2ban
│ ├── jail.local
│ └── filter.d
│ └── nginx-http-auth.conf
└── scripts
└── monitor_logs.py

bash
Copy code

---

## Setup and Configuration

### Dockerfile

```dockerfile
# Use an official Nginx image from Docker Hub
FROM nginx:latest

# Set maintainer label
LABEL maintainer="your-email@example.com"

# Remove default server definition
RUN rm /etc/nginx/conf.d/default.conf

# Copy your Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Install fail2ban
RUN apt-get update && apt-get install -y fail2ban

# Copy fail2ban configuration
COPY fail2ban/jail.local /etc/fail2ban/jail.local
COPY fail2ban/filter.d/nginx-http-auth.conf /etc/fail2ban/filter.d/nginx-http-auth.conf

# Copy custom Python script
COPY scripts/monitor_logs.py /usr/local/bin/monitor_logs.py

# Set file permissions
RUN chmod -R 644 /etc/nginx/nginx.conf

# Expose ports
EXPOSE 80 443

# Start Nginx and fail2ban
CMD service fail2ban start && nginx -g 'daemon off;'
Nginx Configuration
Create an nginx.conf file to configure Nginx securely.

nginx
Copy code
user nginx;
worker_processes auto;

error_log /var/log/nginx/error.log warn;
pid /var/run/nginx.pid;

events {
    worker_connections 1024;
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for"';

    access_log /var/log/nginx/access.log main;

    sendfile on;
    keepalive_timeout 65;

    # Enable Gzip
    gzip on;

    include /etc/nginx/conf.d/*.conf;

    # Security headers
    add_header X-Content-Type-Options nosniff;
    add_header X-Frame-Options "SAMEORIGIN";
    add_header X-XSS-Protection "1; mode=block";
}
fail2ban Configuration
Create a jail.local file for fail2ban configuration.

ini
Copy code
[nginx-http-auth]
enabled = true
filter = nginx-http-auth
action = iptables[name=HTTP, port=http, protocol=tcp]
logpath = /var/log/nginx/error.log
maxretry = 3
Create a custom filter for Nginx in fail2ban/filter.d/nginx-http-auth.conf.

ini
Copy code
[Definition]
failregex = no user/password was provided for basic authentication.*client: <HOST>
ignoreregex =
Custom Python Script
Create a Python script scripts/monitor_logs.py to monitor logs and send alerts.

python
Copy code
import os
import smtplib
from email.mime.text import MIMEText

LOG_FILE = "/var/log/nginx/access.log"
THRESHOLD = 100

def read_log():
    with open(LOG_FILE, "r") as file:
        lines = file.readlines()
    return lines

def alert_admin(message):
    msg = MIMEText(message)
    msg['Subject'] = 'Nginx Alert'
    msg['From'] = 'admin@example.com'
    msg['To'] = 'admin@example.com'

    with smtplib.SMTP('localhost') as server:
        server.send_message(msg)

def monitor_logs():
    log_lines = read_log()
    if len(log_lines) > THRESHOLD:
        alert_admin(f"High traffic detected: {len(log_lines)} requests")

if __name__ == "__main__":
    monitor_logs()
Build and Run
Build the Docker Image:

sh
Copy code
docker build -t secure-nginx .
Run the Docker Container:

sh
Copy code
docker run -d \
  --name secure-nginx \
  --user nginx \
  --read-only \
  --tmpfs /var/cache/nginx \
  --tmpfs /var/log/nginx \
  -p 80:80 -p 443:443 \
  secure-nginx
Monitoring Tools
Consider using the following tools for monitoring your Docker containers:

Prometheus and Grafana: For detailed metrics and custom dashboards.
Datadog: For a comprehensive, cloud-based solution with advanced features.
ELK Stack: For powerful log management and analytics.
cAdvisor: For lightweight, real-time container monitoring.
Portainer: For an easy-to-use management UI.
Refer to the respective documentation for setup and integration.

Accessing the Services
Nginx: Access the Nginx web server via http://localhost.
fail2ban: fail2ban runs in the background and logs actions to /var/log/fail2ban.log.

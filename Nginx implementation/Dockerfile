# Base image
FROM nginx:latest

# Install necessary packages
RUN apt-get update && apt-get install -y fail2ban python3 python3-pip

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Copy Fail2Ban configuration
COPY fail2ban/jail.local /etc/fail2ban/jail.local
COPY fail2ban/filter.d/nginx-http-auth.conf /etc/fail2ban/filter.d/nginx-http-auth.conf

# Copy custom script
COPY scripts/monitor_logs.py /usr/local/bin/monitor_logs.py
RUN chmod +x /usr/local/bin/monitor_logs.py

# Expose ports
EXPOSE 80

# Start services
CMD service fail2ban start && nginx -g 'daemon off;'

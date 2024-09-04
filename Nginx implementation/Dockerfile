# Stage 1: Build stage for installing packages and dependencies
FROM python:3.9-alpine as builder

# Install necessary packages and dependencies
RUN apk add --no-cache \
    nginx \
    fail2ban \
    py3-pip

# Install Python packages
RUN pip install --no-cache-dir some-python-package

# Copy configurations
COPY fail2ban/jail.local /etc/fail2ban/jail.local
COPY fail2ban/filter.d/nginx-http-auth.conf /etc/fail2ban/filter.d/nginx-http-auth.conf

# Copy custom script
COPY scripts/monitor_logs.py /usr/local/bin/monitor_logs.py
RUN chmod +x /usr/local/bin/monitor_logs.py

# Stage 2: Final image
FROM nginx:latest

# Copy Nginx configuration from the builder stage
COPY nginx.conf /etc/nginx/nginx.conf

# Copy Fail2Ban and custom scripts from the builder stage
COPY --from=builder /etc/fail2ban /etc/fail2ban
COPY --from=builder /usr/local/bin/monitor_logs.py /usr/local/bin/monitor_logs.py

# Expose ports
EXPOSE 80

# Start services
CMD service fail2ban start && nginx -g 'daemon off;'

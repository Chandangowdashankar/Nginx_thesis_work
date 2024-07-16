FROM nginx:latest

# Copy the AppArmor profile into the container
COPY nginx.apparmor /etc/apparmor.d/nginx

# Set AppArmor profile to enforce mode
RUN ln -s /etc/apparmor.d/nginx /etc/apparmor.d/disable/
RUN apparmor_parser -r /etc/apparmor.d/nginx

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]


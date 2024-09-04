# Multi-Layer Security for Nginx: Server, Container, and Web Server-Level Defense Against Denial-of-Service Attacks

This repository provides configurations and source code to implement a multi-layer security strategy for Nginx, designed to protect against Denial-of-Service (DoS) attacks. The approach covers defenses at the server level, container level, and within the web server itself.

## Security Layers Overview

### Layer 1: Server-Level Defense

**Description:**
Implement server-level protections using firewall rules and IP filtering to block malicious traffic before it reaches the Nginx server. This helps to prevent DoS attacks and excessive load on the web server.

### Layer 2: Container-Level Defense

**Description:**
Configure Docker container limits to control CPU and memory usage, isolating the Nginx instance and protecting the host system from resource exhaustion due to potential DoS attacks.

### Layer 3: Web Server-Level Defense

**Description:**
Utilize Nginx's built-in features for enhanced security:
- **Rate Limiting**: Controls the rate of requests to prevent abuse.
- **IP Whitelisting**: Restricts access to trusted IP addresses only.
- **Web Application Firewall (WAF)**: Filters and blocks malicious requests.

## Code and Configurations

All code snippets and configurations related to these security layers are provided in this repository. Please refer to the files for detailed implementations and setup instructions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


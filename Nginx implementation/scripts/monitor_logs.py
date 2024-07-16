import time

def monitor_logs():
    log_file = "/var/log/nginx/access.log"
    with open(log_file, "r") as f:
        f.seek(0, 2)  # Move to the end of the file
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            # Perform custom actions based on the log line
            print(line)

if __name__ == "__main__":
    monitor_logs()


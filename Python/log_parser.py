import time
import datetime

Log_file =  "portfolio-website/application.log"
Window = 300
Threshold = 5
error_count = []
ALERT_FILE = "alerts.log"

def monitor_logs():
    with open(Log_file, "r") as f:
      
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            
            # Check for errors in the line
            if "ERROR" in line:
                now = datetime.datetime.now()
                error_count.append(now)
                print(f"Error detected at {now}: {line.strip()}")
                
                # Remove errors outside the time window
                error_count[:] = [t for t in error_count if (now - t).seconds <= Window]
                
                # Check if threshold is exceeded
                if len(error_count) >= Threshold:
                    alert = f"{now} ALERT: {len(error_count)} errors in last 5 min\n"
                    print(alert)
                    with open(ALERT_FILE, "a") as out:
                        out.write(alert)

if __name__ == "__main__":
    monitor_logs()
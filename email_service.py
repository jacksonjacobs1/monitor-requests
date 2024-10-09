import os
import smtplib
from email.mime.text import MIMEText
import time
import argparse

if __name__ == "__main__":
    to_email = "jjaco34@emory.edu"
    log_path = "app.log"

    while True:
        print("Starting the check")
        now = time.time()
        latest_log = os.path.getmtime(log_path)

        if now - latest_log > 300:
            os.system(f"echo 'The log file has not been updated in the last 5 minutes' | mail -s 'Log file not updated' {to_email}")
            print("Email sent")

        time.sleep(1000)
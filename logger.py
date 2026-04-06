import os
from datetime import datetime

log_filename = None

def check_output_dir():
    os.makedirs("output", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

def setup_log_file():
    global log_filename
    check_output_dir()
    log_filename = f"logs/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

def log(msg):
    print(msg)
    with open(log_filename, 'a') as f:
        f.write(msg + "\n")
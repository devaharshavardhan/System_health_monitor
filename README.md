# System Health Monitoring Web Application

## Overview
This project provides a simple web-based dashboard to monitor system health logs, including CPU, memory, and disk usage. The system logs are generated every minute using a cron job and displayed via a Flask web application.

## Project Structure
```
├── app.py                    # Flask web application to display logs
├── system_health_monitor.sh  # Bash script to monitor system health
├── crontab.txt               # Cron job configuration to run monitoring script
├── README.md                 # Documentation
```

## Features
- Monitors system CPU, memory, and disk usage.
- Logs system health data to a file (`/home/ubuntu/system_health.log`).
- Displays the last 10 log entries in a web interface.
- Provides a refresh button to update logs dynamically.

## Setup Instructions

### 1. Install Dependencies
Ensure you have Python and Flask installed on your system:
```sh
sudo apt update
sudo apt install python3 python3-pip -y
```

### 2. Set Up a Virtual Environment
```sh
python3 -m venv venv
source venv/bin/activate
pip install flask
```

### 3. Set Up the Monitoring Script
Give execution permission to the monitoring script:
```sh
chmod +x /home/ubuntu/system_health_monitor.sh
```

### 4. Set Up Cron Job
To run the script every minute, add the following line to your cron jobs:
```sh
crontab -e
```
Then, add:
```sh
* * * * * /home/ubuntu/system_health_monitor.sh >> /home/ubuntu/system_health.log 2>&1
```
Save and exit.

### 5. Run the Flask Application in the Virtual Environment
```sh
source venv/bin/activate
python3 app.py
```
By default, the app runs on `http://0.0.0.0:5000`.

### 6. Access the Web Dashboard
Open a browser and navigate to:
```
http://<your-server-ip>:5000
```

## API Endpoints
- `/` - Displays the web interface with system health logs.
- `/api/logs` - Returns the latest log entries in HTML format.

## License
This project is open-source and available for free use.


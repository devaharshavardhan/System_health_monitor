from flask import Flask, render_template_string

app = Flask(__name__)

LOG_FILE = "/home/ubuntu/system_health.log"

def read_log():
    """Read the last 10 lines from the system health log."""
    try:
        with open(LOG_FILE, "r") as file:
            lines = file.readlines()[-10:]  #This will get the last 10 entries of log files
        return lines
    except FileNotFoundError:
        return ["No logs found."]

@app.route('/')
def index():
    logs = read_log()
    log_entries = []
    for log in logs:
        date, log_details = log.split(":", 1) if ":" in log else ("Unknown", log)
        log_entries.append({"date": date, "details": log_details.strip()})
        
    return render_template_string("""
        <html>
            <head>
                <title>System Health Logs</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f7f9fc; /* Light gray background */
                        color: #333; /* Dark text color for readability */
                        text-align: center;
                        padding: 20px;
                    }
                    h1 {
                        color: #34495e; /* Dark blue heading */
                    }
                    table {
                        width: 80%;
                        margin: 0 auto;
                        border-collapse: collapse;
                        background-color: #ffffff; /* White background for table */
                        border-radius: 8px;
                        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
                    }
                    th, td {
                        padding: 12px;
                        text-align: left;
                        border-bottom: 1px solid #ddd;
                    }
                    th {
                        background-color: #2c3e50; /* Dark blue header */
                        color: white;
                    }
                    tr:hover {
                        background-color: #ecf0f1; /* Light gray row hover effect */
                    }
                    button {
                        padding: 12px 24px;
                        font-size: 16px;
                        margin-top: 20px;
                        background-color: #2c3e50; /* Dark blue button */
                        color: white;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                    }
                    button:hover {
                        background-color: #34495e; /* Lighter blue on hover */
                    }
                    pre {
                        background-color: #f4f4f4;
                        padding: 10px;
                        border-radius: 5px;
                        text-align: left;
                        white-space: pre-wrap;
                        margin-top: 20px;
                    }
                </style>
            </head>
            <body>
                <h1>System Health Logs</h1>
                <table>
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>Log Details</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for entry in log_entries %}
                            <tr>
                                <td>{{ entry.date }}</td>
                                <td>{{ entry.details }}</td>
                            </tr>
                        {% endfor %}
                    </tbody>
                </table>
                <button onclick="refreshLogs()">Refresh Logs</button>
                <script>
                    function refreshLogs() {
                        fetch('/api/logs')
                        .then(response => response.text())
                        .then(data => {
                            document.body.innerHTML = `
                                <h1>System Health Logs</h1>
                                <table>
                                    <thead>
                                        <tr>
                                            <th>Date</th>
                                            <th>Log Details</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        ${data}
                                    </tbody>
                                </table>
                                <button onclick="refreshLogs()">Refresh Logs</button>
                            `;
                        });
                    }
                </script>
            </body>
        </html>
    """, log_entries=log_entries)

@app.route('/api/logs')
def api_logs():
    """API endpoint to get log data."""
    log_entries = read_log()
    log_html = ""
    for log in log_entries:
        date, log_details = log.split(":", 1) if ":" in log else ("Unknown", log)
        log_html += f"""
            <tr>
                <td>{date}</td>
                <td>{log_details.strip()}</td>
            </tr>
        """
    return log_html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# Log Analyzer Tool

This project is a Python-based log analyzer that processes server log files and generates useful summaries and statistics.

The tool is designed to handle real-world messy log files instead of only perfect input. It supports multiple log formats, malformed lines, JSON logs, different timestamp formats, and different response time units without crashing.

---

## Features

- Handles multiple timestamp formats
- Supports normal text logs and JSON logs
- Detects malformed or broken log lines
- Handles missing status codes
- Supports response times in milliseconds and seconds
- Shows top endpoints and IP addresses
- Calculates average response times
- Detects high malformed log percentages

---

## Project Structure

log-analyzer-assessment/

- analyzer.py → Main analyzer program
- parser.py → Log parsing logic
- stats.py → Statistics generation
- README.md
- ANSWERS.md
- requirements.txt

scripts/
- generate_logs.py → Generates sample logs for testing

sample_logs/
- test.log → Generated sample log file

---

## Requirements

- Python 3.x
- python-dateutil

---

## Setup Instructions

### 1. Create virtual environment

py -m venv venv

### 2. Activate virtual environment

venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

---

## Generate Sample Logs

Run the following command:

python scripts/generate_logs.py

This will generate a sample log file inside:

sample_logs/test.log

---

## Run the Analyzer

Run:

python analyzer.py sample_logs/test.log

---

## Example Output

===== LOG ANALYSIS REPORT =====

Total lines: 1000
Valid logs: 889
Malformed lines: 111

Top endpoints:
/api/users
/api/login

Top IPs:
10.0.0.5
172.16.0.3

===== END OF REPORT =====

---

## Notes

The analyzer is built to fail gracefully. Malformed or unexpected lines are skipped safely and counted instead of crashing the application.
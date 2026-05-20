# ANSWERS

## 1. How to run

### Create virtual environment

py -m venv venv

### Activate virtual environment

venv\Scripts\activate

### Install dependencies

pip install -r requirements.txt

### Generate sample logs

python scripts/generate_logs.py

### Run analyzer

python analyzer.py sample_logs/test.log

---

## 2. Stack choice

I chose Python because it is simple, fast to develop with, and very strong for text processing and parsing tasks. Python also has good support for handling JSON, regular expressions, and malformed data, which made it suitable for this assessment.

I wanted to focus more on handling unexpected input and building a reliable parser instead of spending time on frontend or UI development.

A worse choice for this task would have been using a heavy web framework because the main challenge here is parsing and analyzing data, not building a user interface.

---

## 3. One real edge case

One important edge case handled by the project is malformed or empty log lines.

File:
parser.py

Function:
parse_log_line()

The parser safely checks for blank or malformed lines and returns None instead of crashing the application.

Without this handling, the analyzer could stop working completely if the log file contained partial writes, broken entries, or unexpected formats.

---

## 4. AI usage

I used ChatGPT during development to help brainstorm the project structure, improve parsing logic, and improve the reporting format.

I also used it to discuss better ways to handle malformed logs and mixed timestamp formats.

One thing I changed from the AI-generated suggestions was simplifying some of the parsing logic to make the code easier to read and maintain. I also adjusted parts of the response time parsing to better support multiple formats.

---

## 5. Honest gap

One thing that could be improved is the output format.

Currently, the analyzer only prints results in the terminal. With more time, I would add features like exporting reports to JSON or CSV, filtering logs by endpoint or status code, and adding better anomaly detection.
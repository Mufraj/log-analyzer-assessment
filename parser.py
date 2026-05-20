import re
import json
from dateutil import parser as date_parser

LOG_PATTERN = re.compile(
    r"^(?P<timestamp>.+?)\s+"
    r"(?P<ip>\d+\.\d+\.\d+\.\d+)\s+"
    r"(?P<method>GET|POST|PUT|DELETE)\s+"
    r"(?P<path>/\S+)\s+"
    r"(?P<status>\d+|-)\s+"
    r"(?P<response_time>\S+)"
)

def parse_timestamp(timestamp):

    try:
        return date_parser.parse(timestamp)

    except:
        return None

def parse_response_time(response_time):

    try:

        if response_time.endswith("ms"):
            return float(response_time.replace("ms", ""))

        elif response_time.endswith("s"):
            return float(response_time.replace("s", "")) * 1000

        else:
            return float(response_time)

    except:
        return None

def parse_json_log(line):

    try:
        data = json.loads(line)

        return {
            "timestamp": parse_timestamp(data.get("timestamp", "")),
            "ip": data.get("ip"),
            "method": data.get("method"),
            "path": data.get("path"),
            "status": data.get("status"),
            "response_time": parse_response_time(
                str(data.get("response_time", ""))
            )
        }

    except:
        return None

def parse_text_log(line):

    match = LOG_PATTERN.match(line)

    if not match:
        return None

    data = match.groupdict()

    return {
        "timestamp": parse_timestamp(data["timestamp"]),
        "ip": data["ip"],
        "method": data["method"],
        "path": data["path"],
        "status": None if data["status"] == "-" else int(data["status"]),
        "response_time": parse_response_time(data["response_time"])
    }

def parse_log_line(line):

    line = line.strip()

    if not line:
        return None

    if line.startswith("{"):
        return parse_json_log(line)

    return parse_text_log(line)
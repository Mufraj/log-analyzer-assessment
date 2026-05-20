import random
import json
from datetime import datetime, timedelta

methods = ["GET", "POST", "PUT", "DELETE"]
paths = [
    "/api/users",
    "/api/login",
    "/api/products",
    "/api/orders",
    "/api/report"
]

status_codes = [200, 201, 400, 401, 404, 500]

ips = [
    "192.168.1.1",
    "10.0.0.5",
    "172.16.0.3",
    "203.0.113.9"
]

def random_timestamp():
    now = datetime.now()

    formats = [
        now.isoformat(),
        now.strftime("%Y/%m/%d %H:%M:%S"),
        now.strftime("%d-%b-%Y %H:%M:%S"),
        str(int(now.timestamp()))
    ]

    return random.choice(formats)

def random_response_time():
    choices = [
        f"{random.randint(10, 500)}ms",
        f"{round(random.uniform(0.1, 2.0), 3)}s",
        str(random.randint(10, 500))
    ]

    return random.choice(choices)

def generate_normal_log():
    return (
        f"{random_timestamp()} "
        f"{random.choice(ips)} "
        f"{random.choice(methods)} "
        f"{random.choice(paths)} "
        f"{random.choice(status_codes)} "
        f"{random_response_time()}"
    )

def generate_missing_status_log():
    return (
        f"{random_timestamp()} "
        f"{random.choice(ips)} "
        f"{random.choice(methods)} "
        f"{random.choice(paths)} "
        f"- "
        f"{random_response_time()}"
    )

def generate_json_log():
    log = {
        "timestamp": random_timestamp(),
        "ip": random.choice(ips),
        "method": random.choice(methods),
        "path": random.choice(paths),
        "status": random.choice(status_codes),
        "response_time": random_response_time()
    }

    return json.dumps(log)

def generate_malformed_log():
    malformed = [
        "THIS IS BROKEN LOG",
        "ERROR ERROR",
        "",
        "null null null",
        "2024 incomplete"
    ]

    return random.choice(malformed)

def main():
    output_file = "sample_logs/test.log"

    with open(output_file, "w") as file:

        for _ in range(1000):

            log_type = random.choices(
                ["normal", "missing", "json", "malformed"],
                weights=[70, 10, 10, 10]
            )[0]

            if log_type == "normal":
                line = generate_normal_log()

            elif log_type == "missing":
                line = generate_missing_status_log()

            elif log_type == "json":
                line = generate_json_log()

            else:
                line = generate_malformed_log()

            file.write(line + "\n")

    print(f"Log file generated: {output_file}")

if __name__ == "__main__":
    main()
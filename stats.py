from collections import Counter, defaultdict

def generate_stats(parsed_logs):

    stats = {
        "total_requests": 0,
        "status_codes": Counter(),
        "methods": Counter(),
        "top_paths": Counter(),
        "top_ips": Counter(),
        "response_times": defaultdict(list)
    }

    for log in parsed_logs:

        if not log:
            continue

        stats["total_requests"] += 1

        if log["status"] is not None:
            stats["status_codes"][log["status"]] += 1

        if log["method"]:
            stats["methods"][log["method"]] += 1

        if log["path"]:
            stats["top_paths"][log["path"]] += 1

        if log["ip"]:
            stats["top_ips"][log["ip"]] += 1

        if (
            log["path"]
            and log["response_time"] is not None
        ):
            stats["response_times"][log["path"]].append(
                log["response_time"]
            )

    return stats

def calculate_average_response_times(response_times):

    averages = {}

    for path, times in response_times.items():

        if times:
            averages[path] = round(sum(times) / len(times), 2)

    return averages
import sys

from parser import parse_log_line
from stats import (
    generate_stats,
    calculate_average_response_times
)

def main():

    if len(sys.argv) != 2:

        print("Usage: python analyzer.py <log_file>")
        return

    log_file = sys.argv[1]

    parsed_logs = []

    malformed_lines = 0
    total_lines = 0

    try:

        with open(log_file, "r") as file:

            for line in file:

                total_lines += 1

                parsed = parse_log_line(line)

                if parsed:
                    parsed_logs.append(parsed)

                else:
                    malformed_lines += 1

    except FileNotFoundError:

        print(f"File not found: {log_file}")
        return

    stats = generate_stats(parsed_logs)

    average_response_times = calculate_average_response_times(
        stats["response_times"]
    )

    print("\n===== LOG ANALYSIS REPORT =====\n")

    print(f"Total lines: {total_lines}")
    print(f"Valid logs: {len(parsed_logs)}")
    print(f"Malformed lines: {malformed_lines}")

    malformed_percentage = (
        malformed_lines / total_lines
    ) * 100

    print(
        f"Malformed percentage: "
        f"{malformed_percentage:.2f}%"
    )

    if malformed_percentage > 10:
        print(
            "Warning: High malformed log rate detected."
        )

    print("\n--- HTTP Methods ---")

    for method, count in stats["methods"].items():
        print(f"{method}: {count}")

    print("\n--- Status Codes ---")

    for status, count in stats["status_codes"].items():
        print(f"{status}: {count}")

    print("\n--- Top Endpoints ---")

    for path, count in stats["top_paths"].most_common(5):
        print(f"{path}: {count}")

    print("\n--- Top IP Addresses ---")

    for ip, count in stats["top_ips"].most_common(5):
        print(f"{ip}: {count}")

    print("\n--- Average Response Times ---")

    sorted_response_times = sorted(
        average_response_times.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for path, avg in sorted_response_times[:5]:
        print(f"{path}: {avg} ms")

    print("\n===== END OF REPORT =====\n")

if __name__ == "__main__":
    main()
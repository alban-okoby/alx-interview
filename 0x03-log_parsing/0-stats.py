#!/usr/bin/python3


import signal
import sys

total_file_size = 0
status_code_counts = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


def print_stats():
    print(f"File size: {total_file_size}")
    for status_code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{status_code}: {count}")


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    line = line.strip()
    try:
        parts = line.split()
        ip_address = parts[0]
        date = parts[3][1:-1]
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        total_file_size += file_size
        status_code_counts[status_code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print_stats()

    except (IndexError, ValueError):
        continue

print_stats()

#!/usr/bin/python3
"""This script reads standard input compute metrics
    after every ten lines or keyboard interrupt"""
import sys
import re


def print_status_codes(status_codes: dict, total_size: int) -> None:
    """print status codes in list"""
    print("File size: {}".format(total_size))
    for code, count in status_codes.items():
        if count > 0:
            print("{}: {}".format(code, count))


regex_format = (r'^(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] '
                r'"GET /projects/\d+ HTTP/1\.1" (\d+) (\d+)$')

line_count = 0
total_file_size = 0
status = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        stdin_entry = line.strip()
        get_match = re.match(regex_format, stdin_entry)
        if get_match:
            status_code = get_match.group(3)
            file_size = get_match.group(4)
            total_file_size += int(file_size)
            line_count += 1
            for codes in status.keys():
                if codes == status_code:
                    if int(status_code):
                        status[codes] += 1
        if line_count % 10 == 0:
            print_status_codes(status, total_file_size)
except Exception as error:
    print_status_codes(status, total_file_size)
    raise
finally:
    print_status_codes(status, total_file_size)

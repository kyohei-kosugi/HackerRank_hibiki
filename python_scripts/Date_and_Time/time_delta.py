#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

# Complete the time_delta function below.
def time_delta(t1, t2):
    pattern = r'(\w{3} \d{2} \w{3} \d{4} \d{2}:\d{2}:\d{2}) ([+-]\d{4})'
    match_t1 = re.match(pattern, t1)
    match_t2 = re.match(pattern, t2)

    date_format = '%a %d %b %Y %H:%M:%S'

    if match_t1 and match_t2:
        date_str_t1, timezone_str_t1 = match_t1.groups()
        date_str_t2, timezone_str_t2 = match_t2.groups()

        dt_t1 = datetime.strptime(date_str_t1, date_format)
        dt_t2 = datetime.strptime(date_str_t2, date_format)

        timezone_offset_minutes_t1 = int(timezone_str_t1) // 100 * 60 + int(timezone_str_t1) % 100
        timezone_offset_minutes_t2 = int(timezone_str_t2) // 100 * 60 + int(timezone_str_t2) % 100

        timezone_offset_t1 = timedelta(minutes=timezone_offset_minutes_t1)
        timezone_offset_t2 = timedelta(minutes=timezone_offset_minutes_t2)
        
        dt_with_timezone_t1 = dt_t1 - timezone_offset_t1
        dt_with_timezone_t2 = dt_t2 - timezone_offset_t2

        seconds_since_epoch_t1 = (dt_with_timezone_t1 - datetime(1970, 1, 1)).total_seconds()
        seconds_since_epoch_t2 = (dt_with_timezone_t2 - datetime(1970, 1, 1)).total_seconds()

        return str(int(abs(seconds_since_epoch_t1 - seconds_since_epoch_t2)))

    else:
        raise ValueError("Invalid input format")
    
    """Optimize
    fmt = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    diff = dt2 - dt1
    return str(abs(int(diff.total_seconds()))) """




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH_2'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

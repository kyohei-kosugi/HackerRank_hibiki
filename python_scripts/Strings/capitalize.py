#!/bin/python3

import math
import os
import random
import re
import sys
from dotenv import load_dotenv

# Complete the solve function below.
load_dotenv()

def solve(s):
    pattern = r'\b\w'
    result_string = re.sub(pattern, lambda match: match.group(0).capitalize(), s)
    
    return result_string

"""
    kyohei  kosugi  lol testwords = s.split()
    t = []
    for word in words:
        t.append(word.capitalize())
    return ' '.join(t)
"""

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
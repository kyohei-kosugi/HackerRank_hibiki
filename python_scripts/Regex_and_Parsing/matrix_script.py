#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decode_list = []

for i in range(m):
    for j in range (n):
        decode_list.append(matrix[j][i])

original_output = ''.join(decode_list)
decode_pattern = r'([a-zA-Z])([!@#$%&\s]+)([a-zA-Z])'
output = re.sub(decode_pattern, r'\1 \3', original_output)

print(output)
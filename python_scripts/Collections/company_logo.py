#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    char_counts = Counter(s)

    letters = set(s)
    count_list = []
    for letter in letters:
        count_list.append((letter, char_counts[letter]))
    
    sort_data = sorted(count_list, key=lambda x: (-x[1], x[0]))

    for i in range(3):
        print(sort_data[i][0], sort_data[i][1])



"""
from collections import Counter

if __name__ == '__main':
    s = input()
    char_counts = Counter(s)

    # カウントリストを生成し、ソートを行う代わりに直接Counterを使う
    count_list = char_counts.items()
    
    # ソートを1回行うだけに変更
    sorted_data = sorted(count_list, key=lambda x: (-x[1], x[0]))

    # 上位3つの頻出文字を表示
    for letter, count in sorted_data[:3]:
        print(letter, count)
"""
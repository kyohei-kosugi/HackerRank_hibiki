#!/bin/python3

if __name__ == '__main__':
    n, m = map(int, input().split())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    arr.sort(key=lambda x: x[k])

    [print(*score_list) for score_list in arr]

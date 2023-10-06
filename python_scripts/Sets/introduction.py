def average(array):
    # your code goes here
    set_list = set(array)
    distinct_count = len(set_list)
    avr = round(float(sum(set_list) / distinct_count), 3)
    return avr

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
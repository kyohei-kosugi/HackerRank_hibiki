n, m = map(int, input().split())

for i in range(n):
    if i == int((n-1)/2):
        print("-"* int((m-7)/2) + "WELCOME" + "-"* int((m-7)/2))
    elif i < int((n-1)/2):
        print("-" * int((m - 3*(2*i+1))/2) + ".|."* (2*i+1) + "-" * int((m - 3*(2*i+1))/2))
    else:
        print("-" * 3*int(i - (n-1)/2) + ".|." * int((m - 6*(i - (n-1)/2))/3) + "-" * 3*int(i - (n-1)/2))
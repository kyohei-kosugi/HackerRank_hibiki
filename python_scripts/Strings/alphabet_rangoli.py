def print_rangoli(size):
    # your code goes here
    s = size
    h = 2*s - 1
    w = 2*(2*s - 1) - 1
    alp = 'abcdefghijklmnopqrstuvwxyz'
    mid = int((h-1)/2)

    for i in range(h):
        if i <= mid:
            print('-'* (int((w-1)/2)-2*i), end='')
            for j in range(2*i+1):
                if j == 2*i:
                    print(alp[s-1], end='')
                elif j == i:
                    print(alp[s-j-1] + '-', end='')
                elif j < i:
                    print(alp[s-j-1] + '-', end='')
                else:
                    print(alp[j+mid-2*i] + '-', end='')
            print('-'* (int((w-1)/2)-2*i))                  
        else:
            r = 2*mid - i
            print('-'* (int((w-1)/2)-2*r), end='')
            for j in range(2*r+1):
                if j == 2*r:
                    print(alp[s-1], end='')
                elif j == r:
                    print(alp[s-j-1] + '-', end='')
                elif j < r:
                    print(alp[s-j-1] + '-', end='')
                else:
                    print(alp[j+mid-2*r] + '-', end='')
            print('-'* (int((w-1)/2)-2*r))          
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)



""" import string
def print_rangoli(n):
    width = n * 4 - 3
    re_alpha = list(string.ascii_lowercase[0:n][::-1])
    
    for i in range(n):
        row = re_alpha[:(i+1)] + re_alpha[:i][::-1]
        print("-".join(row).center(width, "-"))
        
    for i in range(n-2, -1, -1):
        row = re_alpha[:(i+1)] + re_alpha[:i][::-1]
        print("-".join(row).center(width, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n) """

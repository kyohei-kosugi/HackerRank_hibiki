for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(int(10**(i-1) + 10**(i-2) + 10**(i-3) + 10**(i-4) + 10**(i-5) + 10**(i-6) + 10**(i-7) + 10**(i-8) + 10**(i-9)) * i)



""" 
for i in range(1,int(input())): 
    print(i * (10**i - 1)//9)


for i in range(1,int(input())): 
    print(int(ascii(1) * i) * i)
 """
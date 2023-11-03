cube = lambda x: pow(x, 3) # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fibonacci_list = []
    for i in range(n):
        if i == 0:
            fibonacci_list.append(i)
        elif i == 1:
            fibonacci_list.append(i)
        else:
            number = int(fibonacci_list[i-2] + fibonacci_list[i-1])
            fibonacci_list.append(number)
    return fibonacci_list

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
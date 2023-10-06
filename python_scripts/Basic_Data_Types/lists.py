if __name__ == '__main__':
    N = int(input())
    list = []

    # com_arg = input()
    # input_parts = com_arg.split()
    # e = int(input_parts[2])
    # print(type(input_parts[0]))
    # print(type(input_parts[1]))
    # print(type(input_parts[2]))
    # print(type(e))


    

for _ in range(N):
    com_arg = input()
    input_parts = com_arg.split()

    command = input_parts[0]
    
    if command == 'insert':
        e = int(input_parts[1])
        i = int(input_parts[2])
        list.insert(e, i)
    elif command == 'print':
        print(list)
    elif command == 'remove':
        e = int(input_parts[1])
        list.remove(e)
    elif command == 'append':
        e = int(input_parts[1])
        list.append(e)
    elif command == 'sort':
        list.sort()
    elif command == 'pop':
        list.pop()
    elif command == 'reverse':
        list.reverse()
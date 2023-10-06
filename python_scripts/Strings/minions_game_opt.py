def minion_game(string):
    vowels = 'AEIOU'
    n = len(string)
    kevin_count = 0
    stuart_count = 0

    for i in range(n):
        if string[i] in vowels:
            kevin_count += n - i
        else:
            stuart_count += n - i

    if kevin_count > stuart_count:
        print('Kevin', kevin_count)
    elif stuart_count > kevin_count:
        print('Stuart', stuart_count)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
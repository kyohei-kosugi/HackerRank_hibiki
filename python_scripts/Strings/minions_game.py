def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    n = len(string)
    kevin_count = 0
    stuart_count = 0
    kevin_unique_words = set()
    stuart_unique_words = set()

    for i in range(n):
        if string[i] in vowels:
            for j in range(i, n):
                word = string[i:j+1]
                if word not in kevin_unique_words:
                    start = 0
                    word_count = 0
                    while start < len(string):
                        start = string.find(word, start)
                        if start == -1:
                            break
                        word_count += 1
                        start += 1
                    kevin_count += word_count
                    kevin_unique_words.add(word)
    
    for i in range(n):
        if string[i] not in vowels:
            for j in range(i, n):
                word = string[i:j+1]
                if word not in stuart_unique_words:
                    start = 0
                    word_count = 0
                    while start < len(string):
                        start = string.find(word, start)
                        if start == -1:
                            break
                        word_count += 1
                        start += 1
                    stuart_count += word_count
                    stuart_unique_words.add(word)
    
    if kevin_count > stuart_count:
        print('Kevin', kevin_count)
    elif stuart_count > kevin_count:
        print('Stuart', stuart_count)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
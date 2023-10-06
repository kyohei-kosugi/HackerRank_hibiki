n = int(input())
words = [input() for _ in range(n)]

unique_count = len(set(words))
print(unique_count)

count_dict = {}

for i in words:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1
        
print(' '.join(map(str, count_dict.values())))



""" 
n = int(input())
words = [input() for _ in range(n)]

# ユニークな単語の数をカウント
unique_count = len(set(words))
print(unique_count)

count_dict = {}

for word in words:
    # 単語の出現回数を辞書に追加または更新
    count_dict[word] = count_dict.get(word, 0) + 1

# 単語とその出現回数を表示
for word, count in count_dict.items():
    print(f"{word}: {count}") """
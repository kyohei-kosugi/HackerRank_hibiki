""" from collections import defaultdict

n, m = map(int, input().split())

n_list = []
m_list = []

for _ in range(n):
    value_a = input()
    n_list.append(value_a)

for _ in range(m):
    value_b = input()
    m_list.append(value_b)

for i in range(len(m_list)):
    output_list = []
    for j in range(len(n_list)):
        if m_list[i] == n_list[j]:
            output_list.append(j + 1)
    if len(output_list) == 0:
        print('-1')
    else:
        print(' '.join(map(str, output_list))) """


""" n, m = map(int, input().split())

n_dict = {}  # 辞書を初期化 (キー: 要素, 値: インデックスのリスト)

for i in range(n):
    value_a = input()
    
    # 辞書に要素をキーとして追加し、インデックスを値としてリストに追加
    if value_a in n_dict:
        n_dict[value_a].append(i + 1)
    else:
        n_dict[value_a] = [i + 1]

for _ in range(m):
    value_b = input()
    
    # キーが存在する場合、対応するインデックスのリストを取得
    # 存在しない場合、空のリストを取得
    output_list = n_dict.get(value_b, [])
    
    if not output_list:
        print('-1')
    else:
        print(' '.join(map(str, output_list))) """


from collections import defaultdict
n, m = map(int, input().split(" "))
A = [input() for _ in range(n)]
B = [input() for _ in range(m)]

A_dd = defaultdict(list)
for i in range(len(A)):
    A_dd[A[i]].append(i+1)
for word in B:
    if len(A_dd[word])>0:
        print(" ".join(list(map(str,A_dd[word]))))
    else:
        print(-1)
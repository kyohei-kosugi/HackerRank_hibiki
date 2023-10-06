m = int(input())
m_list = set(map(int, input().split()))
n = int(input())
n_list = set(map(int, input().split()))

diff_m = m_list.difference(n_list)
diff_n = n_list.difference(m_list)

result = sorted(set(diff_m.union(diff_n)))

for i in range(len(result)):
    print(result[i])



""" symmetric method code
# mの要素数を取得
m = int(input())

# mの要素をリストとして取得
m_list = set(map(int, input().split()))

# nの要素数を取得
n = int(input())

# nの要素をリストとして取得
n_list = set(map(int, input().split()))

# 2つの差分を直接計算
result = sorted(m_list.symmetric_difference(n_list))

# 結果を出力
for item in result:
    print(item)
 """
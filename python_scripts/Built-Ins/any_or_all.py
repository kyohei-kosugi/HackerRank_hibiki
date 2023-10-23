n = int(input())
l = [x for x in map(int, input().split())]

def is_palindromic_integer(n):
    # 整数を文字列に変換
    str_n = str(n)
    
    # 文字列を逆さまにしたものを取得
    reversed_str_n = str_n[::-1]
    
    # 元の文字列と逆さまにした文字列が等しいかどうかを確認
    return str_n == reversed_str_n

if all(x > 0 for x in l) and any(is_palindromic_integer(x) for x in l):
    print('True')
else: 
    print('False')


""" 
n,it=int(input()),input()
print(True) if all([int(i)>0 for i in it.split(" ")]) and any([i==i[::-1] for i in it.split(" ")]) else print(False)
 """
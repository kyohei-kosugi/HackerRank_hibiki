# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    a = input().split()
    b = input().split()
    a_list = [int(x) for x in a]
    b_list = [int(x) for x in b]
    
    for i in range(len(a_list)):
        for j in range(len(b_list)):
            if i != len(a_list) - 1 or j != len(b_list) -1:
                print((a_list[i], b_list[j]), end=' ')
            else:
                print((a_list[i], b_list[j]))

""" Chat GPTで最適化
if __name__ == '__main__':
    # ユーザーからの入力を受け取り、スペースで分割して整数のリストに変換
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    # a_listとb_listの要素の組み合わせを出力する
    for a_item in a_list:
        for b_item in b_list:
            print((a_item, b_item), end=' ')
    print()  # 改行を追加して終了
 """
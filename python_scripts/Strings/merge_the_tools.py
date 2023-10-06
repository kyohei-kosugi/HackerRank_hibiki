import textwrap
from collections import OrderedDict

def merge_the_tools(string, k):
    # your code goes here
    substring = textwrap.wrap(string, k)
    # 重複を削除する方法：https://qiita.com/ShinichiIt0/items/419af2f6342bd50923a8
    for sub in range(len(substring)):
        result = ''.join(OrderedDict.fromkeys(substring[sub]))
        print(result)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
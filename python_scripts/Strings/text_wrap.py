import textwrap

def wrap(string, max_width):
    w = textwrap.wrap(string, width=max_width)
    answer = '\n'.join(w)
    return answer

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
from html.parser import HTMLParser

n = int(input())

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for attr in attrs:
                print("->", attr[0], ">", attr[1])
    def handle_startendtag(self, tag, attrs):
        print(tag)
        if attrs:
            for attr in attrs:
                print("->", attr[0], ">", attr[1])


parser = MyHTMLParser()

for _ in range(n):
    html_code = input()
    parser.feed(html_code)
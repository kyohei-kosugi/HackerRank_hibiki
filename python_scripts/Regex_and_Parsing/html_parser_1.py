from html.parser import HTMLParser

line = int(input())

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs:
            for attr in attrs:
                print("->", attr[0], ">", attr[1])
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if attrs:
            for attr in attrs:
                print("->", attr[0], ">", attr[1])

parser = MyHTMLParser()

for _ in range(line):
    html_code = input()
    parser.feed(html_code)
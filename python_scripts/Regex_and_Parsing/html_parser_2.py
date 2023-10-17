from html.parser import HTMLParser
import re

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        pattern = r"\n"
        match = re.search(pattern, data)
        if match:
            print(">>> Multi-line Comment")
            print(data)
        else:
            print(">>> Single-line Comment")
            print(data)
    
    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)
        else:
            pass
  
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

## print()
parser = MyHTMLParser()
parser.feed(html)
parser.close()
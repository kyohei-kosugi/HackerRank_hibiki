import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    count = 0
    for element in node.iter():
        if element.attrib:
            for attr in element.attrib:
                count += 1
    return count

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
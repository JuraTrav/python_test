import sys
import re
from module.XMLparser import create_xml_data, xml_difference
from module.parser import parser, remove_tags

if __name__ == "__main__":
    parse = parser()

    with open(sys.argv[1], 'r') as f:
        contents1 = f.read()
    with open(sys.argv[2], 'r') as f:
        contents2 = f.read()

    parse.feed(remove_tags(contents1))
    create_xml_data(parse.list1, "analyze1.xml")
    parse.list1 = list()
    parse.feed(remove_tags(contents2))
    create_xml_data(parse.list1, "analyze2.xml")
    result = xml_difference("analyze1.xml", "analyze2.xml")
    print result
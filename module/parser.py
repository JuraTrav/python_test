import re
from HTMLParser import HTMLParser

class parser(HTMLParser):

    obj = dict()
    list1 = list()

    def handle_starttag(self, start_tag, tag_attrs):
        tag = {"tag": start_tag, "attributes": tag_attrs}
        self.list1.append(tag)

def remove_tags(str):
    removed_tabs = remove_tabs(str)
    remove_starttag_body = removed_tabs.split("<body>")
    remove_endtag_body = remove_starttag_body[1].split("</body>")

    return remove_endtag_body[0]


def remove_tabs(str):
    clean = r'\s+'
    text = re.sub(clean, ' ', str)

    return text

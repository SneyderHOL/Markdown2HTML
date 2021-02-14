#!/usr/bin/python3
'''python script that checks for a Markdown file'''
import sys, re
from os import path

def matching(line, pattern):
    aux = "(0)+".replace("0", pattern)
    print(aux)
    matching = re.match(aux, line)
    if matching:
        print(str(matching.group()))
        return str(matching.group())
    return None

def heading_level(pattern, tags, line):
    level = str(len(pattern))
    op_tag = tags[0].replace("0", level)
    cl_tag = tags[1].replace("0", level)
    content = ""+ line.replace(pattern + " ", "")
    return op_tag + content + cl_tag + "\n"

def init_list(list_open, pattern):
    text = ""
    if list_open:
        text = pattern[0] + "\n"
    else:
        text = pattern[1] + "\n"
    return text

def add_list_item(list_item, line, pattern):
    text = line.replace("\n", "")
    text = text.replace(pattern + " ", "")
    text = list_item[0] + text + list_item[1] + "\n"
    print(text)
    return text

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit('Usage: ./markdown2html.py README.md README.html')
    filename_1 = sys.argv[1]
    filename_2 = sys.argv[2]
    patterns = {'#': ['<h0>', '</h0>'],
                '-': ['<ul>', '</ul>'],
                "\*": ['<ol>', '</ol>']}
    list_item = ['<li>', '</li>']
    # lists = {'-': 0, '*': 0}
    lists = {'-': False, "*": False}
    list_open = [False, '']
    if path.exists(filename_1):
        text = ''
        match = None
        with open(sys.argv[1]) as read_file:
            for line in read_file:
                for key, value in patterns.items():
                    match = matching(line, key)
                    if match is None:
                        continue
                    if match in lists:
                        if list_open[0] is False:
                            list_open[0] = True
                            list_open[1] = key
                            text += init_list(list_open[0], patterns[list_open[1]])
                        print('before_adding_item')
                        text += add_list_item(list_item, line, match)
                        break
                    else:
                        if list_open[0]:
                            list_open[0] = False
                            text += init_list(list_open[0], patterns[list_open[1]])
                        text += heading_level(match, value, line.replace("\n", ""))
                        break
            else:
                if list_open[0]:
                    list_open[0] = False
                    text += init_list(list_open[0], patterns[list_open[1]])
        with open(sys.argv[2], 'w') as new_file:
            new_file.write(text)
        sys.exit(0)
    else:
        sys.exit('Missing ' + sys.argv[1])

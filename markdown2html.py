#!/usr/bin/python3
'''python script that checks for a Markdown file'''
import sys, re
from os import path

def matching(line, pattern):
    aux = "(0)+".replace("0", pattern)
    matching = re.match(aux, line)
    if matching:
        return str(matching.group())
    return None

def heading_level(pattern, tags, line):
    level = str(len(pattern))
    op_tag = tags[0].replace("0", level)
    cl_tag = tags[1].replace("0", level)
    content = ""+ line.replace(pattern + " ", "")
    return op_tag + content + cl_tag + "\n"

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit('Usage: ./markdown2html.py README.md README.html')
    filename_1 = sys.argv[1]
    filename_2 = sys.argv[2]
    patterns = {'#': ['<h0>', '</h0>']}
    if path.exists(filename_1):
        text = ''
        match = None
        with open(sys.argv[1]) as read_file:
            for line in read_file:
                for key, value in patterns.items():
                    print(key, value)
                    match = matching(line, key)
                    if match is None:
                        text += line
                        continue
                    print(match)
                    text += heading_level(match, value, line.replace("\n", ""))
        with open(sys.argv[2], 'w') as new_file:
            new_file.write(text)
        sys.exit(0)
    else:
        sys.exit('Missing ' + sys.argv[1])

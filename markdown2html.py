#!/usr/bin/python3
'''python script that checks for a Markdown file'''
import sys
from os import path

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit('Usage: ./markdown2html.py README.md README.html')
    if path.exists(sys.argv[1]):
        sys.exit(0)
    else:
        sys.exit('Missing ' + sys.argv[1])

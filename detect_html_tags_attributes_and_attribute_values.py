import re
import sys


N = int(input())
html = ""
# N seems to be wrong in some cases, so we use sys.stdin.
for line in sys.stdin:
    html += line

# Remove comments. Quantifier must be lazy to detect every comment.
# Flag necessary for multiline comment matches.
html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)

# Captures HTML tags. Needs to be * instead of + because
# [^/] is already matching 1 character.
tags = re.findall(r'<([^/][^>]*)>', html)
for tag in tags:
    # If tag has space in it, it means that it has attributes.
    if " " in tag:
        # Captures the name of this tag.
        tag_name = re.match(r'[\w-]+', tag)
        print(tag_name.group(0))
        
        # Captures every attribute in an HTML tag and its value.
        attributes = re.findall(r'([\w-]+)="([^"]+)', tag)
        for attr in attributes:
            print("->", attr[0], ">", attr[1])
    else:
        print(tag)

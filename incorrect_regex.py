import re


T = int(input())
for _ in range(T):
    regex_line = input()
    try:
        re.compile(regex_line)
    except re.error:
        print(False)
    else:
        print(True)

import re


S = input()
k = input()
regex_obj = re.compile(k)

match = regex_obj.search(S)
if match is None:
    print((-1, -1))
else:
    while match:
        print((match.start(), match.end() - 1))
        match = regex_obj.search(S, match.start() + 1)

import re


for _ in range(int(input())):
    N = input()
    if not re.match(r"^[+-]?\d*\.\d+$", N):
        print(False)
    else:
        print(True)

import re


regex = "[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})"
N = int(input())
for _ in range(N):
    current_line = input()
    for hexa in re.findall(regex, current_line, re.I):
        print(hexa)

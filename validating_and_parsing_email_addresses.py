import re


n = int(input())

for _ in range(n):
    current_user = input().split()
    if re.match(r"<[a-zA-Z](\w|\.|-)*@[a-zA-Z]+\.[a-zA-Z]{1,3}>", current_user[1]):
        print(*current_user)

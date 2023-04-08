import re


N = int(input())
for _ in range(N):
    edited_code = re.sub(r"(?<= )&&(?= )", "and", input())
    print(re.sub(r"(?<= )\|\|(?= )", "or", edited_code))

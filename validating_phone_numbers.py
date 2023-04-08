import re


N = int(input())
for _ in range(N):
    phone_number = input()
    match = re.match(r"^[789]\d{9}$", phone_number)
    if match:
        print("YES")
    else:
        print("NO")

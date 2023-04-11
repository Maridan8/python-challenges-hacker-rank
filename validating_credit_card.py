import re


N = int(input())
for _ in range(N):
    number = input()
    if (
        # Checks overall structure.
        re.match(r"[456][0-9]{3}(-?[0-9]{4}){3}$", number)
        and
        # Checks for 4 or more consecutive repeated digits.
        not re.search(r"(.)\1{3}", number.replace("-", ""))
    ):
        print("Valid")
    else:
        print("Invalid")

import re


regex_2_uppercase = r"([A-Z].*){2}"
regex_3_digits = r"([0-9].*){3}"
regex_repeat = r"(.).*\1"
# Next regex checks for both rule 3 and 5.
regex_10_alphanum = r"[a-zA-Z0-9]{10}"

T = int(input())
for _ in range(T):
    uid = input()
    if (
        re.search(regex_2_uppercase, uid)
        and re.search(regex_3_digits, uid)
        and re.search(regex_10_alphanum, uid)
        and not re.search(regex_repeat, uid)
    ):
        print("Valid")
    else:
        print("Invalid")

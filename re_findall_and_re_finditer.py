import re


vowels = "[aeiou]"
consonants = "[qwrtypsdfghjklzxcvbnm]"
regex = r"(?<=" + consonants + ")(" + vowels + "{2,})" + consonants

matches = re.findall(regex, input(), flags=re.I)
if matches == []:
    print(-1)
else:
    print(*matches, sep="\n")

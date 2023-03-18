thousands = "M{0,3}"
hundreds = "(CM|CD|D?C{0,3})"
tens = "(XC|XL|L?X{0,3})"
units = "(IX|IV|V?I{0,3})"

regex_pattern = r"" + thousands + hundreds + tens + units + "$"

import re
print(str(bool(re.match(regex_pattern, input()))))
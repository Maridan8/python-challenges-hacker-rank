#!/bin/python3

import re


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

script = ""
for column in zip(*matrix):
    script += "".join(column)

print(re.sub(r"([a-zA-Z0-9])[\s!@#$%&]+([a-zA-Z0-9])", r"\1 \2", script))

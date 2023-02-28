from itertools import groupby


S = input()
print(*[f"({len(list(g))}, {k})" for k, g in groupby(S)])

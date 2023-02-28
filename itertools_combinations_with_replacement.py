from itertools import combinations_with_replacement


S, k = input().split()
k = int(k)

new_S = ["".join(s) for s in combinations_with_replacement(sorted(S), k)]
print(*new_S, sep="\n")

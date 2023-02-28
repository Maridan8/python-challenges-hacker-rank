from itertools import permutations

S, k = input().split()
k = int(k)

S = permutations(sorted(S), k)
new_S = ["".join(s) for s in S]
print(*new_S, sep="\n")

from itertools import combinations


S, k = input().split()
k = int(k)
sorted_S = sorted(S)

for i in range(1, k + 1):
    new_S = ["".join(s) for s in combinations(sorted_S, i)]
    print(*new_S, sep="\n")

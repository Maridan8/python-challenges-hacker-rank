from collections import defaultdict


def_dict = defaultdict(list)

N, M = map(int, input().split())
for i in range(N):
    def_dict[input()].append(i + 1)

for i in range(M):
    elem = input()
    # If element exists in dictionary, print all its indexes.
    if def_dict[elem]:
        print(*def_dict[elem])
    else:
        print(-1)

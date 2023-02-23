m = int(input())
a = map(int, input().split())
n = int(input())
b = map(int, input().split())

set_a = set(a)
set_b = set(b)

symmetric_difference = set_a.difference(set_b).union(set_b.difference(set_a))

print(*sorted(symmetric_difference), sep="\n")

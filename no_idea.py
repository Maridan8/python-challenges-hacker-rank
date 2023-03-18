n, m = input().split()
array = input().split()
A = set(input().split())
B = set(input().split())

happiness = 0
for elem in array:
    if elem in A:
        happiness += 1
    elif elem in B:
        happiness -= 1

print(happiness)

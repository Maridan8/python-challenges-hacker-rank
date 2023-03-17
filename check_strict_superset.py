A = set(input().split())
N = int(input())

for _ in range(N):
    current_other_set = set(input().split())
    if not A.issuperset(current_other_set):
        print(False)
        exit()
print(True)

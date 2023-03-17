T = int(input())

for _ in range(T):
    A_size = input()
    A = set(input().split())
    B_size = input()
    B = set(input().split())

    print(A.issubset(B))

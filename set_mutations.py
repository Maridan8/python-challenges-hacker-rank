A_size = input()
A = set(map(int, input().split()))

N = int(input())
for _ in range(N):
    command = input().split()
    other_set = set(map(int, input().split()))
    getattr(A, command[0])(other_set)

print(sum(A))

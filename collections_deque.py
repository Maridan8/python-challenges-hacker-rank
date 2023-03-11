from collections import deque


N = int(input())

d = deque()
for _ in range(N):
    command = input().split()
    if command[0] == "append":
        d.append(int(command[1]))
    elif command[0] == "appendleft":
        d.appendleft(int(command[1]))
    elif command[0] == "pop":
        d.pop()
    else:
        d.popleft()

print(*d)

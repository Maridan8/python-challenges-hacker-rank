from collections import deque


T = int(input())
for _ in range(T):
    input()
    blocks = deque(map(int, input().split()))
    possible = "Yes"

    curr = blocks.popleft() if blocks[0] > blocks[-1] else blocks.pop()
    while blocks:
        if blocks[0] <= curr and blocks[0] >= blocks[-1]:
            curr = blocks.popleft()
        elif blocks[-1] <= curr and blocks[-1] >= blocks[0]:
            curr = blocks.pop()
        else:
            possible = "No"
            break
    print(possible)

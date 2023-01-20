# As of 2023/01/16, the Python 3 interpreter in HackerRank is broken
# for this challenge. Pypy 3 should be used.

n = int(input())

if n == 0:
    return

hashed_value = hash(tuple(map(int, input().split())))
print(hashed_value)

from collections import Counter


X = int(input())
shoes = map(int, input().split())
counting = Counter(shoes)

money_earned = 0
N = int(input())
for i in range(N):
    desired_size, price = map(int, input().split())
    if counting[desired_size] > 0:
        money_earned += price
        counting[desired_size] -= 1

print(money_earned)

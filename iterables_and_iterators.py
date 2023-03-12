from itertools import combinations


N = int(input())
letters = input().split()
K = int(input())

letter_combinations = list(combinations(letters, K))
a_count = 0
for letter_comb in letter_combinations:
    if "a" in letter_comb:
        a_count += 1

print(a_count / len(letter_combinations))

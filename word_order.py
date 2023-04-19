from collections import Counter

words = [input() for _ in range(int(input()))]
# From Python 3.7 onwards, Counters remember order of insertion.
word_order_count = Counter(words)

print(len(word_order_count))
print(*word_order_count.values())

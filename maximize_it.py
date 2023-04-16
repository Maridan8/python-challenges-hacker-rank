from itertools import product


K, M = map(int, input().split())
lists = [list(map(int, input().split()[1:])) for _ in range(K)]

# itertools.product combines, as in a cartesian product, the elements
# of all the lists in lists. Each i is a possible combination.
possible_results = [sum(map(lambda n: n ** 2, i)) % M for i in product(*lists)]
print(max(possible_results))

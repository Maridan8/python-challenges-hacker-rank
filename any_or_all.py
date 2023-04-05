N = int(input())
array = input().split()

first_condition = all([int(n) > 0 for n in array])
second_condition = any([n == n[::-1] for n in array])

print(first_condition and second_condition)

n = input()
english_set = set(input().split())

b = input()
french_set = set(input().split())

print(len(english_set | french_set))

K = int(input())

tourists = input().split()
single = set()
group = set()
for tourist in tourists:
    if tourist not in single:
        single.add(tourist)
    else:
        group.add(tourist)
print(single.difference(group).pop())

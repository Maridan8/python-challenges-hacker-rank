from collections import OrderedDict


N = int(input())

ordered_dict = OrderedDict()
for _ in range(N):
    item_name, _, price = input().rpartition(" ")
    if item_name in ordered_dict.keys():
        ordered_dict[item_name] += int(price)
    else:
        ordered_dict[item_name] = int(price)

for key, value in ordered_dict.items():
    print(key, value)

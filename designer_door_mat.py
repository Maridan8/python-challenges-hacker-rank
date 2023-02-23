input_str = input().split()
n, m = int(input_str[0]), int(input_str[1])

lines = m
sep_count = 1
for i in range(n // 2):
    print(
        "-".rjust(lines // 2 - 1, "-")
        + ".|." * sep_count
        + "-".ljust(lines // 2 - 1, "-")
    )
    lines -= 6
    sep_count += 2

print("WELCOME".center(m, "-"))

for i in range(n // 2):
    lines += 6
    sep_count -= 2
    print(
        "-".rjust(lines // 2 - 1, "-")
        + ".|." * sep_count
        + "-".ljust(lines // 2 - 1, "-")
    )

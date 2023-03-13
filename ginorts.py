print(*(sorted(input(), key=lambda c: (c.isdigit(), c.isdigit() and int(c) % 2 == 0, c.isupper(), c))), sep="")

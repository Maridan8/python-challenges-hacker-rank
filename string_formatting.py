def print_formatted(number):
    pad = len(bin(number).lstrip("0b"))
    for i in range(1, number + 1):
        decimal = str(i).rjust(pad)
        octal = oct(i).lstrip("0o").rjust(pad)
        hexadecimal = hex(i).lstrip("0x").upper().rjust(pad)
        binary = bin(i).lstrip("0b").rjust(pad)

        print(" ".join([decimal, octal, hexadecimal, binary]))


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)

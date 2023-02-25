def print_rangoli(size):
    # Mid and upper part of the shape.
    for i in range(size):
        start_char = 96 + size - i
        line = ["-"] * (size * 4 - 3)

        # Mid until left extreme of the line.
        pos = len(line) // 2
        # Start printing few characters and increase.
        for j in range(start_char, start_char + i + 1, 1):
            line[pos] = chr(j)
            pos -= 2

        # Next of mid until right extreme of the line.
        pos = len(line) // 2 + 2
        for j in range(start_char + 1, start_char + i + 1, 1):
            line[pos] = chr(j)
            pos += 2

        print("".join(line))

    # Lower part of the shape.
    for i in range(1, size):
        start_char = 97 + i
        line = ["-"] * (size * 4 - 3)

        # Mid until left extreme of the line.
        pos = len(line) // 2
        # Start printing many characters and decrease.
        for j in range(start_char, start_char + size - i, 1):
            line[pos] = chr(j)
            pos -= 2

        # Next of mid until right extreme of the line.
        pos = len(line) // 2 + 2
        for j in range(start_char + 1, start_char + size - i, 1):
            line[pos] = chr(j)
            pos += 2

        print("".join(line))


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)

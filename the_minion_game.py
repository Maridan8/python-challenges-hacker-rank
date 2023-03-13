def minion_game(string):
    string_size = len(string)
    num_substrings = string_size * (string_size + 1) // 2

    kevin = 0
    for i in range(string_size):
        if string[i] in "AEIOU":
            kevin += string_size - i
    stuart = num_substrings - kevin

    if kevin > stuart:
        print("Kevin " + str(kevin))
    elif stuart > kevin:
        print("Stuart " + str(stuart))
    else:
        print("Draw")


if __name__ == "__main__":
    s = input()
    minion_game(s)

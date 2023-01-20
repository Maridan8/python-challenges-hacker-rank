def merge_the_tools(string, k):
    substring_size = len(string) / k

    t = []
    previous = 0
    for count in range(k, len(string) + 1, k):
        t.append(string[previous:count])
        previous = count

    for string in t:
        print("".join(sorted(set(string), key=string.index)))


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)

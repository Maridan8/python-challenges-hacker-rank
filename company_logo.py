#!/bin/python3

from collections import Counter


if __name__ == '__main__':
    s = input()
    s = sorted(s)
    [print(*letter) for letter in Counter(s).most_common(3)]

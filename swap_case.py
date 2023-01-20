def swap_case(s):
    new_s = [c.upper() if c.islower() else c.lower() for c in s]
    return "".join(new_s)


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)

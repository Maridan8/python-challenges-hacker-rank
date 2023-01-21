if __name__ == "__main__":
    s = input()

    flag = False
    for c in s:
        if c.isalnum():
            flag = True
            break
    print(flag)

    flag = False
    for c in s:
        if c.isalpha():
            flag = True
            break
    print(flag)

    flag = False
    for c in s:
        if c.isdigit():
            flag = True
            break
    print(flag)

    flag = False
    for c in s:
        if c.islower():
            flag = True
            break
    print(flag)

    flag = False
    for c in s:
        if c.isupper():
            flag = True
            break
    print(flag)

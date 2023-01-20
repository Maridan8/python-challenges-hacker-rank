cube = lambda x: x * x * x


def fibonacci(n):
    fibo_list = [0, 1]

    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]

    for i in range(1, n - 1):
        fibo_list.append(fibo_list[i - 1] + fibo_list[i])
    print(fibo_list)
    return fibo_list


if __name__ == "__main__":
    n = int(input())
    print(list(map(cube, fibonacci(n))))

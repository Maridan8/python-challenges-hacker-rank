if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    inter_list = [
        [i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)
    ]

    final_list = [i for i in inter_list if sum(i) != n]

    print(final_list)

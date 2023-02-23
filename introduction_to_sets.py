def average(array):
    distinct_elements = set(array)
    return sum(distinct_elements) / len(distinct_elements)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

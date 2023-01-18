if __name__ == "__main__":
    lowest_score = 101
    second_lowest_score = 101
    lowest_score_id = -1
    second_lowest_score_id = -1
    records = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        records.append([name, score])

        if score < lowest_score:
            second_lowest_score = lowest_score
            lowest_score = score
        if score < second_lowest_score and score > lowest_score:
            second_lowest_score = score

    names = []
    for record in records:
        if record[1] == second_lowest_score:
            names.append(record[0])

    names.sort()
    for name in names:
        print(name)

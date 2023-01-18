if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())

    champion_score = -101
    runner_up_score = -101
    for i in arr:
        if i > champion_score:
            runner_up_score = champion_score
            champion_score = i
        if i > runner_up_score and i < champion_score:
            runner_up_score = i

    print(runner_up_score)

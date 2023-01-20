if __name__ == "__main__":
    N = int(input())
    operable_list = []

    for i in range(N):
        command = input().split()

        if command[0] == "insert":
            operable_list.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(operable_list)
        elif command[0] == "remove":
            operable_list.remove(int(command[1]))
        elif command[0] == "append":
            operable_list.append(int(command[1]))
        elif command[0] == "sort":
            operable_list.sort()
        elif command[0] == "pop":
            operable_list.pop()
        else:
            operable_list.reverse()

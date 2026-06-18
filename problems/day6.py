if __name__ == '__main__':
    N = int(input())
    myList = []
    for i in range(N):
        commands =  input()
        command= commands.split(" ")[0].lower()
        if command == "insert":
            myList.insert(int(commands.split(" ")[1]),int(commands.split(" ")[2]))
        elif command == "append":
            myList.append(int(commands.split(" ")[1]))
        elif command == "remove":
            myList.remove(int(commands.split(" ")[1]))
        elif command == "pop":
            myList.pop()
        elif command == "sort":
            myList.sort()
        elif command == "reverse":
            myList.reverse()
        elif command == "print":
            print(myList)
        else:
            print("Invalid Command")
        
        
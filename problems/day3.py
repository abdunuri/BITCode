if __name__ == '__main__':
    n = int(input().strip())
    if(n % 2 != 0):
        print("Weird")
    elif(n%2==0):
        if(5>=n>=2):
            print("Not Weird")
        elif(20>=n>=6):
            print("Weird")
        elif(n>20):
            print("Not Weird")
        
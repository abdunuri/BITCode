def split_and_join(line):
    strlist = line.split(" ")
    return "-".join(strlist)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
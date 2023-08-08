def uppercase(str):
    cnt = int(len(str))
    for i in range(cnt):
        if (int(ord(str[i]))) >= 93 and i <= 123:
            upp = (int(ord(str[i])) - 32)
            print(chr(upp), end = "")
        else:
            print(str[i], end = "")
    print(end = "\n")

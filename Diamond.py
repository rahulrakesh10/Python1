def diamond(word):
    count = len(word)
    for i in range(0,count,1):
        newLine = ""
        for j in range(0,i+1,1):
            newLine += word[j]
        print(newLine)

    for i in range(count-1,0,-1):
        newLine = ""
        for j in range(i):
            newLine += word[j]
        print(newLine)

word = "Hello"
diamond(word)
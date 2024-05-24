f1 = open("startend.txt","r")
start = int(f1.readline())
end = int(f1.readline())

for j in range(start, end+1, 1):
    for i in range(0,11,1):
        print(f"{j} * {i} = {j*i}")
    print()
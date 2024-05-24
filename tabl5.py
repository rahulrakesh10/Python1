f1 = open("in.txt","r")
f2 = open("out.txt","w")
list1 = f1.readline().split(",")
start = int(list1[0])
end = int(list1[1])

for j in range(start, end+1, 1):
    for i in range(0,11,1):
        f2.write(f"{j} * {i} = {j*i}\n")
    f2.write("\n")
f2.close()
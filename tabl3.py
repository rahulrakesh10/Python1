start = int(input("Enter start number: "))
end = int(input("Enter ending number: "))

for j in range(start, end+1, 1):
    for i in range(0,11,1):
        print(f"{j} * {i} = {j*i}")
    print()
f1=open("convert.txt","r")
for i in range(0,4,1):
    str1=f1.readline().replace("\n","")
    list1=str1.split(" ")
    lhs_value=float(list1[0])
    lhs_units=list1[1]
    equals=list1[2]
    rhs_value=float(list1[3])
    rhs_units=list1[4]
    line1="1 "+lhs_units+" "+equals+" "+str(round((rhs_value/lhs_value),4))+" "+rhs_units
    line2="1 "+rhs_units+" "+equals+" "+str(round((lhs_value/rhs_value),4))+" "+lhs_units
    print(line1)
    print(line2)
    print()

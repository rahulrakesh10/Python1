def convert1(file1):
    f1 = open(file1,'r')
    result = ""
    for i in range(0,3,1):
        str1 = ""
        str2 = ""
        info1 = f1.readline().replace("\n","")
        list1 = info1.split(" ")
        lhs_value = float(list1[0])
        lhs_units = list1[1]
        rhs_value = float(list1[3])
        rhs_units = list1[4]
        str1 = str(1)+" "+lhs_units+" = "+str(rhs_value/lhs_value)+" "+rhs_units
        str2 = str(1)+" "+rhs_units+" = "+str(lhs_value/rhs_value)+" "+lhs_units
        result += (str1 + "\n" + str2 +"\n"+"\n")
    return result

print(convert1('convert.txt'))
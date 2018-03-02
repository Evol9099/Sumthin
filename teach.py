file = open("..//teachers.txt","r")
teachers = []
x = 0
for line in file.readlines():
    newarr = [""]
    
    for letter in line.strip("\n"):
        if letter == ",":
            x += 1
            newarr.append("")

        else:
            newarr[x] += letter
    teachers.append(newarr)
    x = 0
file.close()
print(teachers)

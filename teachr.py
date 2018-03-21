file = open("..//teachers.txt","r")
file1 = open("..//teachers2.txt","w")
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
#print(teachers)
def save():
    for y in range (0,8):
        for x in range (0,6):
            file1.write(teachers[y][x])
            if x == 6:
                file1.write("\n")
            else:
                file1.write(",")
#    file1.write(teachers[y][5]+"\n")

def prfield():
    field = input("What field m8? ")
    if field == "tname":
        for x in range (1,8):
            print(teachers[x][0])
    elif field == "tnamewallergy":
        for x in range (1,8):
            if teachers[x][5] != "":
                print(teachers[x][0])
    elif field == "nofav":
        for x in range (1,8):
            if teachers[x][6] == "":
                print(teachers[x][0])
                fav = input("input fav studerino: ")



#prfield()
save()

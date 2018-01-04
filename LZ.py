file = open("..\\..\\random text 2.txt","r")
list = file.read().split(" ")
dict = {"1":"1"}

print(list)
print(dict["1"])
'''for n in range (0,len(list)):
    dict[list[n]]=n
    for n1 in range (0,len(dict)):
        n1 += 1
        if dict[n1] == dict[n]:
            dict[n1] = dict[list[n]]'''

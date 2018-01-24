file = open("..\\..\\Random Text.txt","r")
text = file.read()
for letter in "abcdefghijklmnopqrstuvwxyz":
    print(letter+" : "+str(text.count(letter)))


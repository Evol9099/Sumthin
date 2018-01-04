file = open("..\\..\\Random Text.txt","r")
outfile = open("..\\..\\Compression.txt","r+")
outoutfile = open("..\\..\\Outcompression.txt","w")
text = file.read()
counta = 0
ctext = ""

while counta != len(text):
    countb = ""
    a = text[counta:counta+1]
    counta += 1
    if a == text[counta:counta+1]:
        countb = 1
        while a == text[counta:counta+1]:
            countb += 1
            counta += 1
    ctext += str(countb)+a
outfile.write(ctext)

'''countc = 0
cpdtext = outfile.read()
print(cpdtext)
while countc != len(cpdtext):
    time = ""
    for n in range (1,10):
        if cpdtext[countc:countc+1] == n:
            time = str(n)
            countc += 1
            for n in range (1,10):
                if cpdtext[countc:countc+1] == n:
                    countc += 1
                    time += str(n)
                    break
    print(time+cpdtext[countc:countc+1])
    #outoutfile.writelines(time+cpdtext[countc:countc+1].strip("\n"))
    countc += 1'''

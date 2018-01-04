outfile = open("..\\..\\Compression.txt","r")
outoutfile = open("..\\..\\Outcompression.txt","w")


countc = 0
cpdtext = outfile.read()
#print(cpdtext)
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
    #print(time+cpdtext[countc:countc+1])
    outoutfile.writelines(time+cpdtext[countc:countc+1].strip("\n"))
    countc += 1

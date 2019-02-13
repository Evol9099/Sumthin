lines = {"something","is","not","okay"}


#hash:
max = (2**256)-1
maxlen = 256
chunks = [""]
ccount = 0

#chunk generation:
for line in lines:
    charvalue = ""

    '''for i in range (len(line)): #calculate charvalue
        if i%2 == 0:
            linevalue += bin(17*(ord(line[i])))[2:]
        else:
            linevalue += bin(9*ord(line[i]))[2:]'''
    #calculate character ASCII value
    for i in range (len(line)):
        if i%2 == 0:
            charvalue += bin(3*(ord(line[i])))[2:]
        else:
            charvalue += bin(ord(line[i]))[2:]

        #chunking:
        space = 256-len(chunks[ccount])
        if space >= len(charvalue):
            chunks[ccount] += charvalue
        else:
            chunks[ccount] += charvalue[:space]
            ccount += 1
            chunks.append(charvalue[space:])
print(chunks)
#padding last chunk
lchunk = bin(int(chunks[ccount]))[2:]
lchunklen = len(lchunk)

if lchunklen < 256:
    lchunk += "1"
    space = 256-(lchunklen+1)
    if space > 64:
        lchunk += "0"*(space-64)
        space = 64
    lchunk += lchunk[:space-1]
chunks[ccount] = lchunk
print(chunks)
#actually hashing now:
def ezhash(chunk):
    chunk1 = chunk[0:128]
    chunk2 = chunk[128:]

    #split chunk1 into 16 pieces
    pieces1 = []
    for i in range (16):
        pieces1.append("")
        pieces1[i] += chunk1[i*8:(i*8)+7]

    #split chunk2 into 4 piece: (so that maybe in the future further scrambling can be done)
    pieces2 = []
    for i in range (4):
        pieces2[i] = chunk2[i*32:(i*32)+32]

    # 1 16-bit piece will bit-flip chunk1;
    count = 0
    for bit2 in pieces2[0][0:16]:
        if bit2 == "1":
            for i in range(16):
                if pieces1[count][i] == "0":
                    pieces1[count][i] = "1"
                else:
                    pieces1[count][i] = "0"
        count += 1

    # 1 8-bit piece will swap 1-16,2-15,...;
    count = 0
    for bit2 in pieces2[1][0:8]:
        if bit2 == "1":
            temp = pieces1[-(1+count)]
            pieces1[-(1+count)] = pieces1[count]
            pieces1[count] = temp
        count += 1

    # 1 8-bit piece will order 1-2,3-4,... in ascending/descending order;
    count = 0
    for bit2 in pieces2[3][0:8]:
        if pieces1[count][0] > pieces1[count+1][0]:
            if bit2 == "1": #ascending
                temp = pieces1[count+1]
                pieces1[count+1] = pieces1[count]
                pieces1[count] = temp

        else:
            if bit2 == "0": #descending
                temp = pieces1[count+1]
                pieces1[count+1] = pieces1[count]
                pieces1[count] = temp
        count += 2

        '''for i in range (3):
            if pieces1[count][i] < pieces1[count+1][i]:
                flag = True
            else:
                flag = False
            elif pieces1[count][i] > pieces1[count+1][i]:

            if bit2 == "1":
                if flag == True: #ascending
                    break
                else:
                    temp = pieces1[count+1]
                    pieces1[count+1] = pieces1[count]
                    pieces1[count] = temp
                    break 
            else:
                if flag == False:
                    
            
                




            if pieces1[count][i] < pieces1[count+1][i]:
                if bit2 == "1": #ascending
                    break
            elif pieces1[count][i] > pieces1[count+1][i]:
                if bit2 == "0":#descending

        count += 2'''

    # 16 2-bit piece will be added onto all pieces;
    '''for bit in chunk1:
        if bit == "0":'''

    #reconstruct hash
    hash = ""
    for i in range (16):
        hash += pieces1[i]
    return hash

#hash all chunks:
print(chunks)
hash1 = ezhash(chunks[0])
for i0 in range (1,len(chunks)):
    hash2 = ezhash(chunks[i0])
    cbdchunk = hash1 + hash2
    hash1 = ezhash(cbdchunk)
finalhash = hash1

#output:
outfile = open("hash output.txt","w")
outfile.write(finalhash)

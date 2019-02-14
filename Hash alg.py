lines = {"is","not","okay","yeet","why","am","I","here","hello","bye","something","nothing"}


#hash:
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
print("initial chunks:",chunks)

#padding last chunk
'''lchunk = bin(int(chunks[ccount]))[2:]'''
lchunk = chunks[ccount]
lchunklen = len(lchunk)
print("last chunk:",lchunk,lchunklen)

if lchunklen < 256:
    lchunk += "1"
    space = 256-(lchunklen+1)
    if space > 64:
        lchunk += "0"*(space-64)
        space = 64
    lchunk += lchunk[:space]
chunks[ccount] = lchunk

print("initial chunks:",chunks) #correct

#actually hashing now:
def ezhash(chunk):
    chunk1 = chunk[:128]
    chunk2 = chunk[128:]

    #split chunk1 into 16 pieces
    pieces1 = []
    for i in range (16):
        pieces1.append("")
        pieces1[i] += chunk1[i*8:(i*8)+8]

    #split chunk2 into 4 piece: (so that maybe in the future further scrambling can be done)
    pieces2 = []
    for i in range (4):
        pieces2.append("")
        pieces2[i] = chunk2[i*32:(i*32)+32]

    # 1: 16-bit piece will bit-flip chunk1;
    count = 0
    for bit2 in pieces2[0][:16]:
        npiece1 = ""
        if bit2 == "1":
            for i in range(8):
                if pieces1[count][i] == "0":
                    npiece1 += "1"
                else:
                    npiece1 += "0"
            pieces1[count] = npiece1
        count += 1

    # 2: 8-bit piece will swap 1-16,2-15,...;
    count = 0
    for bit2 in pieces2[1][0:8]:
        if bit2 == "1":
            temp = pieces1[-(1+count)]
            pieces1[-(1+count)] = pieces1[count]
            pieces1[count] = temp
        count += 1

    # 3: 8-bit piece will order 1-2,3-4,... in ascending/descending order;
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

    # 4: 16 2-bit piece will be added onto all pieces; (Requires Binary Addition)
    '''for bit1 in chunk1:
        if bit1 == "0":'''

    #reconstruct hash
    hash = ""
    for i in range (16):
        hash += pieces1[i]
    print("hash:",hash)
    return hash

#hash all chunks:
print("final:",chunks)
hash1 = ezhash(chunks[0])
for i0 in range (1,len(chunks)):
    hash2 = ezhash(chunks[i0])
    cbdchunk = hash1 + hash2
    hash1 = ezhash(cbdchunk)

#expand final hash into 512 bits
finalhash = hash1*4

#convert to hex
letter = ["A","B","C","D","E","F"]
finalhex = ""

for i0 in range (128):

    fourbin = finalhash[i0*4:(i0*4)+4]

    value = 0
    for i1 in range (4):
        value += int(fourbin[i1])*(2**(3-i1))
    if value > 9:
        value = letter[value-10]
    else:
        value = str(value)
    finalhex += value
print(finalhex)

#output:
outfile = open("hash output.txt","w")
outfile.write(finalhash)

hexchar = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
bin = input("binary: ")
den,hex = "",""

def binval ():
    if len(bin) != 8:
        print("error")
    else:
        for i in range(0,8):
            if int(bin[i]) > 1:
                print("error")

def binden (bin,den):
    for i in range (0,len(bin)):
        den += int(bin[-(i+1)])*(2**i)
    print(den)

def binhex ():
    length = len(bin)
    while length > 3:
        forbin = bin[length-4:length]
        binden (forbin,den)
        if int(den) < 10:
            hexdig = den
        else:
            hexdig = hexchar[den]
        hex = hexdig + hex
        len -= 4

binval()
binhex()
print(hex)


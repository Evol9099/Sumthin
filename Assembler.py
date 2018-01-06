from DenaryConverter import dtb
opcode = {"LDM":"0001","LDD":"0010","LDI":"0011","LDX":"0100","LDR":"0101",
          "STO":"0110","ADD":"1000","INC":"1001","DEC":"1010","JMP":"1011",
          "CMP":"1100","JPE":"1101","JPN":"1110","END":"00000000"}
symbol = {}
Acc = 0
file = open("Assembly Test.txt","r")
outfile = open("Assembly Macode.txt","w")
out = ""
line = file.readline().strip("\n")
countb = 0

while line != "END":
    counta = -1
    if line[0] == "(":
        for letter in line:
            counta += 1
            if letter == ")":
                symbol[line[1:counta]] = countb
    countb += 1
    line = file.readline().strip("\n")
print(symbol)

def output(out):
    print(str(out)+oprand)
    '''out = out+oprand
    outfile.writelines(out+"\n")'''

comp = ""
file.seek(0)
line = file.readline().strip("\n")


while line != "END":
    counta = 0
    countb = 0
    if line[0] == "(":
        counta += 1
        for letter in line:
            if letter != ")":
                counta += 1
            else: break
        out = opcode[line[counta:counta+3]]
    else: out = opcode[line[0:3]]

    if line[counta+4] == "(":
        out += "1100"
        for letter in line[4:]:
            if letter != ")":
                countb += 1
        oprand = dtb(int(symbol[line[5:countb+4]]))

    elif line[counta+4:] == "ACC":
        out += "1000"
        oprand = "00000000"

    elif line[counta+4] == "#":
        out += "0000"
        oprand = dtb(int(line[counta+5:]))

    else:
        out += "0100"
        oprand = dtb(int(line[counta+4:]))

    output(out)
    line = file.readline().strip("\n")

file.close()
outfile.close()

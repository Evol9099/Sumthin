from DenaryConverter import dtb
opcode = {"LDM":"00010000","CMP":"00100000","JPN":"00110000","INC":"01000000","JMP":"01010000",
          "END":"00000000","LDD":"01100000"}
Acc = 0
symbol = {}
file = open("..\\..\\Assembly Test.txt","r")
outfile = open("..\\..\\Assembly Macode.txt","w")
line = file.readline().strip("\n")
memo = "notoperand"
out = ""

def output(out):
    print(out+oprand)
    '''out = out+oprand
    outfile.writelines(out+"\n")'''

while line != "":
    out =opcode[line[0:3]]
    if line[4:] == "ACC":
        oprand = "00000000"
    else:
        oprand = dtb(int(line[5:]))
    if line[4] == "#":
        break

    output(out)

    line = file.readline().strip("\n")
a = 0

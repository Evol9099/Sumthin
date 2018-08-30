def dentobin (den):

    bin = ""

    while den > 0:
        string = str(den % 2)
        bin = string+bin
        den = den // 2
    while len(bin) < 8:
        bin = "0" + bin
    return(bin)

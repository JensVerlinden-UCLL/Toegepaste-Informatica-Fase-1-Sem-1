def hex(hexdecnum):
    binnum = ""
    hexlen = len(hexdecnum)
    i = 0
    while i<hexlen:
        if hexdecnum[i] == '0':
            binnum = binnum + "0000"
        elif hexdecnum[i] == '1':
            binnum = binnum + "0001"
        elif hexdecnum[i] == '2':
            binnum = binnum + "0010"
        elif hexdecnum[i] == '3':
            binnum = binnum + "0011"
        elif hexdecnum[i] == '4':
            binnum = binnum + "0100"
        elif hexdecnum[i] == '5':
            binnum = binnum + "0101"
        elif hexdecnum[i] == '6':
            binnum = binnum + "0110"
        elif hexdecnum[i] == '7':
            binnum = binnum + "0111"
        elif hexdecnum[i] == '8':
            binnum = binnum + "1000"
        elif hexdecnum[i] == '9':
            binnum = binnum + "1001"
        elif hexdecnum[i] == 'a' or hexdecnum[i] == 'A':
            binnum = binnum + "1010"
        elif hexdecnum[i] == 'b' or hexdecnum[i] == 'B':
            binnum = binnum + "1011"
        elif hexdecnum[i] == 'c' or hexdecnum[i] == 'C':
            binnum = binnum + "1100"
        elif hexdecnum[i] == 'd' or hexdecnum[i] == 'D':
            binnum = binnum + "1101"
        elif hexdecnum[i] == 'e' or hexdecnum[i] == 'E':
            binnum = binnum + "1110"
        elif hexdecnum[i] == 'f' or hexdecnum[i] == 'F':
            binnum = binnum + "1111"
        i = i+1
    return binnum

def float_bin(my_number, places = 3):
    my_whole, my_dec = str(my_number).split(".")
    my_whole = int(my_whole)
    res = (str(bin(my_whole))+".").replace('0b','')
 
    for x in range(places):
        my_dec = str('0.')+str(my_dec)
        temp = '%1.20f' %(float(my_dec)*2)
        my_whole, my_dec = temp.split(".")
        res += my_whole
    return res
 
 
 
def IEEE754(n, hex = False) :
    # identifying whether the number
    # is positive or negative
    sign = 0
    if n < 0 :
        sign = 1
        n = n * (-1)
    p = 30
    # convert float to binary
    dec = float_bin (n, places = p)
 
    dotPlace = dec.find('.')
    onePlace = dec.find('1')
    # finding the mantissa
    if onePlace > dotPlace:
        dec = dec.replace(".","")
        onePlace -= 1
        dotPlace -= 1
    elif onePlace < dotPlace:
        dec = dec.replace(".","")
        dotPlace -= 1
    mantissa = dec[onePlace+1:]
 
    # calculating the exponent(E)
    exponent = dotPlace - onePlace
    exponent_bits = exponent + 127
 
    # converting the exponent from
    # decimal to binary
    exponent_bits = bin(exponent_bits).replace("0b",'')
 
    mantissa = mantissa[0:23]
 
    # the IEEE754 notation in binary    
    final = str(sign) + exponent_bits.zfill(8) + mantissa
 
    # convert the binary to hexadecimal
    hstr = '%0*X' %((len(final) + 3) // 4, int(final, 2))

    if hex:
        return hstr
    return final

def ieee745(N): # ieee-745 bits (max 32 bit)
    a = int(N[0])        # sign,     1 bit
    b = int(N[1:9],2)    # exponent, 8 bits
    c = int("1"+N[9:], 2)# fraction, len(N)-9 bits

    return (-1)**a * c /( 1<<( len(N)-9 - (b-127) ))

while True:
        vraag1 = input("1: DECIMAL TO IEEE_754 | 2: IEEE_754 TO DECIMAL | 0: STOP | --> ")

        if vraag1 == "0":
            break

        if vraag1 == "1":
            vraag2 =  input("1: BINARY OUTPUT | 2: HEXADECIMAL OUTPUT | --> ")

            if vraag2 == "1":
                print(IEEE754(float(input("FLOATING DECIMAL: "))))
            elif vraag2 == "2":
                print(IEEE754(float(input("FLOATING DECIMAL: ")), True))
            else:
                print("That wasn't a valid option! You have to start again now... :(") 

        elif vraag1 == "2":
            vraag2 = input("1: BINARY INPUT | 2: HEXADECIMAL INPUT | --> ")

            if vraag2 == "1":
                print(ieee745(input("IEE754 FLOATING IN BINARY: ")))
            elif vraag2 == "2":
                print(ieee745(hex(input("IEE754 FLOATING IN HEXADECIMAL: "))))
            else:
                print("That wasn't a valid option!  You have to start again now... :(") 
        else:
            print("That's not a valid option, please enter one of the given numbers!")


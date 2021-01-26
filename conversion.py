def decimal_to_binary(num):#conversion of decimal to binary code
    c=["0","0","0","0","0","0","0","0"]
    i = 7
    while (num>0):
        r=num%2
        c[i] =str(r)
        i=i-1
        num=int(num/2)
    return "".join(c)

def binary_to_decimal(num): #conversion of binary to decimal code
    total = 0
    i=0
    while(num>0):
        r=num%10
        total += r*(2**i)
        i=i+1
        num=int(num/10)
    return total


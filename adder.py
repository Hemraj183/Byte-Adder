from gates import * # importing module gates to adder
#num1 and num2 are 8 bit binary in string form
def binAdder(num1,num2):
    carry = 0
    result = ['0','0','0','0','0','0','0','0']
    for i in range(7,-1,-1):
        bit1 = int(num1[i])
        bit2 = int(num2[i])
        
        #for sum
        xor1 = xorGate(bit1,bit2)
        sum_ = xorGate(xor1,carry)

        #for carry
        and1 = andGate(bit1,bit2)
        and2 = andGate(xor1,carry)
        carry = orGate(and1,and2)
        
        result[i] = str(sum_)
    return "".join(result)




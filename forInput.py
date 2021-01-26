#validation of selsection of binary and decimal section.
def validation(num):
    if num == "":
        return [True, "**** Empty Field Found!! Number 1 and 2 are only allowed ****"]
    try:
        checkNum = int(num)
    except:
        return [True,"**** No special charcter are not allowed!! Number 1 and 2 are only allowed ****"]
    if int(num) < 0:
        return [True,"**** Negative values are not allowed!! Number 1 and 2 are only allowed ****"]
  
    
    for digit in num:
        if int(digit) not in [1,2]:
            return [True,"****You Give the wrong Input!!****  Things To be Remind!!! Number 1 and 2 only allowed!!!"]
    
    return [False]

def inputbin1(): #code to take first binary input
    flag = False

    while (not flag):
        binNo1 = input("Enter the first binary number having 0 and 1: ").strip()
        if(validation1(binNo1)[0]):
            print (validation1(binNo1) [1])
        else:
            print("**** Thank You for the correct input ****")
            return binNo1
            flag = True

def validation1(num): # validation of first binary input
    if num == "":
        return [True, "Empty Field Found!! please enter binary number"]
    try:
        checkNum = int(num)
    except:
        return [True,"**** No special charcter are not allowed!! please enter binary number ****"]
    if int(num) < 0:
        return [True,"**** Negative values are not allowed!! please enter binary number ****"]

    if int(num) > 11111111:
        return [True,"**** Sum can not be more than 255 you have enter 1 more than 8 time! please enter less than 256! ****"]
    
    
    for digit in num:
        if int(digit) not in [0,1]:
            return [True,"**** Binary values are only o and 1!! Other value not allowed ****"]
    return [False]

def inputbin2(): # code to take second binary input
    flag = False

    while (not flag):
        binNo2 = input("Enter the second binary number having 0 and 1: ").strip()
        if(validation2(binNo2)[0]):
            print (validation2(binNo2) [1])
        else:
            print("**** Thank You for the correct input *****")
            return binNo2
            flag = True

def validation2(num): # validation of second binary input
    if num == "":
        return [True, "**** Empty Field Found!! please enter binary number ****"]
    try:
        checkNum = int(num)
    except:
        return [True,"**** No special charcter are not allowed!! please enter binary number ****"]
    if int(num) < 0:
        return [True,"**** Negative values are not allowed!! please enter binary number ****"]

    if int(num) > 11111111:
        return [True,"**** Sum can not be more than 255 you have enter 1 more than 8 time! please enter less than 256! ****"]

    
    for digit in num:
        if int(digit) not in [0,1]:
            return [True,"**** Binary values are only o and 1!! Other value not allowed ****"]
    return [False]


def inputdec1(): #code to take first decimal input
    flag = False

    while (not flag):
        decNO1 = input("Enter the first decimal number: ").strip()
        if(validation3(decNO1)[0]):
            print (validation3(decNO1) [1])
        else:
            print("**** Thank You for the correct input ****")
            return decNO1
            flag = True

def validation3(num): # validation of first decimal input
    if num == "":
        return [True, "**** Empty Field Found!! please enter decimal number ****"]
    
    try:
        checkNum = int(num)
    except:
        return [True,"**** No special charcter are not allowed!! please enter decimal number ****"]
    if int(num) < 0:
        return [True,"**** Negative values are not allowed!! please enter decimal number ****"]
    if int(num) > 255:
        return [True,"**** Number must lies between 0 to 255!! *****"]
     
  
    return [False]

def inputdec2(): # code to take second decimal input
    flag = False

    while (not flag):
        decNO2 = input("Enter the second decimal number: ").strip()
        if(validation4(decNO2)[0]):
            print (validation4(decNO2) [1])
        else:
            print("**** Thank You for the correct input ******")
            return decNO2
            flag = True
        

    
def validation4(num): # validation of second decimal input

    if num == "":
        return [True, "**** Empty Field Found!! please enter decimal number *****"]
    try:
        checkNum = int(num)
    except:
        return [True,"**** No special charcter are not allowed!! please enter decimal number ****"]
    if int(num) < 0:
        return [True,"**** Negative values are not allowed!! please enter decimal number ****"]
    if int(num) > 255:
        return [True,"**** Number must lies between 0 to 255!! *****"]
    
    
    return [False]


print("")
print("****** WELCOME TO THE BYTE ADDER *******")
print("****** HEMARAJ DHAKAL ********")
print("****** ITAHARI INTERNATIONAL COLLEGE *******")
print("****** LONDON METROPOLITAN UNOVERSITY ******")
print("****** FUNDAMENTAL OF COMPUTING COURSEWORK ******")
print("")
      
#importing the module where diffrent exits.
from conversion import *
from adder import *
from forInput import *

def validation2(num1,num2):
    if num1+num2>255:
        return False
    else:
        return True
def decSelect():
    x = (int(inputdec1()))
    y = (int(inputdec2()))

    sum_=x+y
    if (sum_ >255):
        print("***** You have Given the second Correct But You have sucess the limit which is not more than 255 *****")
        print("***** Please Enter the number which sum is not above 255 *****")
        return decSelect()         
        
    

    a=str(decimal_to_binary(x))#making the given input string.
    b=str(decimal_to_binary(y)) 
      
    
    print("")
    print("******* First Given Value *******")
    print("Decimal Number Given is: ",x)
    print("After changing decimal to binary is",decimal_to_binary(x))
    print("")
    print("******** Second Given Value ******")
    print("Decimal Number Given is: ",y)
    print("After changing decimal to binary is",decimal_to_binary(y))
    print("")
    print("********* Byte Adder *******")
    print(a)
    print(" " ,"+")
    print(b)
    print("")
    print(binAdder(a,b))#importing the module binadder from module adder.
    print("******** Overall result ********")
    print("X-----------X---------X---------X-------------X")
    print("")
    print("*** Decimal ***","     ","*** Binary ***")
    print("")
    print("     ", x ,"              ",a)
    print("     " ,y ,"              ",b)
    print("   ","------","            ","----------")
    print("     ",x+y,"              ", binAdder(a,b))
    print("")
    print("X-----------X---------X---------X---------------X")
    
def binSelect():
    
    m = inputbin1()
    n = inputbin2()
    
    a=int(m)#making the given value integer.
    b=int(n)
    
    p=int(binary_to_decimal(a))
    q=int(binary_to_decimal(b))

    sum_=p+q
    if (sum_ >255):
        print("***** You have Given the second Correct But You have sucess the limit which is not more than 255 *****")
        print("***** Please Enter the number which sum is not above 255 *****")
        return binSelect()
    
    e=decimal_to_binary(p)
    f=decimal_to_binary(q)
    
    print("")
    print("******* First Given Value *******")
    print("Binary Number Given is: ",m)
    print("After changing binary to decimal is: ",p)
    print("")
    print("******** Second Given Value ******")
    print("Binary Number Given is: ",n)
    print("After changing binary to decimal is: ",q)
    print("")
    print("********* Byte Adder *******")
    print(e)
    print(" ","+")
    print(f)
    print("")
    print(binAdder(e,f))#importing the module binadder from module adder.
    print("")
    print("******** Overall result ********")
    print("X-----------X---------X---------X-------------X")
    print("")
    print("  ""*** Binary ***","     ","  ""*** Decimal ***")
    print("")
    print("     ",e ,"              ",p)
    print("     ",f ,"              ",q)
    print("   ","----------","       ","-----------")
    print("     ",binAdder(e,f), "              ",(p+q))
    print("")
    print("X-----------X---------X---------X---------------X")

def input_binary_decimal():
    flag = False

    while (not flag):
        number = input("Enter the number 1 for binary and 2 for decimal: ").strip()#taking user input to select binary/decimal.
        if(validation(number)[0]):
            print (validation(number) [1])
        else:            
            if (int(number)==1):
                print ("**** Thank you for choosing Binary ****")
                print("")
                binSelect()
            elif(int(number)==2):
                print ("**** Thank you for choosing Decimal ****")
                print("")
                decSelect()
            
            else:
                print("**** You are not allowed to enter 1 and 2 same time or same digit multiple times!!! ****")
                return input_binary_decimal()
            flag= True


input_binary_decimal()

#code to check Do you want to continue section.
flag = False
while(not flag):
    check=input("Do you want to continue? Press Y/y for yes and N/n for No: ").strip()
    print("")

    if check.upper()== "Y":
        input_binary_decimal() # calling the function
        
    elif check.upper()== "N":
        print(" **** Thank You For The Participation **** ")
        flag = True
    elif check !="Y":
        print(" **** Press Y/y for yes and N/n for No!!! Other not allowed!!! **** ")
    elif check !="N":
        print(" **** Press Y/y for yes and N/n for No!!! Other not allowed!!! ****")
    else:
        print(" **** Press Y/y for yes and N/n for No!!! Other not allowed!!! ****")
        




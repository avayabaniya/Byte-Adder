"""Module to take 2 binery value store them in list and
    display the output"""

def binaryValue():

    global lnum1,lnum2
    while True:
        try:
            num1 = int(input("Enter 1st binary number:"),2) #the value inputed should be in base 2
            bnum1=str(bin(num1))[2:].zfill(8) #removes '0b' which appears while using bin function with '0'
            
            num2 = int(input("Enter 2st binary number:"),2) #the value inputed should be in base 2
            bnum2=str(bin(num2))[2:].zfill(8) #removes '0b' which appears while using bin function with '0'

            if len(bnum1) > 8 or len(bnum2) > 8: #checks if the length of bnum1 or bnum2 is greater than 8
                print("\n")
                print(" Error \n Entered value out of range")
                print("\n")
                continue
        
        except ValueError: #displays the following message if error value. Returns the program flow to while True
            print("\n")
            print(" Error \n Please Enter again")
            print("\n")

        else:
            break
    
    lnum1=list(bnum1) #creates list of the value stored in bnum1
    lnum2=list(bnum2) #creates list of the value stored in bnum2

    c=0
    while c < 8:
        lnum1[c]=eval(lnum1[c]) #converts the value of the list from string to integer
        lnum2[c]=eval(lnum2[c]) #converts the value of the list from string to integer
        c=c+1
    print("\n")
    print("1st number = ",lnum1)
    print("2nd number = ",lnum2)

binaryValue()

        
            
        

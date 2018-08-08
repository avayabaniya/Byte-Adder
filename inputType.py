"""Module to check if the entered value will be in decimal or binary
    and call the necessary module until the user says yes"""

def inputType():
    
    import imp
    global counter
    again="y"
    a=0
    b=0
    c=0 
    while again == "y" or again == "Y": 
        counter=eval(input("Entered value will be in? \n 1. Binary \n 2. Integer\n"))

        if counter == 1:
            import binaryValue
            a=a+1
            if counter == 1 and a > 1: #condition to check if module binaryValue has already been imported or not
                imp.reload(binaryValue)
        elif counter == 2:
            import integerValue#condition to check if module integerValue has already been imported or not
            b=b+1
            if counter == 2 and b > 1:
                imp.reload(integerValue)
        else:
            print("\n")
            print(" Error \n Enter again \n")
            continue
        import mainOutput
        c=c+1
        if c > 1: #condition to check if module mainOutput has already been imported or not
            imp.reload(mainOutput)


        again=input("\n \n Do you want to enter another number?(y/n)")
        print("\n")

        
    print("***THANK YOU***")
        
inputType()

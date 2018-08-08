""" Module to call previous modules,
    performs binary adder calculation
    and prints the output"""

def mainOutput():
    
    import inputType
    from inputType import counter #imports variable counter from inputType

    if counter == 1:
        import binaryValue
        from binaryValue import lnum1,lnum2 #imports variable lnum1 and lnum2 from binaryValue
        
    elif counter == 2:
        import integerValue
        from integerValue import lnum1,lnum2 #imports variable lnum1 and lnum2 from integerValue
        

    c1=0
    carry=0 
    ans=[0,0,0,0,0,0,0,0] #creates list ans of length 8
    while c1 < 8:
        xorGate1=lnum1[7-c1] ^ lnum2[7-c1]
        andGate1=lnum1[7-c1] & lnum2[7-c1]
        
        andGate2=xorGate1 & carry
        
        xorGate2=xorGate1 ^ carry
        
        carry=andGate1 | andGate2
        
        ans[c1]=(xorGate2)
        c1=c1+1
        
    ans.reverse()    
    print ("\n \n Sum = ",(ans))
    
mainOutput()

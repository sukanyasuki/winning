def print_0(size):
    for i in range(size):
        for j in range(size):
            if  (((j==0 or i==0 or j==size-1) and (i!=0 and i!=size-1)) or ((i==0 or  i==size-1) and (j>0 and j<size-1))): 
                print("*",end="")

            else:
                print(" ",end="")
        print()

        
def print_1(size):
   for i in range(size):
        for j in range(size):
            if (j>=0 and j==size//2) : 
                print("*",end="")
            else:
                print(" ",end="")
        print()


    
def print_2(size):
    for i in range(size):
        for j in range(size):
            if  ((i==0 or i==size-1 or  i==size//2) or ((i>0 and i<size//2) and j==size-1) or ((i>size//2 or i==size-1) and j==0)):
                print("*",end="")

            else:
                print(" ",end="")
        print()
        
def print_3(size):
    for i in range(size):
        for j in range(size):
        
            if (i==0 or i==size-1 or i==size//2 or j==size-1):
                print("*",end="")

            else:
                print(" ",end="")
        print()


def print_4(size):
    for i in range(size):
        for j in range(size):
            if ((i==size//2 or j==size-1)or (j==0 and (i>=0 and i<size//2))):
                print("*",end="")

            else:
                print(" ",end="")
        print()

        
def print_5(size):
   for i in range(size):
        for j in range(size):
            if  ((i==0 or i==size-1 or  i==size//2) or ((i>0 and i<size//2) and j==0) or ((i>size//2 or i==size-1) and j==size-1)):
                print("*",end="")

            else:
                print(" ",end="")
        print()
def print_6(size):
    for i in range(size):
        for j in range(size):
            if  ((i==0 or i==size-1 or  i==size//2) or (j==size-1 and (i>size//2 or i==size-1)) or (j==0 and (i>0 and i<size-1))):
                print("*",end="")

            else:
                print(" ",end="")
        print()


def print_7(size):
    for i in range(size):
        for j in range(size):
            if  i==0 or j==size-1:
                
                print("*",end="")

            else:          
                print(" ",end="")
        print()

def print_8(size):
    for i in range(size):
        for j in range(size):
            if (i>0 and j==0) or(i==0 and j<size) or(i==size//2 and j<size) or(i==size-1 and j<size) or j==size-1: 
                print("*",end="")
            else:
                print(" ",end="")
        print()

  
def print_9(size):
    for i in range(size):
        for j in range(size):
            if  ((i==0 or i==size-1 or  i==size//2) or ((i>0 or i<size//2) and j==size-1 ) or s(j==0 and (i>0 and i<size//2))):
                print("*",end="")
            else:
                print(" ",end="")
        print()
while(1):
    size=int(input("enter the size : "))
    number=input("enter a number from 0-9: ")
    if(number=="0"):
        print_0(size)
        break
    elif(number=="1"):
        print_1(size)
        break
    elif(number=="2"):
        print_2(size)
        break
    elif(number=="3"):
        print_3(size)
        break
    elif(number=="4"):
        print_4(size)
        break
    elif(number=="5"):
        print_5(size)
        break
    elif(number=="6"):
        print_6(size)
        break
    elif(number=="7"):
        print_7(size)
        break
    elif(number=="8"):
        print_8(size)
        break
    elif(number=="9"):
        print_9(size)
        break
    else:
        print("invalid")





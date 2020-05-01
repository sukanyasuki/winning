def print_A(size): 
  
    
    for i in range(size):  
        for j in range((size // 2) + 1):  
            if ((j == 0 or j == size // 2) and i != 0 or i == 0 and j != 0 and j != size // 2 or i == size// 2): 
                print("*", end = "") 
            else: 
                print(" ", end = "") 
          
        print()    


 
def print_B(size):
    for i in range(size):
        for j in range(size):
            if ((j==0 or i>=size) or (i==size//2 and  j<size//2) or((i==0 or i==size-1) and j< size//2) or ((i>0 and i<size//2) or (i>=size//2 and  i<=size-2)) and
                  (j<=0 or  j==(size//2))):
                print("*",end="")

            else:
                print(" ",end="")
        print()



def print_C(size):
    for i in range(size):
        for j in range(size):
            if ((i>0 and i<size-1 and j==0) or ((i==0 or i==size-1) and ((j>0) and (j<=size//2)))):
                
                print("*",end="")

            else:
                print(" ",end="")
        print()



def print_D(size):
    for i in range(size):
        for j in range(size):
            if ((j==0 ) or 
                (j==size//2 and i!=0 and i!=size-1) or
                (i==0 or i==size-1) and (j>0 and j<=size//2-1)) :
                    
                print("*",end="")

            else:
                print(" ",end="")
        print()

def print_E(size):
    
    for i in range(size):
        for j in range(size):
            if(j==1 or((i==0 or i==size-1)and( j>1 and j<size-1))or(i==size//2 and j>1 and j<size-2)):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            
        print()
        
def print_F(size):
    for i in range(size):
        for j in range(size):
            if(j==1 or((i==0)and(j>1 and j<size-1))or(i==size//2 and j>1 and j<size-2)):
                print("*",end=" ")
            else:
                print(" ",end=" ")
                
        print()        


def print_G(size): 
    for i in range(size):     
        for j in range(size):      
            if ((j == 1 and i != 0 and i != size-1) or ((i == 0 or i == size-1) and j > 1 and j < size-2) or (i == ((size-1)/2) and j > size-5 and j < size-1) or (j == size-2 and
                i != 0 and i != size-1 and i >=((size-1)/2))):   
                print("*", end = "") 
            else: 
                print(" ", end = "") 
          
        print()
    

def print_H(size):

    for i in range(size):
        for j in range(size):
            if j==0 or j==size//2+1 or (i==size//2 and j<=size//2):
                    
                print("*",end="")

            else:
                print(" ",end="")
        print()


def print_I(size):
    
    for i in range(size):
        for j in range(size):
            if (i==0 or i==size-1) or j==size//2: 
                print("*",end="")

            else:
                print(" ",end="")
        print()

def print_J(size):
    for i in range(size):
        for j in range(size):
            if ((i==0  or j==size//2) or (i==size-1 and j<=size//2)): 
                print("*",end="")

            else:
                print(" ",end="")
        print()

def print_K(size):
    for i in range(size):
        for j in range(size//2+1):
            if(j==0 ) or (j+i==size//2 or i -j==size//2):
                print("*",end="")
            else:
                print(" ",end="")
        print()        
  

def print_L(size):
    for i in range(size):
        for j in range ((size//2)+1):
            if (i<=size and j==0) or (i==(size-1) and j<=size):
            
                print("*", end = "") 
            else: 
                print(" ", end = "") 
          
        print()
def print_M(size):
    for i in range(size):
        for j in range(size//2+1):
            if(j==0 or j==size//2) or ((i==j) and (j>0 and j<size//2)) or (i==size//2-3 and j==size//2+1) or (i==size//2-2 and j==size//2):
                print("*",end="")
            else:
                print(" ",end="")
        print()
        
def print_N(size):
    for i in range(size):
        for j in range(size):
            if(j==0 or j==size//2) or ((i==j)and (j>0 and j <size//2)):
                print("*",end="")
            else:
                print(" ",end="")
        print()

    
def print_O(size):
    for i in range(size):
        for j in range(size):
            if  (((j==0 or i==0 or j==size-1) and (i!=0 and i!=size-1)) or
                 ((i==0 or  i==size-1) and (j>0 and j<size-1))): 
                print("*",end="")

            else:
                print(" ",end="")
        print()
        
def print_P(size):
    for i in range(size):
        for j in range(size//2+1):
            if(j==0) or( j==size//2 and  (i==size//2-3 or i==size//2-2) or( i==0 or i==size//2-1) and(jl>0 and j<size//2)):
                print("*",end="")
            else:
                print(" ",end="")
        print()



def print_R(size):
    for i in range(size):
        for j in range(size//2+1):
            if(j==0) or (j==size//2 and( i!=0 and i!=size//2)) or ((i==0 or i==size//2) and j>0 and( j< size//2)):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def print_S(size):
    for i in range(size):
        for j in range(size):
            if(i==0 or i==size//2 or i==size-1 or i<size//2 and j==0 or i>size//2 and j==size-1):
                print("*",end="")
            else:
                print(" ",end="")
        print()


def print_T(size):
    for i in range(size):
        for j in range(size//2+1):
            if(j==size//2-2 or i==0):
                print("*",end="")
            else:
                print(" ",end="")
        print()

    



def print_U(size):
    for i in range(size):
        for j in range(size//2+1):
            if(j==0 or j==size//2) and (i!=size-1) or (i==size-1 and (j>0 and j<size//2)):
                print("*",end="")
            else:
                print(" ",end="")
        print()
     
def print_X(size):
    for i in range(size):
        for j in range(size//2+1):
            if(i==j) or (i+j==size//2):
                print("*",end="")
            else:
                print(" ",end="")

        print()
        
def print_Y(size):
    for row in range(size):
        for col in range(size//2+1):
            if(col==0 or col==size//2+2) or (row+col==size//2) or (col-row==size//2):
                print("*",end="")
            else:
                print(" ",end="")
        print()
def print_Z(size):
    for i in range(size):
        for j in range(size):
            if(i==0 or i==size-1 and j>0 and j<size or i+j==size):
                print("*",end="")
            else:
                print(" ",end="")
        print()
       
while(1):
    size=int(input("enter the size"))
    ch=input("enter a character from A-Z:")
    if(ch=="A"):
        print_A(size)
        break
    elif(ch=="B"):
        print_B(size)
        break
    elif(ch=="C"):
        print_C(size)
        break
    elif(ch=="D"):
        print_D(size)
        break
    elif(ch=="E"):
        print_E(size)
        break
    elif(ch=="F"):
        print_F(size)
        break
    elif(ch=="G"):
        print_G(size)
        break
    elif(ch=="H"):
        print_H(size)
        break
    elif(ch=="I"):
        print_I(size)
        break
    elif(ch=="J"):
        print_J(size)
        break
    elif(ch=="K"):
        print_K(size)
        break
    elif(ch=="L"):
        print_L(size)
        break
    elif(ch=="M"):
        print_M(size)
        break
    elif(ch=="N"):
        print_N(size)
        break
    elif(ch=="O"):
        print_O(size)
        break
    elif(ch=="P"):
        print_P(size)
        break
    elif(ch=="Q"):
        print_Q(size)
        break
    elif(ch=="R"):
        print_R(size)
        break
    elif(ch=="S"):
        print_S(size)
        break
    elif(ch=="T"):
        print_T(size)
        break
    elif(ch=="U"):
        print_U(size)
        break
    elif(ch=="V"):
        print_V(size)
        break
    elif(ch=="W"):
        print_W(size)
        break
    elif(ch=="X"):
        print_X(size)
        break
    elif(ch=="Y"):
        print_Y(size)
        break
    elif(ch=="Z"):
        print_Z(size)
        break
    else:
        print("invalid")


















        



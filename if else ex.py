#The if statement


a=20
b=10
if a>b:
    print("a is greater than b")

    #output:a is greater than b 

#The elif statement

    a=10
    print(a>15)
    if a<20:
        print("a is less than 20")
    elif a==18:
            print("a is exactly 18")
    elif a>5 :
            print("a is greater than 5")

            #false
            #a is less than 20

#The else statement


a=int(input("enter a number"))
if(a%2)==0:
    print("number is even")
else:
    print("number is odd")

    #number=4 output:number is even
    #number=5 output: number is odd

    
#short hand if...else
a=100
b=76
print("A") if a>b else print("B")

#output:A

#short hand if
a=3
b=34
if a<b: print("a is less than b")

  #output:a is less than b

#The and keyword
a=100
b=50
c=200
if a>b and c>a:
    print("Both conditions are True")

    #output:Both conditions are True

#The or keyword

a=45
b=67
c=100
if a>b or a<c:
    print("At least one of the conditions is True")

     #output:At least one of the conditions is True
 

# Function program to check string is palindrome

def palindrome(a):
    b=a[::-1]
    if a==b:
        print("palindrome")
    else:
        print("a is not palindrome")

palindrome("racecar")
palindrome("python")
palindrome("adnjy")


#Function program to check number is positive or negative

def positive(a):
    if a>0:
        print(a,"is positive number")
    else:
        print(a,"is negative number")

positive(-45)
positive(100)



#function program to check number is even or odd

def even(a):
    if a%2==0:
        print(a, " is even number")
    else:
        print(a," is odd number")

even(20)
even(15)


#Get input from user and perform (a+b)(a-b)


def process(a,b):
    c=(a+b)*(a-b)
    print(c)
    
e=int(input("enter number"))
f=int(input("enter number"))
process(e,f)      
process(9,3)
process(7,4)
process(6,2)
process(5,1)


#Get inut from user and perform (a+b)(a-b)(a-c)


def function(a,b,c):
    d=(a+b)*(a-b)*(a-c)
    print(d)

e=int(input("enter number "))
h=int(input("enter number "))
k=int(input("enter number "))
function(e,h,k)





















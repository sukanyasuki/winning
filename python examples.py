#python syntax

 ==>print "Hello World"

 print("Hello,World")

 ==>comments in python
 print("Hello,World!")
  # output :Hello,World!


 ==>Docstrings
 
 """This is a
multi line docstring."""
 
  print("Hello.World!")
  
   #output:Hello,World!


#python variables

  ==>create a variable
    a=3
    b="hello"
    print(a)
    print(b)

    #output:5
          #  hello

  ==>output both text and variable
  
      a="programming language"
      print(python is "+a)

        #output:python is programming language

  ==>Add a variable to another variable
            
            a="Hello"
            b="World"
            c=a+b
            print(c)

            #output:Hello World

   ==>verify the type of an object
            a=12
            b="Hello"
            c=1+2j
            print(type(a))
            print(type(b))
            print(type(c))

            #output:int,float,complex

  ==>create integer

            a=123
            b=456783556
            c=-3456
            print(type(a))
            print(type(b))
            print(type(c))

            #output:<class 'int'>


  ==>creating floating  point numbers

            a=3,4
            b=-45.67
            print(type(a))
            print(type(b))

            #output:<class 'float'>


  ==>creating scientific numbers with an "e" to indicate the power of 10

            a=12e34
            b=54E8
            print(type(a))
            print(type(b))

            #output:<class 'float'>

    ==>create complex numbers

            a=1+5j
            b=4j
            print(type(a))
            print(type(b))

            #output:<class 'commplex'>

#python casting

     ==>casting integer
            a=int(1@)
            b=int(4.5)
            c=int("4")
            print(a)
            print(b)
            print(c)

            #output:1o,4,4

    ==>casting floates

            a=float(3)
            b=float("5.6")
            c=float(3.2)
            d=float("4")
            print(a)
            print(b)
            print(c)
            print(d)

            #output:3.0 ,5.6 , 3.2 ,4

    ==>casting strings

            a=str("hello")
            b=str(34)
            c=str(4.5)
            print(a)
            print(b)
            print(c)

            #output:hello ,4.5,34
#python strings
            
   ==>Get the character at postion 1 of string
            a="python"
            print(a[1])

            #output: y

  ==>substring. Get the character from position 2 to position 5

            a="python"
            print(a[2:])

            #output:thon

            
  ==>Remove whitespaces from the beginning or at the end of a string

            a=  "  python  "
            print(a.strip())

            #output:python

  ==>Return length of a string

            a="hello world"
            print(len(a))

            #output:11

  ==>Convert  astring to lower case

            a="PYTHON"
            print(a.lower())

            #output:python


  ==>conver string to upper case

            a="python"
            print(a.upper())

            #output:PYTHON

 ==>Replace string with another string

            a="python"
            print(a.replae("p","r")

           #output:rython

  ==>split a string into substring

                  a="python ,java"
                  print(a.split(",")

                  #output:['python','java']
                        
#python operators
                        
 ==>addition operation

     a=4
     b=5
     c=a+b
     print(c)

     #output:9

 ==>substraction operation
                        
     a=6
     b=3
     c=a-b
     print(c)

     #output:3
                        
  ==>Multiplication operation
                        
     a=6
     b=3
     c=a*b
     print(c)

     #output: 18

  ==>Division operation
     a=6
     b=3
     c=a/b
     print(c)

     #output: 2
                        
  ==>Modules operation
                        
     a=7
     b=3
     c=a%b
     print(c)

     #output: 1
                        
  ==>Assignment operation                      
                    
    a=43
    print (a)
                        
    #output:43

#python lists

  ==>create a list
                        
      a=[1,2,3,4,5]
      print(a)
                        
    #output:[1,2,3,4,5]
                        
  ==>Access item list

        a=[1,2,"java","python"]
        print(a[2])

        #output:java
                        
  ==>change the value of alist

        a=["hi","java","python"]
        a[1]="hello"
        print(a)

         #output:['hi','hello','python']

  ==>Loop through a list
         

        a=["hi","java","python"]
        for b in a :
        print(b)

         #output:hi,hello,python

  ==> Check if list item exists

          a=[1,2,3]
          if 2 in a :
          print("yes,2 is in the number list")

       # output:yes, 2 is in number list

   ==>Get the length of a string

         a=[1,2,3,4,5]
         print(len(a))

       #ouyput: 5
                        
  ==>Add an item to the end of a list

       a=[1,2,3,4]
       a.append(5)
       print(a)

       #output:[1,2,3,4,5]

   ==>Add an item at a specific index

        a=["hi","python"]
        a.insert(1,"java")
        print(a)
        #output:['hi','java','python']
                        
   ==>Remove an item
                        
         a=[1,2,3,4,5]
         a.remove(3)
         print(a)
                        
        #output:[1,2,4,5]

    ==>Remove the last item

         a=[1,2,3,4,5]
         a.pop()
         print(a)
                        
        #output:[1,2,3,4]

     ==>Remove an item at a specified index

            
         a=[1,2,3,4,5]
         del a[2]
         print(a)
                        
        #output:[1,2,4,5]

    ==>Empty list
                        
         a=[1,2,3,4,5]
         a.clear()
         print(a)
                        
        #output:[]

    ==>Using the list() constructor to make a list
                        
        a=list((1,2,3,4,5))
        print(a)
                        
        #output:[1,2,3,4,5]

#python Tuples                        

  ==>Create tuple

       a=("hi","python","java")
       print(a)

       #output:('hi','python'.'java')

  ==>Change tuple values

      a=("hi","python","java")
      a[1]="hello"              
       print(a)

       #output:Tuple is immutable so we cannot change values  it print same tuple.

  ==>Access tuple item

      a=("hi","python","java")
      print(a[2])

       #output:java

  ==>Loop through a tuple 

      a=("hi","python","java")
      for b in a :                 
      print(b)

       #output:hi,python,java                   
                

  ==> Check if a tuple item exists             
                        
      a=("php","python","java")
      if "python" in a :                 
      print("yes, "python" is in a programming tuple)

       #output:yes, 'python' is in a programming tuple

  ==>Get length of a tuple
      a=("hi","python","java")
      print(len(a))

        #output:3


  ==>Deleate a tuple
      a=("hi","python","java")
      del a
      print(a)

        #output:it raise a error

  ==>Using the tuple() constructor to create a tuple
      a=tuple(("hi","python","java"))
      
      print(a)

        #output:('hi','python','java')


#Python sets


 ==>Create a set
     a={1,2,3,4}
     print(a)
            
     #output:{1,2,3,4}
            
 ==>Loop through a set       
        
     a={1,2,3,4}
     for b in a :
     print(b)
            
     #output:1,2,3,4                
               
                        
                        
==>Check if an item exist      
        
     a={1,2,3,4}
     print(3 in a)
            
     #output:True               

  ==>Add an item to a set     
        
     a={"hi","hello","python"}
     a.add("java")
     print(a)
            
     #output:{'hi','hello','python','java'}


  ==>Add multiple item to a set     
        
     a={"hi","hello","python"}
     a.update("java","world")
     print(a)
            
     #output:{'hi','java','world''hello','python'}


   ==>Get length of a set     
        
     a={"hi","hello","python","java"}
     print(len(a))
            
     #outpu:4


   ==>Remove an item in  a set     
        
     a={"hi","hello","python","java"}
     a.remove("python")
     print(a)
            
     #outpu:{'hi','hello','java'}


 ==>Remove an item in  a set by using the discard() method    
        
     a={"hi","hello","python","java"}
     a.discard("python")
     print(a)
            
     #outpu:{'hi','hello','java'}



  ==>Remove the last item in  a set by using the pop() method    
        
     a={"hi","hello","python","java"}
     a.pop()
     print(a)
            
     #outpu:{'hi','hello','java'}


  ==>Empty a set  
        
     a={"hi","hello","python","java"}
     a.clear()
     print(a)
            
     #outpu:set()

  ==>Deleate a set  
        
     a={"hi","hello","python","java"}
     del a
     print(a)
            
     #outpu:It raise an error

            
   ==>Using the set() constructer to create a set
        
     a=set(("hi","hello","python","java","world"))
     print(a)
            
     #outpu:{'hi','hello','python','java','world'}

#Python Dictionaries
            
    ==>Create a dictionary
            

    dict={1:"hello",2:"python",3:"java"}
    print(dict)

      #output:{1:'hello',2:python',3:'java'}


   ==>Access the items of a dictionary
            

    dict={1:"hello",2:"python",3:"java"}
    b=dict[2]        
    print(b)

      #output:python
            

 ==>Change the value of a specific item in a dictionary
            

    dict={1:"hello",2:"python",3:"java"}
     dict[3]="world"       
    print(dict)

      #output:{1:'hello',2:python',3:'world'}

            
 ==>print all key names in a dictionary,one by one
            

    dict={1:"hello",2:"python",3:"java" /n}
    dict.keys()      
    print(dict)

      #output:1
              2
              3


            
 ==>print all values  in a dictionary,one by one
            

    dict={1:"hello",2:"python",3:"java" }
    for a in dict      
    print(a)

      #output:hello
              python
              java


            
 ==>Using the  values()  function to return values of  a dictionary
            

    dict={1:"hello",2:"python",3:"java" }
    dict.values()     
    print(dict)

      #output:hello
              python
              java


 ==>Loop through both keys an values by using the items() function 
            

    dict={1:"hello",2:"python",3:"java" }
    dict.items()     
    print(dict)

      #output:1 hello
             2  python
             3 java



  ==>Check if a keys exist 
            
    dict={1:"hello",2:"python",3:"java" }
    if 2 in dict :    
    print("yes, 2 is one the keys in the dict dictionary")

      #output:yes, 2 is one the keys in the dict dictionary

            
  ==>Get the length of a dictionary
            
    dict={1:"hello",2:"python",3:"java",4:"hi" }   
    print(len(dict))
            
      #output:4

  ==>Add an element to a dictionary
            
    dict={1:"hello",2:"python",3:"java",4:"hi" }
     dict[5]="world"       
    print(dict)
            
      #output:={1:'hello',2:'python',3:'java',4:'hi',5:'world }
     

  ==>Remove an item from a dictionary
            
    dict={1:"hello",2:"python",3:"java",4:"hi" }
     dict.pop(3)      
    print(dict)
            
      #output:={1:'hello',2:'python',4:'hi'}


 ==>Empty a dictionary
            
    dict={1:"hello",2:"python",3:"java",4:"hi" }
     dict.clear      
    print(dict)
            
      #output:{}


 ==>Using the dict()construtor to create a dictionary
            
    a=dict(1:"hello",2:"python",3:"java")     
    print(a)
            
      #output:{1:'hello',2:'python',3:java'}






            


            









            






            







            


            


            
           

            
            


            
          

            
         

            
          

            
        

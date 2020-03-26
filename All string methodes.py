#Capitaliz()

a="python"
b=a.capitalize()
print(b)

  #Description :This method is used to  convert first character  of a string is capital.

#casefold()

a="HELLO WORLD"
b=a.casefold()
print(b)

   #Description :This method is used to convert hole string into lower case.

#center()
a="python"
b=a.center(10)
print(b)
    
  #Description :This method is used to center aline the string,using a specified character.

#count()
a="hello world hello"
b=a.count("hello")
print(b)        
          
  #Description :This method used to returns the number of times repeated values in a given string.

#encode()
a="hello world"
b=a.encode()
print(b)

  #Description :This method is  used to encoded version of string.

#endswith()

a="welcome to python class"
b=a.endswith(".")
print(b)
   # Description : This method is used to return True if given string ends with a specified value,otherwise it return false.


#expandtabs()

a="w\to\tr\tl\td"
b=a.expandtabs(2)
print(b)
    #Description : This method is used to sets the tab size to specified number of whitespaces.


#find()
 
a="hello world welcome"
b=a.find("w")
print(b)

    #Description :This method is used to find the first occurance value of a given string.

#format()

a="How to learn {programming}, easy"
print(a.format(programming="python"))
#print(b)

    #Description :This method is used to format the specified value and insert them inside the string.

#format_map()

a={'x' :'python' ,'y' :'language'}
b=("{x} is programming {y}".format_map(a))
#print(b)
    #Description :This method is used to format specified value in a given string.

#index()
a="welcome python program"
b=a.index("o")
print(b)
     #Description :This method is used to find specified value and returns the position of  a string where it is occur.

#isalnum()
a="computer23"
b=a.isalnum()
print(b)
     #Description :This method is used to verify all characters in a string  are alphanumeric then the result is true.

#isalpha()
a="python"
b=a.isalpha()
print(b)
     #Description :This method is used to find given string contains all characters are alphabets then it returns true.

#isdecimal()
a="0123"
b=a.isdecimal()
print(b)
     #Description : This method is used to returns true if given string contains all characters are decimals(0-9).

#isdigit()
a="50200"
b=a.isdigit()
print(b)
     #Description :This method is used to find given string contains all digits  then it returns true otherwise false.

#isidentifier()
a="python"
b=a.isidentifier()
print(b)
     #Description :This method is used toreturn true if the syring is a valid identifier otherwise false.

#islower()
a="python"
b=a.islower()
print(b)
     #Description :This method is used to find given string contains all characters are lower case then it give result true,otherwise false.

#isnumeric()
a="23456"
b=a.isnumeric()
print(b)
    #Description :This method is used to find given string contains all characters are numeric then it give result true otherwise false.

#isprintable()
a="python"
b=a.isprintable()
print(b)
    #Description :This method is used to find all characters are printable or not is printable it give result true,otherwise false.

#isspace()
a="  java  "
b=a.isspace()
print(b)
    #Description :This method returns true all characters in a string are whitespaces otherwise false.

#istitle()
a="Hello"
b=a.istitle()
print(b)
     #Description :This method is used to return if all words in a string start with upper case and remain all words are lower case otherwise false.

#isupper()
a="PYTHON"
b=a.isupper()
print(b)
     #Description :This method is used tofind all characters of a string is upper case then it returns true otherwise false.

#join()
a=("hello","world")
b="*".join(a)
print(b)
     #Description :This method takes all iterable and join them into one string.

#ljust()
a="java"
b=a.ljust(5)
print(b,"is programming language")
     #Description :This method is used to will left aline the string using a specified characters as the fill characters.

#lower()
a="PYTHON and JAVA"
b=a.lower()
print(b)
     #Description :This method is used to convert all characters of string into lower case.

#lstrip()
a="   hello   "
b=a.lstrip()
print(b)
     #Description :This method is used to remove string contain left whitespaces.

#partition()
a="I drink water daily"
b=a.partition("water")
print(b)
     #Description :This method is used to search for a specied string and split the string into a tuple contains three elements.

#replace()
a="I learn java"
b=a.replace("java","python")
print(b)
     #Description :This method is used to replace a specified word with another specified word in a given string.

#rfind()
a="Hello welcom to python program"
b=a.rfind("o")
print(b)
      #Description :This method is used to find last occurance of the specified value in a given string.

#rindex()
a="Hello world welcome"
b=a.rindex("come")
print(b)
      #Description :This method is used to find last occurance of the specified value of a given string.

#rjust()
a="python"
b=a.rjust(10)
print(b,"is programming language")
      #Description :This method is used will right aline string using a specified character as the fill character.
#rpartition()
a="I learn python because it is easy"
b=a.rpartition("python")
print(b)
      #Description :This method is used to find for the last occurance of a specified string and split the string into tuple containing thre elements.

#startswith()
a="Hello world"
b=a.startswith("Hello")
print(b)
      #Description :This method is used to find string stats with specified value then it gives true otherwise false.

#strip()
a="     java   "
b=a.strip()
print(b)
      #Description :This method is used to remove any leading and travelling whitespaces of a string.
#swapcase()
a="Hello World"
b=a.swapcase()
print(b)
      #Description :This method is used to convert all lower case letters into upper case and vice versa.

#title()
a="welcome world"
b=a.title()
print(b)
      #Description :This method is used to convert every first character in every first word is upper case.

#upper()
a="python"
b=a.upper()
print(b)
     #Description :This method is used to convert string into upper case.

#zfill()
a="65"
b=a.zfill(8)
print(b)
     #Description :This method is used to add at the beginning of the string until it reaches the specified length.



#How to reverse a list

   Every list in python has a built in reverse() method.

Definition:Reverse list means the list containing values  give in reverse order.


They are several methods to reverse a list.they shown below

  1.We use a list reverse()method

  Ex:a=[1,2,3,4,5]
     b=a.reverse()
     print(b)

output:[5,4,3,2,1]

  2.using the negative indexing order

    Ex:a=[1,2,3,4,5]
       b=(a[::-1])
       print(b)

output:[5,4,3,2,1]


#Difference between copy and direct assignment in list

#List copy() method

Definition: It copy the list elements.
  * The copy method is basically an overloaded constructor.
  * It initilize the new object with an already existing object.
  * Both the objects uses seperate memory locations.
  
Ex : a=[1,2,3,4,5]
     b=a.copy()
     print(b)
     output:[1,2,3,4,5]

# direct
  *Direct initilization can be done using assignment operator,
  * This assins the value of one object to another object both are already exists.
  *One memory location is used but different reference variables are pointing to the same location.

Ex: a=[1,2,3,4,5]
    b=a
    print(b)

    output: [1,2,3,4,5]


#Difference between clear and delete methods in list

    #clear()
    Clear means remove all items from the list.
    #use clear() method
    Ex: a=[1,2,3,4]
        b=a.clear()
        print(b)

        Output:[]

    #clear the list using delete method
        Ex: a=[1,4,5,6]
             b=a.del[:]
             print(b)

             Output: []

    #delete()
             Delete means remove the item at a specific index from given list.

             Ex:a=[1,2,3,4,5]
             b=a.del[2]
             print(b)

     
     Output :[1,2,4,5]

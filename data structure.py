#Data structure

Data structure is used to store a collection of related data.
They are four types of data structuer.
     1.List
     2.Tuple
     3.Set
     4.Dictionary

#1.List:
==>It is enclosed in square brackets[]

#Properties of list:

==>Indexing and ordering is possible.
==>Duplicates are allowed.
==>It is mutable.Mutable means change and adding elements is possible in list.

Example:

    a=[1,2,3,"hello",5,4,2,6]

List methods:
1.append() :Adding element at the end of the list
 Ex:
   a=[1,2,3]
   b=a.append(4)
   print(b)

   o/p:[1,2,3,4]
   
2.clear() :remove all elements in the list.
Ex:
    a=[1,2,3,4]
    b=a.clear()
    print(b)

    o/p:[]

3.copy() :Return a copy of the specified list.
Ex:
    a=[1,2,3]
    b=a.copy(a)
    print(b)

    o/p:[1,2,3]
    
4.count() :Number of elements with the specified value.
Ex:
    a=[1,2,3,4,2,3]
    b=a.count(3)
    print(b)

    o/p:2

5.extend():Add element to the end of the list.
Ex:
    a=[1,2,3,4]
    b=[5,6,7]
    c=a.extend(b)
    print(c)

    o/p:[1,2,3,4,5,6,7]

6.index():Return the position at first occurence of the list.
Ex:
    a=[1,2,3,2,4]
    b=a.index(2)
    print(b)

    o/p:1

7.insert():we can insert the value at the soecified position of the list.
Ex:
    a=[1,2,3]
    b=a.insert(1,5)
    print(b)

    o/p:[1,5,2,3,]

8.pop():Remove an element  at the specified value.
Ex:
    a=[1,2,3,4,5]
    b=a.pop(3)
    print(b)

    o/p:[1,2,3,5]

9.reverse():return the list in reverse order.
Ex:
    a=[1,2,3,4,5]
    b=a.return()
    print(b)

    o/p:[5,,4,3,2,1]

10.remove():delete an element at specific position.
Ex:
    a=[1,2,3,4]
    b=a.remove(2)
    print(b)

    o/p:[1,3,4]

11.sort():we can arrange the list in accending order.
Ex:
    a=[2,4,3,1,5]
    b=a.sort()
    print(b)

    o/p:[1,2,3,4,5]


# Tuple :
==>It is enclosed in paranthices ()

Example:a=(1,2,3,4)

#properties of tuple:

==>Indexin and orderining is possible.
==>Duplicates are  allowed.
==>Inmutiable.Inmutable means changing and adding elements is not possible in tuple.

#Tuple methods
1.count():Number of elements with the specified value.
Ex:
    a=(1,2,3,4,2,3,4,5)
    b=a.count(4)
    print(b)

    o/p:2

2.index():find the first occurence of the specified value.
Ex:
    a=(1,2,3,4,5,2)
    b=a.index(2)
    print(b)

    o/p:1


#Set
    ==>It is enclosed by curlly brackets {}
    
    a={1,2,3,4,5}

#properties of set
 ==>Indexing and orderining is not possible.
 ==>Dupicates are not allowed.
 ==>set is mutable.

 #set methods:
 1.add():Add an element to the set.
 Ex:
    a={1,2,3,4}
    b=a.add(5)
    print(b)

    o/p:{1,2,3,4,5}

2.clear():Remove all elements from the set.
Ex:
    a={1,2,3,4}
    b=a.clesar()
    print(b)

    o/p:{}

3.copy():Return a copy of the set.
Ex:
    a={1,2,3,4}
    b=a.copy()
    print(b)

    o/p:{1,2,3,4}

4.difference():Return a set containing the diffference betweentwo or more sets.
Ex:
    a={1,2,3,4,5}
    b={4,5,2,6}
    c=a.difference(b)
    print(c)

    o/p:{1,3}

5.difference_update():Remove the items that exist in both the sets.
Ex:
    a={1,2,3,4}
    b={4,3,5,6}
    c=a.difference_update(b)
    print(c)

    o/p:{1,2}

6.discard():Remove the soecified item.
Ex:
    a={1,2,3,4,7,8}
    b=a.discard(3)
    print(b)

    o/p:{1,2,4,7,8}

7.intersection:Return a set that is the intersection of two other sets.
Ex:
    a={1,2,3,4}
    b={2,3,5,6}
    c=a.intersection(b)
    print(c)

    o/p:{2,3}

8.intersection_update():Remove the  items that is not present in both the sets.
Ex:
    a={1,2,3,4,5}
    b={2,4,6,7}
    c=a.intersection_update(b)
    print(c)

    o/p:{2,4}

9.isdisjoint():Method returns true if none of the items are present in both the sets.
Ex:
    a={1,2,3,4}
    b={5,6,7}
    c=a.isdisjoint(b)
    print(c)

    o/p:true

10.issubset():Method return true if all items in the set exists in the specified set .
Ex:
    a={1,2,3,4,5}
    b={2,3,4,5,6,7}
    c=a.issubset(b)
    print(c)

    o/p:true

11.issuperset():Method return true if all items in the specified set exists in the original set
Ex:
    a={1,2,3,4,5}
    b={3,4,5}
    c=a.issuperset(b)
    print(c)

    o/p:true

12.pop():Method remove a random item from the set.
Ex:
    a={1,2,3,4}
    b=a.pop()
    print(b)

    o/p:{1,3,4}

13.remove():Remove the specified item.
Ex:
    a={1,2,3,4,5}
    b=a.remove(3)
    print(b)

    o/p:{1,2,4,5}

14.symmetric_difference():Method returns a set that contains all items from both the sets,but not the items that are present in both sets.
Ex:
    a={1,2,3,4,5}
    b={6,7,8,9,3,4}
    c=a.symmetric_difference(b)
    print(c)

    o/p:{1,2,5,6,7,8,9}

 15.symmetric_difference_update():Method update the original set by rempving items that are present in both sets and inserting the other items.
 Ex:
     a={1,2,3,4}
     b={6,7,8,3}
     c=a.symmetric_difference_update(b)
     print(c)

     o/p:{1,2,4,6,7,8}

  16.union():Method return a set all  items containing both original and specified set.
  Ex:
      a={1,2,3,4}
      b={4,5,2,7}
      c=a.union(b)
      print(c)

      o/p:{1,2,3,4,5,7}

 17.update():Method update the current set by adding from another set.
 Ex:
     a={1,2,3,4}
     b={4,5,2}
     c=a.update(b)
     print(c)

     o/p:{1,2,3,4,5}


#Dictionary

 ==>It is enclose by currly braces with colan {:}
 
 Ex:a={1:"java",2:"python",5:"hello"}

 #Properties of dictionary
 ==>Indexing and orderining not possible.
 ==>Duplicate keys are not allowed but duplicate values are allowed.
 ==>Dictionary is mutable.

 #Dictionary methods

 1.clear():It remove all items from the dictionary.
 Ex:
     a={1:"hello",2:"hi",3:"java"}
     b=a.clear()
     print(b)

     o/p:{}

2.copy():Return copy of the dictionary.
Ex:
    a={1:"hi",2:"hello"}
    b=a.copy()
    print(b)

    o/p:{1:'hi',2:'hello'}

3.fromkey():Method return a dictionary with specified keys and the specified value.
Ex:
    a={1,2,3}
    b={python,java,hi}
    c=dict.fromkeys(a,b)
    print(c)

    o/p:{1:'python',2:'java',3:'hi'}

4.get():Method returns the value of the item with specified key.
Ex:
    a={1:"hi",2:"python"}
    b=a.get(2)
    print(b)

    o/p:python

5.items():Returns a list containing a tuple for each key value pair.
Ex:
    a={1:"java",2:"hi"}
    b=a.item()
    print(b)

    o/p:([(1,'java'),(2,'hi')])

6.keys():Returns a list containing the dictionary keys.
Ex:
    a={1:"python",2:"java"}
    b=a.keys()
    print(b)

    o/p:([1,2])

7.pop():Remove the specified item from the dictionary.
Ex:
    a={1:"hi",2:"welcome",3:"python"}
    b=a.pop(2)
    print(b)

    o/p:{1:'hi',3:'python'}

8.popitem(): Remove the last inserted key value pair.
Ex:
    a={1:"hi",2:"python",3:"java"}
    b=a.popitem()
    print(b)

    o/p:{1:'hi',2:'python'}

9.update():Update the dictionary with the specified key value pairs.
Ex:
    a={1:"hello",2:"hi"}
    b=a.update({6:"java"})
    print(b)

    o/p:{1:'hello',2:'hi',6:'java'}

10.values():Return a list of all the values in the dictionary.
Ex:
    a={2:"hi",4:"java",3:"python"}
    b=a.vlues()
    print(b)

    o/p:(['hi','java','python'])

11.setdefault():Return the value of the specified key.
Ex:
    a={1:"hi",2:"java",5:"hello"}
    b=a.setdefault(1)
    print(b)

    o/p:hi
     
    
       

    
    
    

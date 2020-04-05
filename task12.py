#Task 1
s=[]
a=[5,6,8,9]

m=s+a
print(m)  #concatation
print(a)
a.append(8)
a.append(9)
a.append(1)
a.append(5)
a.append(6)
a.append(7)
a.append(8)
b=a.count(8)
print(a)  #adding elements to the list
print(b)  #first occurence of 8
average=sum(a)/len(a)

print("averge of the list=",average)  #average
e=sum(a)+min(a)+max(a)
print(e)  #sum of list,minume value of list and maxiam list
f=set(a)
print(f)  #remove duplicates
h=(len(a))
print(h)
g=sum(a)
print(g)
mean=g/h
print("mean of the list=",mean) #mean of list
a.sort()
print(a)  #sort list
median=len(a)//2
result=(a[median]+a[~median])/2
print("median of the list=",median)
n=(5+1)/2
print(n)   #median
j=tuple(f)
print(j)    #list conver to tuple



#Task 2
set1=set({})
set2=set({})
print(set1)
print(set2)
a={7,8,9,1,2,3,4,5,0}
set1.update(a)  #update set1
print(set1)
b={4,5,6,0}
set2.update(b)  #update set2
print(set2)
c=set2.issubset(set1)  #check set2 is subset of set1
print(c)
d=set1.isdisjoint(set2)  #check is disjoint
print(d)
set1.discard(8)  #remove 8 from set1
print(set1)
set2.discard(0)  #remove 0 from set2
print(set2)
h=set1.union(set2)
print(h)
k=sum(h)
print(k)  #sum


#Tak 3

tuple1=(1,4,5,6,7)
tuple2=(5,6,7,8,9)
a=set(tuple1)  #remove duplicates of tuple1
print(a)
b=set(tuple2)  #remove duplicates of tuple2
print(b)
result=(tuple1 +tuple2)
print("result is concatation=",result)  #concetation
h=set(result)
print(h)
print(result[-1])  #index value of 9
c=result*3  #multiplication
print(c)
d={0,4,5}
print(d)
commonElement=(d&h)  #common elements
print("commonElement of tuples=",commonElement)
l=tuple(commonElement)
print(l)
k=l*3   #multiplication
print(k)


#task 4

dictionary={1:["english","maths","science",["bio-zoology","bio-botany","physics"]],2:(10,20,40,"python program")}
print(dictionary[1][-1][-2][-6:])  #botany
a=(dictionary[1][0:3])   #english,maths,science
print(a)
b=tuple(a)  #convert dictionary to tuple
print(b)
print(len(b))  #lenth of tuple
print(dictionary.keys())  #print all keys




              





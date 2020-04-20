import random
list=["snake","water","gun"]
print(list)
point1=0
point2=0
i=0
while i<=10:
    
    random=random.choice(list)
    user=input("enter a string:")
    if random=="snake" and user=="snake":
        print("tie")
        print("both have no points")
        break
    elif random=="snake" and user=="water":
        print("system win")
        print("system has one point")
        point2=point2+1
        break
    elif random=="snake" and user=="gun":
        print("user win")
        print("user has one point")
        point1=point1+1
        break
    elif random=="water" and user=="snake":
        print("user win")
        print("user has one point")
        point1=point1+1
        break
    elif random=="water" and user=="water":
        print("tie")
        print("both have no points")
        break
    elif random=="water" and user=="gun":
        print("system win")
        print("system has one point")
        point2=point2+1
        
        break
    elif random=="gun" and user=="snake":
        print("user win")
        print("user has one point")
        point1=point1+1
        
        break
    elif random=="gun" and user=="gun":
        print("tie")
        print("both have no points")
        i=i+1


print("your scors is",point1)
print("random score is",point2)
if point1>point2:
      print("user win the game")
elif point2>point1:
    print("system win the game")
else:
    print("tie")


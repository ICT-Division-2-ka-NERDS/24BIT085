import random
n1=int(input("Enter length of list 1: "))
n2=int(input("Enter length of list 2: "))

l1=[]
for i in range(n1):
    l1.append(random.randint(1,100))

l2=[]
for i in range(n2):
    l2.append(random.randint(1,100))

l3=[i for i in l1 if i not in l2]
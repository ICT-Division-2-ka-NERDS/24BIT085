import random

l=[]
for i in range(20):
    l.append(random.randint(1,100))
print(l)
n=int(input("Enter number to check it's occurence: "))

for i in range(20):
    if l[i]==n:
        print("Occurence Position-->", i)

import random
l=[]
for i in range(30):
    l.append(random.randint(-200,200))

pos=[]
neg=[]

for j in l:
    if j>0:
        pos.append(j)
    elif j<0:
        neg.append(j)
    else:
        pass

print("All of positive number--> ",pos)
print("All of negative number--> ",neg)

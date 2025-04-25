import random as r

l=[]
for i in range(10):
    l.append(r.randrange(15,45))

l=set(l)
print(l)
l=list(l)

c=0
for i in l:
    if i<30:
        c+=1
    elif i>35:
        l.pop(l.index(i))

l=set(l)
print(l)
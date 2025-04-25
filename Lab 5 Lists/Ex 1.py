import random
le=[]
lo=[]

i=0
while i<5:
    j=random.randint(1,100)
    if j%2!=0:
        lo.append(j)
        i+=1

j=0
while j<4:
    m=random.randint(1,100)
    if m%2!=0:
        le.append(m)
        i+=1
lo[2]=le

x=lo
print(x)
for e in x:
    if type(e)==type(x):
        c=lo.index(e)
        x.remove(e)
        for n in e:
            x.insert(c,n)
            c+=1

print(x)
x.sort()
print(x)

import random as r
l=[]
for i in range(0,10):
    l.append(r.randrange(-15,16))
print(l)

def rans(l):
    return l*l

print("hacker on top")
m=map(rans,l)
print(list(m))
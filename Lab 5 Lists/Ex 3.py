import random

l=[]
for i in range(50):
    l.append(random.randint(1,30))

for j in range(50):
    n=l[j]
    for k in range(50):
        if j==k:
            continue
        elif l[k]==n:
            del l[k]

print(l)

l1=['apple','banana','papaya','cherry']

l2=[]
for i in l1:
    if i.count('a')>=1:
        l2.append(i)
print(l2)
''' --------------------------- '''

l3=[i for i in l1 if 'a' in i]
print(l3)

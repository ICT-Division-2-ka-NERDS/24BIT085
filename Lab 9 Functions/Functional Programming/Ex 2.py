l1=[i for i in range(1,7)]
l2=[i for i in range(6,0,-1)]

k=lambda e1,e2:e1+e2
m=map(k,l1,l2)
print(list(m))
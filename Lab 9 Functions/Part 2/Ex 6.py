def sali(l,i=0):
    if i>=len(l):
        return l
    
    if l[i]<0:
        l[i]=0

    return sali(l,i+1)

l=[1,-3,5,-6,4]
print(sali(l))
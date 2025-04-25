def reli(l):
    if l==[]:
        return []
    
    if len(l)==1:
        return l
    
    return [l[-1]] + reli(l[:-1])

l=[1,2,3,4,5]
print(reli(l))
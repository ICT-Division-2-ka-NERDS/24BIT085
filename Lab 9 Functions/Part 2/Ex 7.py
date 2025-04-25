def av(l,i=0,total=0):
    if l==[]:
        return 0
    if len(l)==1:
        return l[0]
    
    if len(l)==i:
        return total/i 
    
    return av(l,i+1,total+l[i])

print(av([1,23,4]))
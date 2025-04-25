def pfac(num,factor=2,factors=None):
    if factors is None:
        factors=[]
    
    if num<2:
        return factors
    
    if num%factor==0:
        factors.append(factor)
        return pfac(num//factor,factor,factors)
    else:
        return pfac(num,factor+1,factors)
    
print(pfac(12))

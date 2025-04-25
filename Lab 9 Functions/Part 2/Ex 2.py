def bn(n):
    if n==0:
        return '0'
    if n==1:
        return '1'
    
    return bn(n//2)+str(n%2)

print(bn(27))
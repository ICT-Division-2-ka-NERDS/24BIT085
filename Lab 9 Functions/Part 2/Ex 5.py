def pow(a,b):
    if b==0:
        return 1
    if b==1:
        return a
    
    return pow(a,b-1)*a

print(pow(2,3))
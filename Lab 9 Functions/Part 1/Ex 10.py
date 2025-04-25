def frequency(s):
    l=s.split(' ')
    d={}
    for i in l:
        c=0
        for j in l:
            if i==j:
                c+=1
        d[i]=c
    
    return d

st='are are are is is'
print(frequency(st))
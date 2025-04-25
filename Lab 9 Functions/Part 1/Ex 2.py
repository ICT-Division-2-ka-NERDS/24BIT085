def co(n):
    j=1
    ts,s=0,0
    while i>5:
        for i in range(0,5):
            ms+=n**(j**i)
            s+=ms
        ts+=s
    return ts    

    #return (n)+(10*n+n)+(100*n+10*n+n)+(1000*n+100*n+10*n+n)

for i in range(4,8):
    print(i,"-->",co(i))
def tup(x):
    l=[]
    for i in range(x+1):
        x=(i,i**2,i**3)
        l.append(x)

n=int(input("Enter a number: "))
tup(n)
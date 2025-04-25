import math

def fac(i):
    r=1
    for i in range(1,i+1):
        r*=i
    return r

def sin(n):
    n*=(22/7)/180
    i=1
    c=2
    while True:
        r=(n**i)*(-1**(c))/fac(i)
        i+=2
        c+=1
        print(r)

m=int(input("Enter Angle in degrees: "))
sin(m)

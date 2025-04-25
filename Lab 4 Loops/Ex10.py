f=0
s=1
l=[f,s]
n=int(input("Enter a number to print fibonacci series: "))

if n==1:
    print(0)

if n==2:
    print(1)

for i in range(n):
    c=f+s
    l.append(c)
    f=s
    s=c

print(l)
n=int(input("Enter number to check prime,perfect,armstrong,palindrome,automorphic: "))

i=2
while i<n:
    if n//i==0:
        print(n,"is not a prime number")
    i+=1

else:
    print(n,"is a prime number")


l=[]
while i<n:
    s=0
    if s//i==0:
        l.append(i)
        s+=i
    i+=1
    if s==n:
        print(n,'is a perfect number')

    else:
        print(n,'is not a perfect number')


sa=0
d=10

nu=n
while sa<=n:
    nu=nu%d
    sa+=nu**3
    d*=10

if sa==n:
    print(n,'is an armstrong number')

else:
    print(n,'is not an armstrong number')


sn=str(n)
l=sn.split()
m=len(sn)
pn=n
rsn=[]

la=pn%10**(m-1)
ma=la//10**(m-2)
fa=la%10**(m-2)

rsn.append(fa)
rsn.append(ma)
rsn.append(la)

if rsn==l:
    print("is Palindrone")

else:
    print("not Palindrone")


sq=n**2
nl=n%10
ld=sq%10
if ld==nl:
    print('is Automorphic')
else:
    print('is not Automorphic')
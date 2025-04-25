n=int(input("Enter Upper Limit: "))
r=int(input("Enter Number: "))
for i in range(1,n+1):
    nfac=1
    nfac*=i

for i in range(1,r+1):
    rfac=1
    rfac*=i

for i in range(1,n-r+1):
    nrfac=1
    nrfac*=i

ncr=nfac/(rfac*nrfac)
npr=nfac/nrfac

print(n,"C",r,"is =",ncr)
print(n,"P",r,"is =",npr)

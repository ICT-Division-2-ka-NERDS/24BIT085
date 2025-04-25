n=input("Enter string: ")
for i in range(0,len(n)):
    if n[i].isupper==True:
        continue
    elif n[i].islower==True:
        p=ord(n[i])
        p=p-32
        n[i]=chr(p)

print(n)

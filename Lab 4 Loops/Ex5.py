n=int(input("Enter number to print all pythagorean triplet before it: "))
for i in range(0,n-2):
    a=i
    b=i+1
    c=i+2
    if c**2==a**2+b**2:
        print("Phythagorean Triplet -->",a,b,c)
    else:
        continue
    

t=(124,'asdds',235,6798,234)
l=list(t)

n=int(input("Enter the no.of element to be modified: "))
ne=input('Enter the new element: ')
l[n-1]=ne

t1=tuple(l)

print('New tuple ',t1)
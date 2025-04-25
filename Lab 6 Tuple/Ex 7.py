t=(124,'asdds',235,6798,234)
l=list(t)

n=int(input("Enter the no.of element to delete: "))
l.pop(n-1)

t1=tuple(l)
print('New tuple ',t1)
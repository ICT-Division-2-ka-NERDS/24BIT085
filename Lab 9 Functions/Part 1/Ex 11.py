def create_list(l1,l2):
    l=[]
    for i in l1:
        for j in l2:
            if i==j:
                l.append(j)
    
    print(l)

n=int(input("Enter range of lists: "))

l1,l2=[],[]
for k in range(n+1):
    ele=input("Enter element")
    l1.append(ele)

for k in range(n+1):
    ele=input("Enter element")
    l2.append(ele)

create_list(l1,l2)
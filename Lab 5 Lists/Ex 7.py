#Stack --> LIFO

s=[]
c='y'
while c=='y':
    print('1. Push')
    print('2. Pop')
    print('3. Display')
    choice=int(input("Enter choice of action:"))
    if choice==1:
        i=input("Enter Value: ")
        s.append(i)
    elif choice==2:
        if s==[]:
            print("Error no element is Stack")
        else:
            print("Deleted element is,",s.pop())
    elif choice==3:
        l=len(s)
        for i in range(l):
            print(i[i-l])
    else:
        print("Wrong input")
    c=input("do you wish to continue? n,y")

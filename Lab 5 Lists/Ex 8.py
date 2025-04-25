#Queue --> FIFO

a=[]
c='y'
while (c=='y'):
    print('1. Insert')
    print('2. Delete')
    print('3. Display')
    print('4. Peek')
    choice=int(input('Enter your choice: '))
    if choice==1:
        b=int(input('Enter new number: '))
        a.append(b)
    elif choice==2:
        if(a==[]):
            print('queue empty')
        else:
            print('Deleted element is:', a[0])
    elif choice==3:
        l=len(a)
        for i in range(0,l):
            print(a[i])
    elif choice==4:
        print(a[-1])
    else:
        break

class ComDate:
    def __init__(self,day,month,year):
        self.l=[day,month,year]
    
    def __eq__(self,other):
        if isinstance(other,ComDate):
            return self.l == other.l
        else:
            return False

n='y'
while n=='y':
    l1=[]
    l2=[]
    for i in range(2):
        day=int(input('Enter Day: '))
        month=int(input('Enter Month: '))
        year=int(input('Enter Year'))
        if i==1:
            l1.append(day,month,year)
        elif i==2:
            l2.append(day,month,year)
    
    d1=ComDate(l1)
    d2=ComDate(l2)
    print(d1==d2)

    c=input('Do u wish to continue y/n: ')
    if c.lower()=='n':
        break
    else:
        print('-_-   bruh')
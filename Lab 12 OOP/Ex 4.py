class DIMEN_2:
    def __init__(self,sha,dime):
        self.sha = sha
        self.dime = dime
    
    def perimeter(self):
        if self.sha == 'rectangle':
            l = self.dime['length']
            b = self.dime['breadth']
            return 2*(l+b)
        
        elif self.sha == 'square':
            a = self.dime['side']
            return 4*a

        elif self.sha == 'circle':
            r = self.dime['radius']
            return 2*3.14159*r
        
        else:
            print('Wrong Shape!!')
        
    def area(self):
        if self.sha == 'rectangle':
            l = self.dime['length']
            b = self.dime['breadth']
            return l*b
        
        elif self.sha == 'square':
            s = self.dime['side']
            return s**2

        elif self.sha == 'circle':
            r = self.dime['radius']
            return 3.14159*r*r

        else:
            print('Wrong Shape!!')
    
n='y'
while n=='y':
    print("Choose Shape [1.rectangle, 2.square, 3.circle]: ")
    c=int(input())
    if c==3:
        r = int(input('radius: '))
        DIMEN_2=DIMEN_2("circle", {"radius": r})
        print("Circle circumference:", DIMEN_2.perimeter())
        print("Circle area:", DIMEN_2.area())

    elif c==1:
        l = int(input('length: '))
        b = int(input('breadth: '))
        DIMEN_2 = DIMEN_2("rectangle", {"length": l, "breadth": b})
        print("Cylinder Surface Area:", DIMEN_2.perimeter())
        print("Cylinder area:", DIMEN_2.area())

    elif c==2:
        a = int(input('side: '))
        DIMEN_2 = DIMEN_2("square", {"side": a})
        print("square Surface Area:", DIMEN_2.perimeter())
        print("square area:", DIMEN_2.area())
    
    else:
        print("Run Again!!")
        break
    
    o=input('Do u wish to continue n/y')
    if o.lower()=='n':
        break
    else:
        print('-_-')
        break
        
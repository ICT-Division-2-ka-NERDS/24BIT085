class Solid:
    def __init__(self, sh, dim):
        self.sh = sh
        self.dim = dim

    def surface_area(self):
        if self.sh == "sphere":
            r = self.dim['radius']
            return 4 * 3.14159 * r**2
        elif self.sh == "cylinder":
            r = self.dim['radius']
            h = self.dim['height']
            return 2 * 3.14159 * r * (r + h)
        elif self.sh == "cube":
            a = self.dim['side']
            return 6 * a**2
        elif self.sh == "cuboid":
            a = self.dim['length']
            b = self.dim['width']
            c = self.dim['height']
            return 2*(a*b+b*c+c*a)
        else:
            print(" Wrong Shape!!")
        
    def volume(self):
        if self.sh == "sphere":
            r = self.dim['radius']
            return (4/3) * 3.14159 * r**3
        elif self.sh == "cylinder":
            r = self.dim['radius']
            h = self.dim['height']
            return 3.14159 * r**2 * h
        elif self.sh == "cube":
            a = self.dim['side']
            return a**3
        elif self.sh == "cuboid":
            a = self.dim['length']
            b = self.dim['width']
            c = self.dim['height']
            return a*b*c
        else:
            print("Wrong Shape!!")

n='y'
while n=='y':
    print("Choose Shape [1.sphere, 2.cylinder, 3.cube, 4.cuboid]: ")
    c=int(input())
    if c==1:
        r = int(input('radius: '))
        solid=Solid("sphere", {"radius": r})
        print("Sphere Surface Area:", solid.surface_area())
        print("Sphere Volume:", solid.volume())

    elif c==2:
        r = int(input('radius: '))
        h = int(input('height: '))
        solid = Solid("cylinder", {"radius": r, "height": h})
        print("Cylinder Surface Area:", solid.surface_area())
        print("Cylinder Volume:", solid.volume())

    elif c==3:
        a = int(input('side: '))
        solid = Solid("cube", {"side": a})
        print("Cube Surface Area:", solid.surface_area())
        print("Cube Volume:", solid.volume())

    elif c==4:
        a = int(input('length: '))
        b = int(input('width: '))
        c = int(input('height: '))
        solid4 = Solid("cuboid", {"length": a, "width": b, "height": c})
        print("Cuboid Surface Area:", solid4.surface_area())
        print("Cuboid Volume:", solid4.volume())
    
    else:
        print("Run Again!!")
        break
    
    o=input('Do u wish to continue n/y')
    if o.lower()=='n':
        break
    else:
        print('-_-     bruhh')
        break
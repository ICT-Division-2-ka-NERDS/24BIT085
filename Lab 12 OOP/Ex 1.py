class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def set_n():
        r=int(input("Enter the real part: "))
        i=int(input("Enter the imaginary part: "))
        return Complex(r,i)
    def add(self,c2):
        return (self.r+c2.r,self.i+c2.i)
    def sub(self,c2):
        return (self.r-c2.r,self.i-c2.i)
    def mul(self,c2):
        return (self.r*c2.r-self.i*c2.i,self.i*c2.r+self.r*c2.i)
    def div(self,c2):
        return ((self.r*c2.r+self.i*c2.i)/(c2.r**2+c2.i**2),(self.i*c2.r-self.r*c2.i)/(c2.r**2+c2.i**2))
    def printN(self):
        print(self.r,'+i',self.i)

c1=Complex(4,5)
c2=Complex(3,8)
print(c1.add(c2))
print(c1.sub(c2))
print(c1.mul(c2))
print(c1.div(c2))
print(c1.printN())
print(c2.printN())
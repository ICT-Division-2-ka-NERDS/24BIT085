class String:
    def __init__(self,s):
        self.s=s
    
    def Concat(self,s2):
        try:
            if isinstance(s2,String):
                return self.s+s2.s
        except ValueError:
            print("Wwrong Datatype!!")

    def toLower(self):
        return self.s.lower()
    
    def toUpper(self):
        return self.s.upper()

s1=input("Enter a String: ")
s2=input("Enter another String: ")

st1=String(s1)
st2=String(s2)
print('s1+s2',st1.Concat(s2))
print('s2+s1',st2.Concat(s1))
print(st1.toLower(),st1.toUpper())
print(st2.toLower(),st2.toUpper())
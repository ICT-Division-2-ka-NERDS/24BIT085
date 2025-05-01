#1
a=3
b=4
if a>b:
    print(a,'is largest')
elif b>a:
    print(b,'is largest')
else:
    print('Equal')

#2
a=45
b=65
c=34
if a>b and a>c:
    print(a,'is largest')
elif b>c and b>a:
    print(b,'is largest')
elif c>a and c>b:
    print(c,'is largest')
else:
    print('Equal')

#3
a=10
if a%2==0:
    print('Even')
else:
    print('Odd')

#4
a=24
if a%10==0:
    print('Divisible by 10')

#5
age=int(input("Enter Age: "))
if age>18:
    print('Major')
else:
    print('Minor')

#6
a=int(input('Enter a number: '))
i=10
c=0
while a//i!=0:
    c+=1
print('Number of digits: ',c)

#7
a=int(input('Enter a year: '))
if a%4==0 and a%100==0:
    print('leap year')
else:
    print('not leap year')

#8
a=int(input('Enter 1st angle :'))
b=int(input('Enter 2nd angle :'))
c=int(input('Enter 3rd angle :'))
if a+b+c==180:
    print('Valid Triangle')
else:
    print('Not a valid triangle')

#9
a=int(input('enter a number: '))
print(a)

#10
l=10
b=5
peri=2*(l+b)
area=l*b
if peri>=area:
    print('area not greater then perimeter')
else:
    print('perimeter greater then area')

#11
a=[1,2]
b=[3,4]
c=[6,7]
mab=(a[1]-b[1])/(a[0]-b[0])
mbc=(c[1]-b[1])/(c[0]-b[0])
if mab==mbc:
    if (c[1]-2)==mbc(c[0]):
        print("All three lie on the same plane")
    else:
        print('Not in a line')

else:
    print('Not in a straight line')

#12
radius=float(input("Enter the value of radius"))
x=float(input("Enter the x coordinate of centre of circle"))
y=float(input("Enter the y coordinate of centre of circle"))
x1=float(input("Enter the x coordinate of the point you want to check"))
y1=float(input("Enter the y coordinate of the point you want to check"))
func=(x-x1)**2+(y-y1)**2-radius**2
print("The given point lies inside the circle") if(func<0) else print("The given point doesn't lies inside the circle")

#13
number_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
num=int(input("Enter the number:"))
if 0 <= num <= 19:
    print(number_words[num])
else:
    print("Number out of range!")

#14
sub1=float(input("Enter the marks in subject 1"))
sub2=float(input("Enter the marks in subject 2"))
sub3=float(input("Enter the marks in subject 3"))
total=sub1+sub2+sub3
average=total/3
if(sub1<=39 or sub2<=39 or sub3<=39 ):
    print("sorry you are failed!")

if(100<=sub1<=80):
    print("your grade in sub1 is O")
elif(70<=sub1<=79):
    print("your grade in sub1 is A+")
elif(60<=sub1<=69):
    print("your grade in sub1 is A")
elif(55<=sub1<=59):
    print("your grade in sub1 is B+")
elif(50<=sub1<=54):
    print("your grade in sub1 is B")
elif(45<=sub1<=49):
    print("your grade in sub1 is C")
elif(40<=sub1<=44):
    print("your grade in sub1 is P")
else:
    print("your grade in sub1 is F")

if(100<=sub2<=80):
    print("your grade in sub2 is O")
elif(70<=sub2<=79):
    print("your grade in sub2 is A+")
elif(60<=sub2<=69):
    print("your grade in sub2 is A")
elif(55<=sub2<=59):
    print("your grade in sub2 is B+")
elif(50<=sub2<=54):
    print("your grade in sub2 is B")
elif(45<=sub2<=49):
    print("your grade in sub2 is C")
elif(40<=sub2<=44):
    print("your grade in sub2 is P")
else:
    print("your grade in sub2 is F")
    

if(100<=sub3<=80):
    print("your grade in sub3 is O")
elif(70<=sub3<=79):
    print("your grade in sub3 is A+")
elif(60<=sub3<=69):
    print("your grade in sub1 is A")
elif(55<=sub3<=59):
    print("your grade in sub3 is B+")
elif(50<=sub3<=54):
    print("your grade in sub3 is B")
elif(45<=sub3<=49):
    print("your grade in sub3 is C")
elif(40<=sub3<=44):
    print("your grade in sub3 is P")
else:
    print("your grade in sub3 is F")
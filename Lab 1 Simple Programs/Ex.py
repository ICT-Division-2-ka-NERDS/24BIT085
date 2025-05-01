a=2
b=3

print(a+b) #1
print(b-a) #2
print(a*b) #3
print(a/b) #4
#6
c=1
print('Minutes =',b*60)
#7
d=120
print('Hours =',d/60)
#9
e=800
print('Dollars =',e/48)
#8
f=4
print('Ruppes =',f*48)
#10
g=9
print('Pounds =',(g/48)*70)
#11
grams=float(input("Enter the weight in grams:"))
kilograms=grams/1000
print("The weight in kgs is",kilograms)
#12
kilograms=float(input("Enter the weight in kilograms:"))
grams=kilograms*1000
print("The weight in grams is",grams)
#13
byte=int(input("Enter the no of bytes you want to covert"))
Kb=byte/1024
Mb=Kb/1024
Gb=Mb/1024
print("The bytes in Kb,Mb and Gb are",Kb,Mb,Gb,"respectively",sep=",")
#14
C=float(input("Enter temperature in celcius"))
F = (9/5*C) + 32
print("The temperature in farenheit is",F)
#15
F=float(input("Enter temperature in Farenheit"))
C = 5/9*(F-32)
print("The temperature in celcius is",C)
#16
P=float(input("Enter the principal amount"))
R=float(input("Enter the Rate of intrest"))
N=float(input("Enter the duration of loan in years"))
I = P*R*N/100
print("The Intrest amount is Rs",I)
#17
side=float(input("Enter the length of square"))
A=side**2
P=4*side
print("The Area of square is",A)
print("The Perimeter of square is",P)
#18
length=float(input("Enter the length of rectangle"))
width=float(input("Enter the width of rectangle"))
A=length*width
P=2*(length+width)
print("The Area of rectangle is",A)
print("The Perimeter of rectangle is",P)
#19
radius=float(input("Enter the radius of circle"))
A=22/7*radius**2
P=2*22/7*radius
print("The Area of circle is",A)
print("The Perimeter of circle is",P)
#20
base=float(input("Enter the base of triangle"))
height=float(input("Enter the height of triangle"))
A=base*height/2
print("The area of triangle is",A)
#21
gross_salary=float(input("Enter the gross salary"))
allowance=0.1*gross_salary
deduction=0.03*gross_salary
NetSalary=gross_salary + allowance - deduction
print("The Net salary is ",NetSalary)
#22
grosssales=float(input("enter ghrosssalary"))
netsales = grosssales - ( 0.1*grosssales)
print (netsales)
#23
m=int(input("enter m"))
p=int(input("enter p"))
c=int(input("enter c"))
avg=(m+p+c)/3
print(avg)
#24
a=int(input("Enter value of a"))
b=int(input("Enter value of b"))
a,b=b,a
print("The value of a after swap is",a)
print("The value of b after swap is",b)
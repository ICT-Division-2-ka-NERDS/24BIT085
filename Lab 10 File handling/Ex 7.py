'''7.	If an Employee object contains following details:
empcode, empname, Date of Joining, Salary
Write a program to serialize and deserialize this data.'''

import json as j
f1=open('C:\Users\Aryan Pal\AppData\Local\Programs\Python\Python310\Doc\24BIT085 Python (CP-II)\Lab 10 File handling\Employee.xlsx','w+')
f2=open('cpy','w+')
l=j.load(f1)
print(l)
j.dump(l,f2)
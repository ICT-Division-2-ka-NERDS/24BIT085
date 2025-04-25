s=input("Enter a string : ")
alp=0
nu=0
for i in s:
    if i.isalpha()==True:
        alp+=1
    elif i.isnumeric()==True:
        nu+=1
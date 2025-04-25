import cpf() from Ex 4.py as c:
a=''    #any file location
b=''    #any file location
c(a,b)

with open('b.txt','w+') as f:
    lines= f.readlines()
    for line in lines:
        line=line.lower()
        f.write(line)
    f.close()
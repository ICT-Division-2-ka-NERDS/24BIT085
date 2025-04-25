f=open('sample.txt','w+')
l=['a','an','the']
lines=f.readlines()
for i in lines:
    for j in i:
        if j in l:
            j==' '

f.close()
f=open('C:\Users\Aryan Pal\AppData\Local\Programs\Python\Python310\Doc\24BIT085 Python (CP-II)\Lab 10 File handling.csv','r')

st_data={}
lines=f.readlines()
for line in lines[1:]:
    l=line.strip().split(',')
    roll=l[0]
    name=l[1]
    sub1=int(l[2])
    sub2=int(l[3])
    sub3=int(l[4])
    subt=sub1+sub2+sub3
    st_data[roll]={
        'Name':name,
        'Sub1':sub1,
        'Sub2':sub2,
        'Sub3':sub3,
        'Total':subt,
    }

print(st_data)
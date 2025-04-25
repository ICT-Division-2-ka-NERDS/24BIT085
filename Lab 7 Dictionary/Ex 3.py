e={1:[1,23,20000],  2:[1,24,65500],  3:[2,54,76555],  4:[3,87,23545],  5:[2,55,87654],  6:[2,56,99999],  7:[3,88,12345],  8:[1,25,90076],  9:[2,57,87678],  10:[3,89,45632],  11:[3,90,12346]}
print(e)
l=e.values()
d1=[]
d2=[]
d3=[]   
for i in l:
    if i[0]==1:
        d1.append(i)
    elif i[0]==2:
        d2.append(i)
    elif i[0]==3:
        d3.append(i)

print("Maximum and Minimum of dept 1,2,3 are",max(d1),min(d1),max(d2),min(d2),max(d3),min(d3))
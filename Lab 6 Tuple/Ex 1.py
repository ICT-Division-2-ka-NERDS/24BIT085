stu=['g1','g2','g3','g4',('b1','b2','b3','b4'),'g5',('b5','b6'),'g6',]
g=0
b=0

for i in stu:
    if isinstance(i,str):
        g+=1
    elif isinstance(i,tuple):
        b+=len(i)

print("Number of boys and girls are, ",b,g,"respectively") 
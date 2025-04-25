def count_lower_upper(s):
    l,u=0,0
    a,b=1,1
    ld={}
    ud={}
    for i in s:
        if i.islower()==True:
            l+=1
            ld[a]=i
            a+=1
            
        elif i.isupper()==True:
            u+=1
            ud[b]=i
            b+=1
    
    print("Uppercase are -->",u,ud)
    print("Lowercase are -->",l,ld)

a=input("Enter a string: ")
count_lower_upper(a)
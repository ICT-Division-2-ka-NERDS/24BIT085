def cpf(a,b):

    l=[]

    with open('a.txt','r') as f:
        l=f.readlines()

    with open('b.txt','w') as g:
        for i in l:
            g=f.write(i)

    print("Copied")
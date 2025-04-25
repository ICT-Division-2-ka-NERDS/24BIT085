def convert(s):
    l=s.split(" ")
    print(set(s))

    w=[]
    for i in l:
        if i not in w:
            w.append(i)
        else:
            continue
    w.sort()
    print((' ').join(w))

st=input("Enter String: ")
convert(st)
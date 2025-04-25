lst = ['madam','Python',"malayalam",12321]
def ispali(s):
    i,j = 0, len(s) - 1

    ispali = True
    while i < j:
        if s[i] != s[j]:
            ispali=False
            break
        i += 1
        j -= 1

    if ispali:
        print("Yes") 
    else:
        print("No")

m=list(map(ispali,lst))
print(m)


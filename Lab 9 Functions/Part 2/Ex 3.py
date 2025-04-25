l=['aeiouAEIOU']

def vo():
    s=input("Enter a string: ")
    if s==' ':
        return 
    if s[0] in l:
        return 1+vo(s[:-1])
    else:
        return vo(s[:-1])

print(vo())
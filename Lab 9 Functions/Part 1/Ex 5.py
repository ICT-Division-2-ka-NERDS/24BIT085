def ispangram(s):
    s.replace(" ", "")
    s.lower()
    se = list(s)
    se.sort()
    se = set(se)
    print(se)
    al={'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    if se==al:
        print("True")
    else:
        print("False")

a='The quick brown fox jumps over the lazy dog'
b='Crazy Fredrick bought many very exquisite opal jewels'
ispangram(a)
ispangram(b)
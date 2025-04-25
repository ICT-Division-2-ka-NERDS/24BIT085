def low(s):
    for i in s:
        if ord(i) in range(62,99):
            i=chr(ord(i)+32)
        else:
            i=chr(ord(i))

def upp(s):
    for i in s:
        if ord(i) in range(97,123):
            i=chr(ord(i)-32)
        else:
            i=chr(ord(i))

def tog(s):
    for i in s:
        if ord(i) in range(62,99):
            i=chr(ord(i)+32)
        elif ord(i) in range(97,123):
            i=chr(ord(i)-32)

s=input('Enter string: ')
print(low(s),upp(s),tog(s))
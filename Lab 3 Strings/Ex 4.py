s1=input("Enter a string:")
s2=input("Enter another string:")

if len(s1)>len(s2):
    for s2 in s1:
        print(s1-s2)

elif len(s2)>len(s1):
    for s1 in s2:
        print(s2-s1)

else:
    print('')
def count_alpha_digits(s):
    n,a=0,0
    for i in s:
        if i.isnumeric==True:
            n+=1
        elif i.isalpha==True:
            a+=1
    d={'Number:':n,'Alphabet:':a}
    print(d)

st=input("Enter a string: ")
count_alpha_digits(st)
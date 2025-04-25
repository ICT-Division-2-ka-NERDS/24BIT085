def isplai(s):
    i,j=0,len(s)-1
    while i < j:
        if s[i] != s[j]:
            is_palindrome=False
            break
        i += 1
        j -= 1

        if is_palindrome==True:
            print("Yes") 
        else:
            print("No") 

st=input("Enter string: ")
isplai(st)
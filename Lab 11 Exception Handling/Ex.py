'''Write a program that receives an integer an input.
If a string is entered instead of an integer,
then report an error and give another chance to user to enter an integer.
Continue this process till correct input is supplied.'''

def intr():
    try:
        n=int(input("Enter an integer: "))
    except ValueError:
        print("Wrong data type !!")
        intr()
    else:
        return n

intr()
print("GG")
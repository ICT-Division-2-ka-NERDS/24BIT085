def fun():
    print('1')
def disp():
    print('2')
def msg():
    print('3')

lst=[fun,disp,msg]
for i in lst:
    i()
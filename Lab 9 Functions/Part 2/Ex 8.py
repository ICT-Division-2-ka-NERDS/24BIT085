def le(st):
    if st=='':
        return 0
    
    return 1+le(st[:-1])

s='asfsgsdfg'
print(le(s))
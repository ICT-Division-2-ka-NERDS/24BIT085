def create_array(x,y,z,n):
    return [[[n for k in range(z)] for j in range(y)] for i in range(x)]
print(create_array(3,4,5,10))

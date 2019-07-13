a_x = int(input('input x value for vector a:'))
a_y = int(input('input y value for vector a:'))
a_z = int(input('input z value for vector a:'))
b_x = int(input('input x value for vector b:'))
b_y = int(input('input y value for vector b:'))
b_z = int(input('input z value for vector b:'))
a =(a_x,a_y,a_z)
b =(b_x,b_y,b_z)


def dotproduct(a,b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]


print(dotproduct(a,b))

from vector import *

def bounding_box(A,B,C):
    coors = [(A.x, A.y), (B.x, B.y), (C.x, C.y)]

    xmin = 999999
    xmax = -999999
    ymin = 999999
    ymax = -999999

    for (x,y) in coors:
        if x < xmin:
            xmin = x
        if x > xmax:
            xmax = x
        if y < ymin:
            ymin = y
        if y > ymax:
            ymax = y

    return V3(xmin, ymin), V3(xmax, ymax)

def mul_externa(v0,v1):
    return(
        v0.y * v1.z - v0.z * v1.y,
        v0.z * v1.x - v0.x * v1.z,
        v0.x * v1.y - v0.y * v1.x
    )

def barycentric(A,B,C,P):
    cx,cy, cz = mul_externa(
                    V3(B.x - A.x, C.x - A.x, A.x-P.x),
                    V3(B.y - A.y, C.y - A.y, A.y-P.y) )


    if cz == 0:
        u = 0
        v = 0
        w = 0.0001
    else:
        u = cx/cz
        v = cy/cz
        w = 1-(u+v)

    return(w,v,u)


# print((1,2,3)@(1,2,3))
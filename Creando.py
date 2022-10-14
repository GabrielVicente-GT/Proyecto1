import Obj
import gl
from vector import *

def crear():



    scale_factor = (12,12,12)
    translate_factor = (500, 50,0)

    cube = Obj.Obj('Bigmax_White_OBJ.obj')

    for face in cube.faces:
        f1 = face[0][0] - 1
        f2 = face[1][0] - 1
        f3 = face[2][0] - 1

        v1 = transform_vertex(cube.vertices[f1], scale_factor, translate_factor)
        v2 = transform_vertex(cube.vertices[f2], scale_factor, translate_factor)
        v3 = transform_vertex(cube.vertices[f3], scale_factor, translate_factor)

        if len(face) == 4:

            f4 = face[3][0] - 1
            v4 = transform_vertex(cube.vertices[f4], scale_factor, translate_factor)

            gl.glLine2(v1[0][0], v1[0][1], v2[0][0],v2[0][1])
            gl.glLine2(v2[0][0], v2[0][1], v3[0][0],v3[0][1])
            gl.glLine2(v3[0][0], v3[0][1], v4[0][0],v4[0][1])
            gl.glLine2(v4[0][0], v4[0][1], v1[0][0],v1[0][1])

        elif len(face) == 3:


            gl.glLine2(v1[0][0], v1[0][1], v2[0][0],v2[0][1])
            gl.glLine2(v2[0][0], v2[0][1], v3[0][0],v3[0][1])
            gl.glLine2(v3[0][0], v3[0][1], v1[0][0],v1[0][1])

def transform_vertex(vertex, scale, translate):

    return [
        (
            (vertex[0] * scale[0]) + translate[0], #X.
            (vertex[1] * scale[1]) + translate[1] #Y.
        )
    ]

def transform_vertex_v3(vertex, scale, translate):

    return V3(
            (vertex[0] * scale[0]) + translate[0], #X.
            (vertex[1] * scale[1]) + translate[1], #Y.
            (vertex[2] * scale[2]) + translate[2] #Z.
    )

def crear_v3():


    # # kakashi
    # scale_factor = (9,9,100)
    # translate_factor = (500, 50,0)

    # cube = Obj.Obj('kakashi.obj')

    # Faraon
    scale_factor = (125,125,250)
    translate_factor = (525, 50,0)

    cube = Obj.Obj('faraon.obj')

    for face in cube.faces:
        f1 = face[0][0] - 1
        f2 = face[1][0] - 1
        f3 = face[2][0] - 1

        v1 = transform_vertex_v3(cube.vertices[f1], scale_factor, translate_factor)
        v2 = transform_vertex_v3(cube.vertices[f2], scale_factor, translate_factor)
        v3 = transform_vertex_v3(cube.vertices[f3], scale_factor, translate_factor)

        if len(face) == 4:

            f4 = face[3][0] - 1
            v4 = transform_vertex_v3(cube.vertices[f4], scale_factor, translate_factor)

            # gl.triangulocreado(v1,v2,v3)
            # gl.triangulocreado(v2,v3,v4)
            gl.triangulo_version_dos(v1,v2,v3)
            gl.triangulo_version_dos(v1,v3,v4)


        elif len(face) == 3:

            # gl.triangulocreado(v1,v2,v3)
            gl.triangulo_version_dos(v1,v2,v3)

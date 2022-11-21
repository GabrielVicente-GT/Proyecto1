#imports necesarios para poder cargar modelo, textura, vectores y realizar operaciones con matrices

from Object import *
import gl
from vector import *
from textures import *
import MatricesSimuladas as MatrizSimulada

#Funcion transform optimizada con matrices
def transform_vertex_robusto(vertex):
    renderizado = gl.RenderizadoFuncio()
    augmented_vertex = MatrizSimulada.matrix(([vertex[0]],[vertex[1]],[vertex[2]],[1]))
    transformed_vertex = renderizado.ViewPort @ renderizado.Projection @renderizado.View @ renderizado.Model @ augmented_vertex
    divisor = transformed_vertex.obtener_valor_unico(3,0)

    return V3(
        transformed_vertex.obtener_valor_unico(0,0)/divisor,
        transformed_vertex.obtener_valor_unico(1,0)/divisor,
        transformed_vertex.obtener_valor_unico(2,0)/divisor,
    )

#Funcion de creacion que utiliza textura objeto traslacion rotacion
def crear_robusto(Objeto, Textura,translate, scale, rotate):
    renderizado = gl.RenderizadoFuncio()
    renderizado.loadModelMatrix(translate,scale,rotate)
    cube = Obj(Objeto)
    if Textura == None:
        renderizado.texture = None
    else:
        renderizado.texture = Texture(Textura)

    for face in cube.faces:
        f1 = face[0][0] - 1
        f2 = face[1][0] - 1
        f3 = face[2][0] - 1

        v1 = transform_vertex_robusto(cube.vertices[f1])
        v2 = transform_vertex_robusto(cube.vertices[f2])
        v3 = transform_vertex_robusto(cube.vertices[f3])

        if len(face) == 4:

            f4 = face[3][0] - 1
            v4 = transform_vertex_robusto(cube.vertices[f4])


            ft1 = face[0][1] - 1
            ft2 = face[1][1] - 1
            ft3 = face[2][1] - 1
            ft4 = face[3][1] - 1
            vt1 = V3(*cube.tvertices[ft1])
            vt2 = V3(*cube.tvertices[ft2])
            vt3 = V3(*cube.tvertices[ft3])
            vt4 = V3(*cube.tvertices[ft4])

            fn1 = face[0][2] - 1
            fn2 = face[1][2] - 1
            fn3 = face[2][2] - 1
            fn4 = face[3][2] - 1
            vn1 = V3(*cube.tvertices[fn1])
            vn2 = V3(*cube.tvertices[fn2])
            vn3 = V3(*cube.tvertices[fn3])
            vn4 = V3(*cube.tvertices[fn4])

            gl.triangulo_version_dos_textura((v1,v2,v3),(vt1,vt2,vt3),(vn1,vn2,vn3))
            gl.triangulo_version_dos_textura((v1,v3,v4),(vt1,vt3,vt4),(vn1,vn3,vn4))


        elif len(face) == 3:

            ft1 = face[0][1] - 1
            ft2 = face[1][1] - 1
            ft3 = face[2][1] - 1
            vt1 = V3(*cube.tvertices[ft1])
            vt2 = V3(*cube.tvertices[ft2])
            vt3 = V3(*cube.tvertices[ft3])


            fn1 = face[0][2] - 1
            fn2 = face[1][2] - 1
            fn3 = face[2][2] - 1
            vn1 = V3(*cube.tvertices[fn1])
            vn2 = V3(*cube.tvertices[fn2])
            vn3 = V3(*cube.tvertices[fn3])

            gl.triangulo_version_dos_textura((v1,v2,v3),(vt1,vt2,vt3),(vn1,vn2,vn3))

#Permite obtener los color de los pixeles de una imagen
def fondo(Imagen):
    renderizado = gl.RenderizadoFuncio()
    renderizado.Fondo = Texture(Imagen)
    renderizado.framebuffer = renderizado.Fondo.pixels

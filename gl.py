#Archivo gl solicitado por SR1

#Importa el archivo proporcionado en clase
import  Render
from vector import *
import random
import extras as ex
from textures import *
from Object import *

#Funcion que recibe objeto y textura y devuelve textura con triangulos
def EscrituraSobreTextura(a,b):
        # """
    t = Texture(b)
    r = Render.Render(t.width,t.height)

    r.framebuffer = t.pixels

    cube = Obj(a)

    r.color_actual=ex.color(255,255,255)

    for face in cube.faces:
        if len(face) == 3:
            f1 = face[0][1] - 1
            f2 = face[1][1] - 1
            f3 = face[2][1] - 1

            vt1 = V3(cube.tvertices[f1][0]*t.width,cube.tvertices[f1][1]*t.height)
            vt2 = V3(cube.tvertices[f2][0]*t.width,cube.tvertices[f2][1]*t.height)
            vt3 = V3(cube.tvertices[f3][0]*t.width,cube.tvertices[f3][1]*t.height)

            r.line(vt1,vt2)
            r.line(vt2,vt3)
            r.line(vt3,vt1)
        if len(face) == 4:
            f1 = face[0][1] - 1
            f2 = face[1][1] - 1
            f4 = face[3][1] - 1
            f3 = face[2][1] - 1

            vt1 = V3(cube.tvertices[f1][0]*t.width,cube.tvertices[f1][1]*t.height)
            vt2 = V3(cube.tvertices[f2][0]*t.width,cube.tvertices[f2][1]*t.height)
            vt3 = V3(cube.tvertices[f3][0]*t.width,cube.tvertices[f3][1]*t.height)
            vt4 = V3(cube.tvertices[f4][0]*t.width,cube.tvertices[f4][1]*t.height)

            try:
                r.line(vt1,vt2)
                r.line(vt2,vt3)
                r.line(vt3,vt4)
                r.line(vt4,vt1)
            except:
                pass


    r.write('./t.bmp')

#Devuelve la instancia global de render valor estatico
def RenderizadoFuncio():
    global renderizado
    return renderizado

#Le asigna al renderizado global un render sencillo
def glInit():
    global renderizado
    renderizado = Render.Render(1,1)

#Crea la ventana con el ancho y la altura que el usuario desea
def glCreateWindow(width, height):
    global renderizado
    global widthFrame
    global heightFrame

    #Si el ancho y alto cumplen con la condicion de que sean valores
    #modulos de 4 se crea el render, de otrao forma, se adaptan para que sean
    #modulos de 4

    if width % 4 == 0 and height % 4 == 0:
        renderizado       = Render.Render(width,height)
    else:
        width   = width+width%4
        height  = height+height%4
        renderizado       = Render.Render(width,height)

    widthFrame  = width
    heightFrame = height

#Se crea la ventana donde se trabajara el punto
def glViewPort(x, y, width, height):
    global renderizado
    renderizado.set_color(Render.color(round(255*0), round(255*0), round(255*0)))

    #posicion desde la que se crea el view port
    #Se crea desde la esquina inferior izquierda
    global xPositionVP
    global yPositionVP

    #altura y ancho de viewport
    global widthVP
    global heightVP

    #si sobrepasan la altura y ancho de la ventana total se hace una reasignacion
    if  x > widthFrame or x < 0:
        x = widthFrame
    elif y > heightFrame or y < 0:
        y = heightFrame

    #posicion de inicio para el viewport
    xPositionVP = x
    yPositionVP = y


    #si sobrepasa la suma de la altura con la posicion el alto y ancho
    #respectivo, se hace una reasignacion
    if (xPositionVP + width) > widthFrame:
        width = widthFrame - xPositionVP
    if (yPositionVP + height) > heightFrame:
        height = heightFrame - yPositionVP

    widthVP     = width
    heightVP    = height

    #se renderiza el viewport
    for w in range (xPositionVP, xPositionVP + widthVP):
        for z in range (yPositionVP, yPositionVP + heightVP):
            renderizado.point(w, z)

#Se pinta todo el tablero de pixeles con el color predeterminado
def glClear():
    global renderizado
    renderizado.clear()

#Se cambia el color predeterminado
def glClearColor(r, g, b):
    global renderizado
    renderizado.set_color(Render.color(round(255*r), round(255*g), round(255*b)))

#Se dibuja un punto en las cordenadas especificas (respetando el viewport)
def glVertex(x, y):
    global puntomedidoX
    global puntomedidoY

    if y > 0:
        puntomedidoY = yPositionVP + round(heightVP/2) + round((heightVP/2)*y)
    elif y < 0:
        puntomedidoY = yPositionVP + round(heightVP/2) - round((heightVP/2)*(-y))
    elif y == 0:
        puntomedidoY = yPositionVP + round(heightVP/2)

    if x > 0:
        puntomedidoX = xPositionVP + round(widthVP/2) + round((widthVP/2)*(x))
    elif x < 0:
        puntomedidoX = xPositionVP + round(widthVP/2) - round((widthVP/2)*(-x))
    elif x == 0:
        puntomedidoX = xPositionVP + round(widthVP/2)

    # for xx in range(10):
    #     for yy in range (10):
    # # print(puntomedidoX,puntomedidoY)
    #         renderizado.point(923+xx,100+yy)
    if puntomedidoY == (yPositionVP +heightVP):

        puntomedidoY = puntomedidoY -1

    if puntomedidoX == (xPositionVP +widthVP):

        puntomedidoX = puntomedidoX -1
    renderizado.point(puntomedidoX,puntomedidoY)

#Se cambia el color con el que se dibuja el punto
def glColor(r, g, b):
    global renderizado
    renderizado.set_color(Render.color(round(255*r), round(255*g), round(255*b)))

#Se escribe el archivo
def glFinish(nombre):
    global renderizado
    renderizado.write(nombre)

#Se calcula el valor convertido e escala de 1 a la altura del bmp
def escala(unitario, tipo):
    #Valores para operar
    devolucion = 1
    a = 0
    b = 0

    #Dependiendo si se calcula un punto respecto a la altura o el ancho
    if tipo == "W":
        a = widthVP
        b = xPositionVP
    elif tipo == "H":
        a = heightVP
        b = yPositionVP

    #El caso dependiendo si esta en el centro del eje, a la izquierda o a la derecha
    if unitario > 0:
        devolucion = b + round(a/2) + round((a/2)*(unitario))
    elif unitario < 0:
        devolucion = b + round(a/2) - round((a/2)*(-unitario))
    elif unitario == 0:
        devolucion = b + round(a/2)

    #Si el valor calculado es igual al limite se le resta un pixel para que quede dentro del viewport
    if devolucion == (a + b):
        devolucion = devolucion -1

    return devolucion

#Funcion linea mejorada
def glLine2(v1,v2):
    global renderizado

    y1 = round(v2.y)
    x1 = round(v2.x)
    y0 = round(v1.y)
    x0 = round(v1.x)

    dy,dx= abs(y1 - y0),abs(x1 - x0)

    pendiente = dy > dx
    if pendiente:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dy,dx = abs(y1 - y0),(x1 - x0)

    limitation = dx
    compensation = 0

    y = y0
    for x in range(x0,1+x1):
        if pendiente:
            renderizado.point(y, x)
        else:
            renderizado.point(x, y)

        compensation += dy * 2

        if compensation >= limitation:
            y += 1 if y0 < y1 else -1
            limitation += dx * 2

#Funcion triangulo con textura y shader
def triangulo_version_dos_textura(verices,vertices_de_textura = (),vertices_de_n = ()):
    global renderizado

    A,B,C = verices
    nA,nB,nC = vertices_de_n
    tA,tB,tC = vertices_de_textura

    Bmin, Bmax = ex.bounding_box(A,B,C)
    Bmin.round()
    Bmax.round()

    for x in range(Bmin.x, Bmax.x+1):
        for y in range(Bmin.y, Bmax.y+1):
            w,v,u = ex.barycentric(A,B,C,V3(x,y))
            if(w < 0 or v < 0 or u<0):
                continue

            z = C.z*u + B.z * v + A.z * w  +0

            if x<len(renderizado.zbuffer) and y<len(renderizado.zbuffer[0]) and renderizado.zbuffer[x][y] < z and x > 0 and y > 0:

                renderizado.zbuffer[x][y] = z
                renderizado.set_color(renderizado.Shader(renderizado, vertices = (A,B,C), bar = (w,u,v),texture_coords=(tA,tB,tC),normals=(nA,nB,nC)))
                renderizado.point(x,y)

#Archivo gl solicitado por SR1

#Importa el archivo proporcionado en clase
import  Render
from vector import *
import random
import extras as ex

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
def glFinish():
    global renderizado
    renderizado.write('a.bmp')

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

def glLine(x0,y0,x1,y1):
    global renderizado
    #Se cambia el color para tener contraste
    renderizado.set_color(Render.color(round(255*1), round(255*1), round(255*1)))

    #Se realiza la conversión utilizando la funcion escala para convertir valores entre -1 y 1
    #A valores en pixeles

    x0 = escala(x0,"W")
    y0 = escala(y0,"H")
    x1 = escala(x1,"W")
    y1 = escala(y1,"H")

    #Se calcula la pendiente "diferenca" entre y1 y y0 al igual que con sus respectivas x
    dy,dx= abs(y1 - y0),abs(x1 - x0)

    #Si la pendiente es "mas inclinada" verticalmente
    pendiente = dy > dx
    if pendiente:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    #Y si es inversa
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    #Se calcula nuevamente la pendiente
    dy,dx = abs(y1 - y0),abs(x1 - x0)

    #Tomando en cuenta que dy implica el desplezamaiento
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

def glLine2(x0,y0,x1,y1):
    global renderizado
    #Se cambia el color para tener contraste
    renderizado.set_color(Render.color(round(255*0), round(255*0.62), round(255*0.1)))

    #Se realiza la conversión utilizando la funcion escala para convertir valores entre -1 y 1
    #A valores en pixeles

    x0 = round(x0)
    y0 = round(y0)
    x1 = round(x1)
    y1 = round(y1)

    #Se calcula la pendiente "diferenca" entre y1 y y0 al igual que con sus respectivas x
    dy,dx= abs(y1 - y0),abs(x1 - x0)

    #Si la pendiente es "mas inclinada" verticalmente
    pendiente = dy > dx
    if pendiente:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    #Y si es inversa
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    #Se calcula nuevamente la pendiente
    dy,dx = abs(y1 - y0),(x1 - x0)

    #Tomando en cuenta que dy implica el desplezamaiento
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

def glLine2(v1,v2):
    global renderizado
    #Se cambia el color para tener contraste

    #Se realiza la conversión utilizando la funcion escala para convertir valores entre -1 y 1
    #A valores en pixeles

    x0 = round(v1.x)
    y0 = round(v1.y)
    x1 = round(v2.x)
    y1 = round(v2.y)

    #Se calcula la pendiente "diferenca" entre y1 y y0 al igual que con sus respectivas x
    dy,dx= abs(y1 - y0),abs(x1 - x0)

    #Si la pendiente es "mas inclinada" verticalmente
    pendiente = dy > dx
    if pendiente:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    #Y si es inversa
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    #Se calcula nuevamente la pendiente
    dy,dx = abs(y1 - y0),(x1 - x0)

    #Tomando en cuenta que dy implica el desplezamaiento
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

#Algoritmo simple
def triangulocreado(A,B,C):

    global renderizado

    renderizado.set_color(Render.color(round(255*0), round(255*0.62), round(255*0.1)))
    # glLine2(A,B)
    # glLine2(B,C)
    # glLine2(C,A)

    A.round()
    B.round()
    C.round()

    if A.y > B.y:
        A,B = B,A
    if A.y > C.y:
        A,C = C,A
    if B.y > C.y:
        B,C = C,B

    renderizado.set_color(Render.color(round(random.randint(0,255)), random.randint(0,255), random.randint(0,255)))

    dx_ac = C.x - A.x
    dy_ac = C.y - A.y

    if dy_ac == 0:
        return

    m_ac = dx_ac/dy_ac

    dx_ab = B.x - A.x
    dy_ab = B.y - A.y

    if dy_ab != 0:
        m_ab = dx_ab/dy_ab

        for y in range(A.y, B.y+1):
            xi = round(A.x - m_ac * (A.y-y))
            xf = round(A.x - m_ab * (A.y-y))

            if xi>xf:
                xi,xf = xf,xi
            for x in range(xi,xf + 1):
                renderizado.point(x,y)

    dx_bc = C.x - B.x
    dy_bc = C.y - B.y



    if dy_bc != 0:
        m_bc = dx_bc/dy_bc
        for y in range(B.y, C.y+1):
            xi = round(A.x - m_ac * (A.y-y))
            xf = round(B.x - m_bc * (B.y-y))

            if xi>xf:
                xi,xf = xf,xi
            for x in range(xi,xf + 1):
                renderizado.point(x,y)

def triangulo_version_dos(A,B,C):
    global renderizado

    # colorA = (255,0,0)
    # colorB = (0,255,0)
    # colorC = (0,0,255)

    luz = V3(0,0,1)
    normal_triangulo =  (C-A) * (B-A)
    # # print("A> ",A)
    # # print("B> ",B)
    # # print("C> ",C)
    # # print("C-A> ",(C-A))
    # # print("B-A> ",(B-A))
    # # print("all> ",(C-A) * (B-A))
    i = luz.normalize() @ normal_triangulo.normalize()
    # print(i)
    # # print(normal_triangulo.normalize().x,normal_triangulo.normalize().y,normal_triangulo.normalize().z)
    if i < 0:
        return

    gris = 255*i

    Bmin, Bmax = ex.bounding_box(A,B,C)
    Bmin.round()
    Bmax.round()

    # print(Bmin.x, Bmin.y, Bmax.x,Bmax.y)
    for x in range(Bmin.x, Bmax.x+1):
        for y in range(Bmin.y, Bmax.y+1):
            w,v,u = ex.barycentric(A,B,C,V3(x,y))
            if(w < 0 or v < 0 or u<0):
                continue

            # renderizado.set_color(Render.color(round(colorA[0] * w) + round(colorB[0] * v +colorC[0] * u),round(colorA[1] * w) + round(colorB[1] * v +colorC[1] * u),round(colorA[2] * w) + round(colorB[2] * v +colorC[2] * u)))
            renderizado.set_color(Render.color(round(gris),round(gris) ,round(gris)))

            z = A.z * w + B.z * v + C.z*u

            if renderizado.zbuffer[x][y] < z:
                renderizado.zbuffer[x][y] = z
                renderizado.point(x,y)

def zbuffer():
    print(renderizado.zbuffer[0])

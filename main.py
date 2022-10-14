#Gabriel Alejandro Vicente Lorenzo
#SR1 UVG

#Se importan los metodos solicitados por el ejercicios
import gl
import Creando
from vector import *

gl.glInit()
#Se crea la Ventana (Que renderiza a.bmp)
gl.glCreateWindow(1024,1024)

#Cambia el color con el que trabaja Clear
gl.glClearColor(0,0,0)

#Pinta TODOELMAPA de bits de un mismo color
gl.glClear()

# Creando.crear()
Creando.crear_v3()

#Trinagulos

# gl.triangulo_version_dos(V3(10,70), V3(50,160), V3(70,80))
# gl.triangulocreado(V3(180,50), V3(150,1), V3(70,180))
# gl.triangulocreado(V3(150,150), V3(120,160), V3(130,180))

#Se crea el ViewPort (Ventana mas pequeña que se dibuja apartir de x y y)
# gl.glViewPort(100, 100, 824, 824)

#Se pinta la linea
# gl.glLine(-1,-1,0,1)

#Casa
# gl.glLine(0,0.025,0,0.05)
# gl.glLine(0,0.025,0.57,0.08)
# gl.glLine(0.57,0.08,0.57,0.1)
# gl.glLine(0.57,0.1,0.33,0.4)
# gl.glLine(0.33,0.4,-0.28,0.35)
# gl.glLine(-0.28,0.35,-0.57,0.1)
# gl.glLine(-0.57,0.1,0,0.05)
# gl.glLine(-0.57,0.1,-0.57,0.075)
# gl.glLine(-0.57,0.075,0,0.025)
# gl.glLine(0,0.05,0.33,0.4)
# gl.glLine(0,0.025,0,-0.33)
# gl.glLine(0,-0.33,0.53,-0.22)
# gl.glLine(-0.53,-0.16,0,-0.33)
# gl.glLine(-0.53,-0.16,-0.53,0.070)
# gl.glLine(0.53,-0.22,0.53,0.072)
# gl.glLine(0.53,-0.22,0.53,0.072)

# square = [
#     (-0.6,-0.6),
#     (0,-0.6),
#     (0,0),
#     (-0.6,0)
# ]

# last_point = square[-1]
# for point in square:
#     gl.glLine(*last_point,*point)
#     last_point = point

# print(o.lines)

#Escribe el archivo .bmp
gl.zbuffer()
gl.glFinish()

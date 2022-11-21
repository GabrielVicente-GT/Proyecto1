#Gabriel Alejandro Vicente Lorenzo 20498
#Proyecto 1

#Se importan los metodos solicitados por el ejercicios
import gl
import Creando
from vector import *
from extras import *

gl.glInit()
#Se crea la Ventana 1024*1024
gl.glCreateWindow(1024,1024)

#Se cambia la vista de camara
renderizado = gl.RenderizadoFuncio()
renderizado.lookAt(V3(0,0,10), V3(0,0,0), V3(0,1,0))

#Se carga un fondo para la imagen
Creando.fondo('./Fondos/FondoLago.bmp')

#Se carga un shader que carga intensidad sin cambios
renderizado.Shader = shaders

#Modelos con transformaciones, cambios de escala, rotaciones
Creando.crear_robusto('./Objts/Gato.obj','./Textrs/Gato.bmp',translate = (0,0.25,0),scale = (0.007,0.007,0.007),rotate = (-pi/3,pi/20,-pi/4))
Creando.crear_robusto('./Objts/Pato.obj','./Textrs/Pato.bmp',translate = (0.3,-0.8,-0.5),scale = (0.01,0.01,0.01),rotate = (-pi/3,0,pi/4))
Creando.crear_robusto('./Objts/snake.obj','./Textrs/snake.bmp',translate = (-0.8,-0.5,0),scale = (0.011,0.011,0.011),rotate = (-pi/3,0,pi))

#Se cambia de shader, intensidad variada con color azul fijo
renderizado.Shader = shader_arcoiris

#Modelo con transformaciones, cambios de escala, rotaciones
Creando.crear_robusto('./Objts/Ave.obj','./Textrs/Ave.bmp',translate = (0.7,0.2,0),scale = (0.03,0.03,0.03),rotate = (-pi/3,0,pi/2))

#Se cambia de shader, intensidad variada con color rojo fijo
renderizado.Shader = shader_rosado

#Modelo con transformaciones, cambios de escala, rotaciones
Creando.crear_robusto('./Objts/Delfin.obj','./Textrs/Delfin.bmp',translate = (0,-0.4,0),scale = (0.002,0.002,0.002),rotate = (-pi/3,0,-pi/4))

#Se escribe el proyecto
gl.glFinish('Proyecto_1_20498.bmp')

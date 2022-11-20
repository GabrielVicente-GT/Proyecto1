#Import que viene default con python
from math import *

#Clase vector de la clase
class V3(object):
    def __init__(self,x,y = 0,z = 0,w=1):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

#Valores sin decimales
    def round(self):
        self.x = round(self.x)
        self.y = round(self.y)
        self.z = round(self.z)

#Opearcion suma
    def __add__(self, other):
        return V3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

#Resta
    def __sub__(self, other):
        return V3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

#Multiplicacion
    def __mul__ (self, other):
        if (type(other) == int or type(other) == float):
            return V3(
                self.x * other,
                self.y * other,
                self.z * other
            )
        return V3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

#Multiplicacion@
    def __matmul__(self,other):
        return self.z*other.z + self.x*other.x + self.y*other.y

#Largo
    def len(self):
        return(self.z**2 + self.y**2  +self.x**2)**(1/2)

#Vector normal
    def normalize(self):
        try:
            return self*(1/self.len())
        except:
            return V3(-1,-1,-1)

#String
    def __str__(self):
        cadena = str(self.x)+" "+str(self.y)+" "+str(self.z)+" "
        return cadena
'''Referencia tomada de https://www.youtube.com/watch?v=IbzzK9PtFBE en el cual se explica
cómo multiplicar dos matrices'''

#Clase matrix que permite realizar matrices y operarlas sin numpy
class matrix(object):

    #Inicia con un valor dado en la propiedad analizar
    def __init__(self, X):
        self.analizar = X

    #Se obtiene un valor de la matriz
    def obtener_valor_unico(self, x, y):
        return self.analizar[x][y]

    #Para dejar el mismo operador que numpylibrary se utiliza matmul y se aplica la logica de multiplicacion
    #Comentario de arriba sirve de punto de referencia
    def __matmul__(self, other):
        resultado_operado = []
        for largo_inicial in range(len(self.analizar)):
            resultado_operado.append([])
            for largo_matriz_dos in range(len(other.analizar[0])):
                resultado_operado[largo_inicial].append(0)
        for largo_inicial in range(len(self.analizar)):
            for largo_matriz_dos in range(len(other.analizar[0])):
                for largo_total_matriz in range(len(other.analizar)):
                    resultado_operado[largo_inicial][largo_matriz_dos]+=other.analizar[largo_total_matriz][largo_matriz_dos]*self.analizar[largo_inicial][largo_total_matriz]

        return matrix(resultado_operado)

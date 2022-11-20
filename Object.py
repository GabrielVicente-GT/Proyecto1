#Clase que permite leer las propiedades del objeto
class Obj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()
            self.vertices = []
            self.tvertices = []
            self.nvertices = []
            self.faces = []
            i=1
            for line in self.lines:

                if not line or line.startswith("#"):
                    continue

                prefix, value =  line.split(' ', 1)
                i+=1
                #Lee los v y los agrega a vertices
                if prefix == 'v':
                    self.vertices.append(list(map(float, value.split(' '))))
                #Lee los vt y los agrega a tvertices
                elif prefix == 'vt':
                    self.tvertices.append(list(map(float, value.split(' '))))
                #Lee los vn y los agrega a nvertices
                elif prefix == 'vn':
                    self.nvertices.append(list(map(float, value.split(' '))))
                #Lee los f y los agrega a faces
                elif prefix == 'f':
                    self.faces.append([list(map(int , face.split('/'))) for face in value.split(' ')])


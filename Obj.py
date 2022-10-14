
class Obj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()
        self.vertices = []
        self.faces = []
        i=1
        for line in self.lines:

            if not line or line.startswith("#"):
                continue
            # print("linea: ", line,"linea: ",i)
            prefix, value =  line.split(' ', 1)
            # print("prefix", prefix,"value",value)
            i+=1
            if prefix == 'v':
                self.vertices.append(list(map(float, value.split(' '))))
            if prefix == 'f':
                try:
                    self.faces.append([list(map(int , face.split('/'))) for face in value.split(' ')])
                except:
                    self.faces.append([list(map(int , face.split('//'))) for face in value.split(' ')])


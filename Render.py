#Render proporcionado en clase para trabajar eficientemente
import struct
def char(c):
    #1 byte

    return struct.pack('=c', c.encode('ascii'))

def word(w):
    #2bytes

    return struct.pack('=h', w)

def dword(d):
    #4bytes

    return struct.pack('=l', d)


def color(r,g,b):
    return bytes([b, g, r])

BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)
BLUE  = color(51, 114, 176)
ORANGE = color(243, 156, 18)
RED = color(255, 0, 0)

class Render(object):

    def __init__(self, width, height):
            self.width  = width
            self.heigth = height
            self.color_actual   =  BLACK



            # self.framebuffer = []
            self.clear()

    def clear(self):
        self.framebuffer = [
            [ self.color_actual for x in range(self.width)]
            for y in range(self.heigth)
        ]
        self.zbuffer = [
            [ -999999 for x in range(self.width)]
            for y in range(self.heigth)
        ]

    def write(self, filename):
        f = open(filename, 'bw')

        #pixel header

        f.write( char('B'))
        f.write( char('M'))
        f.write( dword(14 + 40 + self.width * self.heigth * 3))
        f.write( word(0))
        f.write( word(0))
        f.write( dword(14+40))

        #info header

        f.write( dword(40))
        f.write( dword(self.width))
        f.write( dword(self.heigth))
        f.write( word(1))
        f.write( word(24))
        f.write( dword(0))
        f.write( dword(self.width*self.heigth*3))
        f.write( dword(0))
        f.write( dword(0))
        f.write( dword(0))
        f.write( dword(0))

        # pixel data

        for x in range(self.heigth):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])

        f.close()

    def point(self, x, y):
        self.framebuffer[y][x] = self.color_actual

    def point2(self, x, y):
        self.zbuffer[y][x] = self.color_actual

    def set_color(self, color):
        self.color_actual = color




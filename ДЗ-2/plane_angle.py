import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z        
        
    def __sub__(self, no):
        x = self.x - no.x
        y = self.y - no.y
        z = self.z - no.z   
        return Point(x, y, z)
        
    def dot(self, no):
        """скалярное произведение"""
        x = self.x * no.x
        y = self.y * no.y
        z = self.z * no.z
        return x + y + z

    def cross(self, no):
        """векторное произведение"""
        x = self.y * no.z - self.z * no.y
        y = self.z * no.x - self.x * no.z
        z = self.x * no.y - self.y * no.x
        return Point(x, y, z)
        
    def absolute(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

def plane_angle(a : Point, b : Point, c : Point, d : Point) -> float:
    ab = b - a
    bc = b - c
    cd = d - c
    
    x = ab.cross(bc)
    y = bc.cross(cd)

    cosPhi = (x.dot(y) / (x.absolute() * y.absolute()))

    rad = math.acos(cosPhi)    
    
    return math.degrees(rad)

if __name__ == '__main__':
    a = Point(0, 0, 0)
    b = Point(1, 1, 1)
    c = Point(1, 0, 0)
    d = Point(0, 0, 1)

    print(plane_angle(a, b, c, d))
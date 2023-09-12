import numpy as np

class Point:  
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    @property
    def r(self):
        self._r = np.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        return self._r

    def __str__(self):
        return f'({self.x},{self.y},{self.z})'
    
    def __eq__(self, other):
        return self._r == other.r
    
    def __lt__(self, other):
        return self._r < other.r
    
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y, self.z+other.z)
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def asdict(self):
        return {'x':self.x, 'y':self.y, 'z':self.z}

p = Point(1, 2, 3)
print(p)
print(p+Point(4,5,6))
p.__iadd__(Point(6,7,8))
print(p)
print(p.r)

p2 = Point(4,5,6)
print(p2.r)
print(p > p2)

print(p.asdict())
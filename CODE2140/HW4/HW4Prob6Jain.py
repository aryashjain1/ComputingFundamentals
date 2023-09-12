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


class Sphere:
    def __init__(self, r, center = Point(0,0,0)):
        self.radius = r
        self.center = center
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, v):
        if v > 0:
            self._radius = v
        else:
            raise ValueError(f'The inputted radius {v} is invalid. Make sure it is a positive, non-zero value.')
    
    @property
    def vol(self):
        return (4/3) * np.pi * (self._radius ** 3)
    
    def __str__(self):
        return f'The volume of the sphere centered at ({self.center.x}, {self.center.y}, {self.center.z}) with a radius of {self._radius} is equal to {self.vol}.'

class CenteredSphere(Sphere):
    def __init__(self, r):
        super().__init__(r, Point(0,0,0))
    
    def __str__(self):
        return f'The volume of the sphere centered at the origin with a radius of {self._radius} is equal to {self.vol}.'
    

spheres = []
for _ in range(4):
    c =Point(np.random.randint(0,6), np.random.randint(0,6), np.random.randint(0,6))
    s = Sphere(np.random.randint(1, 6), c)
    spheres.append(s)

centered_spheres = [CenteredSphere(np.random.randint(5, 11)), CenteredSphere(np.random.randint(5, 11))]

spheres += centered_spheres

for sphere in spheres:
    print(sphere)

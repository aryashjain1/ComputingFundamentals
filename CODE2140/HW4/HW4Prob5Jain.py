import matplotlib.pyplot as plt
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


class Circle:
    def __init__(self, r, center=Point(0, 0)):
        self.center = center
        self.r = r
    
    @property
    def r(self):
        return self._r
    
    @r.setter
    def r(self, v):
        if v < 0:
            raise ValueError(f'The inputted radius {v} is invalid. Make sure it is a positive, non-zero value.')
        else:
            self._r = v

    def draw(self):
        x_min, x_max = self.center.x - self._r, self.center.x + self.r
        x = np.arange(x_min, x_max, 0.01)
        y = self.center.y + np.sqrt(self._r ** 2 - (x - self.center.x) ** 2)
        y2 = self.center.y - np.sqrt(self._r ** 2 - (x - self.center.x) ** 2)
        plt.figure()
        plt.plot(x, y, 'r', x, y2, 'r')
        plt.grid()
        plt.title("The drawn circle")
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend([f'(x - {self.center.x})^2 + (y - {self.center.y})^2 = {self._r ** 2}'])
        plt.text(1,4,f'(x - {self.center.x})^2 + (y - {self.center.y})^2 = {self._r ** 2}')
        plt.show()

c = Circle(np.random.randint(1, 11), Point(np.random.randint(0, 6), np.random.randint(0, 6)))
print(f'Radius: {c.r}\tCenter:{c.center}')
c.draw()

import math

class Cuboid:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
    
    def GetVolume(self):
        return round(self.width * self.height * self.depth, 2)
    
    def GetSurfaceArea(self):
        return round(2 * (self.width*self.height + self.height*self.depth + self.depth*self.width), 2)

class Cube(Cuboid):
    def __init__(self, sideLength):
        super().__init__(sideLength, sideLength, sideLength)

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def GetVolume(self):
        return round(math.pi * self.radius**2 * self.height, 2)
    
    def GetSurfaceArea(self):
        return round(2 * math.pi * self.radius * (self.radius + self.height), 2)

class Prism:
    def __init__(self, sideLength, faces, height):
        self.sideLength = sideLength
        self.faces = faces
        self.height = height
    
    def GetVolume(self):
        return round(self.faces * self.sideLength**2 * self.height / (4 * math.tan(math.pi/self.faces)), 2)
    
    def GetSurfaceArea(self):
        return round(2 * self.faces * self.sideLength * self.height + self.faces * self.sideLength**2 / (2 * math.tan(math.pi/self.faces)), 2)
class IShape:
    def draw(self): pass

class Circle(IShape) :
    def draw(self):
        print("Circle")

class Squre(IShape):
    def draw(self):
        print("Squre")

from factory.Shape import IShape, Circle, Squre
class ShapeFactory:
    @staticmethod
    def getShape(type) :
        if type == 'circle':
            return Circle()
        if type == 'squre':
            return Squre();
        assert 0, 'could not find the shape %s' % (type)

f = ShapeFactory()
Circle c = f.getShape('circle')
c.draw()

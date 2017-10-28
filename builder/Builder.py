from Car import Car, Body, Wheel, Engine
class IBuilder:
    def getWheel(self) : pass
    def getEngine(self) : pass
    def getBody(self) : pass

class JeepBuilder(IBuilder):
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def getBody(self):
        body = Body()
        body.shape = "SUV"
        return body

from director import Director
d = Director()
d.setBuilder(JeepBuilder())
c = d.getCar()

c.spec()

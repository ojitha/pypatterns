class Car(object):
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def setBody(self, body):
        self.__body = body

    def attachWheel (self, wheel):
        self.__wheels.append(wheel)

    def setEngine(self, engine):
        self.__engine = engine

    def spec(self):
        print("body: {}".format(self.__body.shape))
        print("engine: {}".format(self.__engine.horsepower))
        for i in self.__wheels:
            print ("wheel {} of size {}".format(i,i.size))

class Wheel:
    size = None

class Engine:
    horsepower = None

class Body:
    shape = None

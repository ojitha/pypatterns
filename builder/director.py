from Car import Car, Body, Wheel, Engine
class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getCar(self):
        car = Car()
        body = self.__builder.getBody()
        car.setBody(body)

        car.setEngine(self.__builder.getEngine())

        i = 0
        while i < 0:
            car.attachWheel(self.__builder.getWheel())
            i += 1

        return car

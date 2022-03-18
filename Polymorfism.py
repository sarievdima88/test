"""
# класс Auto
class Auto:
    def auto_start(self, param_1, param_2=None):
        if param_2 is not None:
            print(param_1 + param_2)
        else:
            print(param_1)
a = Auto()
a.auto_start(50)
a = Auto()
a.auto_start(10, 20)
"""
# класс Transport
class Transport:
    def show_info(self):
        print("Родительский метод класса Transport")


# класс Auto, наследующий Transport
class Auto(Transport):
    def show_info(self):
        print("Родительский метод класса Auto")


# класс Bus, наследующий Transport
class Bus(Transport):
    def show_info(self):
        print("Родительский метод класса Bus")

t = Transport()
t.show_info()

a = Auto()
a.show_info()

b = Bus()
b.show_info()

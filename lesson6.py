class Transport:
    # Атрибуты Объекта
    def __init__(self, name, model, year):
        self.name = name
        self._model = model
        self.__year = year
      # Методы класса
    def on_start(self, speed):
         print(f"Car {self.name} go with {speed}")

 #   def on_stop(self):
         print("Stop")
class Auto(Transport):
    def __init__(self, name, model, year, pass_):
        super().__init__(name, model, year)
        self.pass_ = pass_
    def drift(self):
        print("Vggggg!")



auto_1 = Auto("Mercedez", "C550", 2021, 5)
auto_1.on_start(100)
auto_1.drift()
print(auto_1.pass_)
#auto_1.name = "Toyota"
#print(auto_1.name)

#auto_2 = Auto("Mazda", "CX6",)
#print(auto_2.auto_count)
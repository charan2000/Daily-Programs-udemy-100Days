class Animal:
    def __init__(self):
        self.eyes = 2
        self.hearts = 1
        print("Animal Class")

    def breath(self):
        print("Ïn air, Out air")

class Fish(Animal):
    def __init__(self):
        print("Fish Class")

class Mamals(Animal):
    def __init__(self):
        super().__init__()
        print("Mamal Class")


jellyFh = Fish()
jellyFh.breath()
women = Mamals()


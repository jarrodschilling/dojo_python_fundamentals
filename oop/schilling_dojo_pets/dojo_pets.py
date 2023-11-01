from pets import Pets
from ninjas import Ninja


class Dog(Pets):
    def __init__(self, name, tricks):
        super().__init__(name, "dog", tricks)
        # self.noise = "bark"
    
    def sleep(self):
        super().sleep()

    def eat(self):
        super().eat()

    def play(self):
        super().play()

    def noise(self):
        super().noise("bark")


kylo = Dog("kylo", "jumps")
loki = Pets("loki", "Dog", "lazy")
carl = Ninja("Carl", "Thomas", "Bones", "Kibbles", kylo)

carl.feed().walk().bathe().feed().feed()
print(kylo.energy)


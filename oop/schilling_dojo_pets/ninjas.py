from pets import Pets
class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print(f"{self.first_name} is walking {self.pet.name}")
        self.pet.play()
        return self
    
    def feed(self):
        print(f"{self.first_name} is feeding {self.pet.name} a {self.treats}")
        self.pet.eat()
        return self
    
    def bathe(self):
        print(f"{self.first_name} is bathing {self.pet.name}")
        self.pet.noise()
        return self
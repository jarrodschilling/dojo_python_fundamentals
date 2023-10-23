class User:
    def __init__(self, name, age, hair):
        self.name = name
        self.age = age
        self.hair = hair

    def my_name_is(self):
        print(f"Hey my name is {self.name}")

jarrod = User("Jarrod", 38, "long")

jarrod.my_name_is()
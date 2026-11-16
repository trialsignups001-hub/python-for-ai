class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

class Dog(Animal):

    def __init__(self, name, breed, color):
        super().__init__(name,breed)
        self.color = color
    
    def description(self):
        print(f"My dog name is {self.name} and it is a {self.breed} and it is {self.color} in color")


pet = Dog("Tommy","Golden Retreiver", "Golden")
pet.description()
# 2 Inheritance - Creating Subclasses
class Animal:

    cuteness_raise_amt = 1.1

    def __init__(self, first, last, cuteness):
        self.first = first
        self.last = last
        self.cuteness = cuteness
        self.description = 'My name is ' + first + last + ' and my cuteness level is ' + str(cuteness)
    
    # Methods
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def increase_cuteness(self):
        self.cuteness = int(self.cuteness * self.cuteness_raise_amt)
    

class Dog(Animal):

    cuteness_raise_amt = 1.4

    def __init__(self, first, last, cuteness, fur_colour):
        super().__init__(first, last, cuteness) # Let the parent class handle the OG attributes
        self.fur_colour = fur_colour

class Cat(Animal):

    def __init__(self, first, last, cuteness, kittens=None):
        super().__init__(first, last, cuteness) 
        if kittens is None:
            self.kittens = []
        else:
            self.kittens = kittens

    def add_kitten(self, kitt):
        if kitt not in self.kittens:
            self.kittens.append(kitt)
    
    def remove_kitten(self, kitt):
        if kitt in self.kittens:
            self.kittens.remove(kitt)
    
    def print_kitten(self): 
        for kitt in self.kittens:
            print('-->', kitt.full_name()) # Wow, confusing



furry_thing = Animal('Bojo', 'Binks', 70)
border_collie = Dog('Lucky', 'Blackie', 90, 'Black and White')

border_collie.increase_cuteness()
print(border_collie.cuteness) # Increases to 125

norwegian_forest_cat = Cat('Majestic', 'Beastie', 100, [furry_thing])

norwegian_forest_cat.add_kitten(border_collie) # Add border collie as a second kitten
norwegian_forest_cat.print_kitten()

print(isinstance(furry_thing, Dog))
print(issubclass(Cat, Animal))

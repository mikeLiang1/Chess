# 4 Property Decorators - Getters, Setters, Deleters

class Animal:

    cuteness_raise_amt = 1.1

    def __init__(self, first, last, cuteness):
        self.first = first
        self.last = last
        self.cuteness = cuteness
    
    # Method (using property decorator, the preferred method over spamming setters and deleters)
    @property # Declaring as a method but can access it as an attribute (so we don't have to change our code)
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    # Setters (can be used to change OG attributes from the method)
    @full_name.setter # Name of the property
    def full_name(self, new_name):
        first, last = new_name.split(' ')
        self.first = first
        self.last = last

    # Deleters 
    @full_name.deleter 
    def full_name(self):
        print('Delete name!')
        self.first = None
        self.last = None

furry_thing = Animal('Bojo', 'Binks', 70)

# Setter application
furry_thing.full_name = 'Idiot Sandwich'
print(furry_thing.last) 

# Property decorator application
print(furry_thing.full_name) # Originally, print(furry_thing.full_name())
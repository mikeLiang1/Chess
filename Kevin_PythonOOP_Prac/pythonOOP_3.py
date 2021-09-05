# 3 Special Methods (Magic / Dunder)

class Animal:

    cuteness_raise_amt = 1.1

    def __init__(self, first, last, cuteness):
        self.first = first
        self.last = last
        self.cuteness = cuteness
    
    # Methods
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def increase_cuteness(self):
        self.cuteness = self.cuteness * self.cuteness_raise_amt
    
    # Special Methods (Dunders) https://www.pythonlikeyoumeanit.com/Module4_OOP/Special_Methods.html
    def __repr__(self): # For debugging and dev -> should return your exact line of code with formatting (umambiguous)
        return "Animal('{}', '{}', '{}')".format(self.first, self.last, self.cuteness)
    
    def __str__(self): # For user (readeable)
        return '{} {} My name is {} {} and my cuteness level is {}'.format(self.first, self.last, self.first, self.last, self.cuteness)
    
    def __add__(self, other):
        return self.cuteness + other.cuteness 

    def __len__(self):
        return len(self.full_name())

furry_thing = Animal('Bojo', 'Binks', 70)
furry_thing.increase_cuteness()

print(repr(furry_thing)) #print(furry_thing.__repr__())
print(str(furry_thing)) #print(furry_thing.__str__())

print(furry_thing + furry_thing) # Actually adds the cuteness and doesnt print gibberish
print(len(furry_thing))

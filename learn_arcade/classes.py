###### Simple classes ######

class Character():
    def __init__(self):
        """ A constructer runs automatically when a class is created """
        self.name = "" # self. means that the attribute is unique to the instance of the class
        outfit = "Green"
        self.max_hit_points = 0
        self.current_hit_points = 0
        self.max_speed = 0
        self.armor_level = 0

class Address():
    def __init__(self):
        self.name = ""
        self.line1 = ""
        self.line2 = ""
        self.city = ""
        self.county = ""
        self.postcode = ""

home_add = Address()

home_add.name = "Peter Parker"
home_add.line1 = "59 Ulswater Crescent"
home_add.line2 = ""
home_add.city = "Crook"
home_add.county = "Durham"
home_add.postcode = "DL15 8PE"

#### methods ####

class Dog():
    def __init__(self): # list attributes first, then any methods
        self.age = 0
        self.name = ""
        self.breed = ""

    def bark(self): # first param of a method but be self
        """ 
        A method is a function that exists inside a class.
        So I could call dog.bark() here 
        """
        print("woof")
        print("my name is {}".format(self.name)) # methods can reference any of the class attributes using self.

my_dog = Dog()

my_dog.name = "Sunny"
my_dog.breed = "Cockapoo"
my_dog.age = 2

#my_dog.bark()


### practice ###

class Cat():
    def __init__(self):
        self.name = ""
        self.colour = ""
        self.weight = 0

    def meow(self):
        print("Meow!")

class Monster():
    def __init__(self):
        self.name = ""
        self.health = 0

    def decrease_health(self,amount):
        self.health -= amount
        print("{} took damage, its health is now {}".format(self.name,self.health))
        if self.health == 0:
            print("{} is dead".format(self.name))

def main():
    my_kitty = Cat()
    my_kitty.name = "tabby"
    my_kitty.colour = "tan"
    my_kitty.weight = 20

    my_kitty.meow()
    print()
    
    the_monster = Monster()
    the_monster.name = "Scary boi"
    the_monster.health = 100

    the_monster.decrease_health(20)
    input()
    the_monster.decrease_health(20)
    input()
    the_monster.decrease_health(20)
    input()
    the_monster.decrease_health(20)
    input()
    the_monster.decrease_health(20)
    input()

#main()

class Star():
    def __init__(self):
        print("A new star is born!")

class Monster2():
    def __init__(self,health,name):
        self.name = name
        self.health = health

def main2():

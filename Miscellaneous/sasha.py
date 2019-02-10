class Bottle:
    """This class defines a Bottle object as an entity with a color and a volume (attributes), which by default are set
    as 'white' and '1.0'.
    Bottle objects also have a method, 'empty()', which changes the attribute of volume bringing it to 0.0"""
# the class definition starts with the word "class". It is followed by the name of the class and by two columns.
# everything that follows is indented, and consists mainly of definitions.

    def __init__(self):         # this __init__(self) definition sets the parameters/attributes that characterize
        # the class, along with their default values. If I create a Bottle object without any other specification,
        # its attributes will have the default values
        self.color = "white"
        self.volume = 1.0

    def empty(self):            # this is a method of Bottles. It acts specifically on Bottle objects: it won't work if
        # I try to apply it to a string or an integer or a list. Note that methods are defined within the class
        # definition! That's why they only apply to one category of object. Think of methods of lists
        # methods of strings... they work in the exact same way.
        self.volume = 0.0


def fill(bottle):
    bottle.volume = 2.0
    return bottle


my_bottle = Bottle()            # my_bottle is a variable that stores an instance of the Bottle class. Think of it as
# Plato's concept of hyperuranium: the class is the ideal representation and the instance is one particular object
# corresponding to that idea
print(f"This is my bottle.\nIts color is {my_bottle.color}, and it contains {my_bottle.volume} litres of juice")
my_bottle.empty()
print("Here is what my bottle looks like if I try to print it:\n{0}".format(my_bottle))
print("Now I applied a method, my bottle is empty and it contains a volume of {0}".format(my_bottle.volume))
my_bottle = fill(my_bottle)

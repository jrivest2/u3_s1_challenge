"""Make a Product Class"""

from random import *


class Product:
    """General Product Representation"""
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        """Calculates the stealability of a product"""
        if self.price / self.weight < 0.5:
            return "Not so stealable..."
        elif 0.5 <= self.price / self.weight < 1:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        """Calculates flammability x weight"""
        if self.flammability * self.weight < 10:
            return "...fizzle."
        elif 10 <= self.flammability * self.weight < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif 5 <= self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"

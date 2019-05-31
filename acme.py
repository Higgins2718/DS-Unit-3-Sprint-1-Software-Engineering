import random


class Product:
    name = str,
    price = int,
    weight = int,
    flammability = float,
    identifier = int

    def __init__(self, name):
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
        self.identifier = random.randint(1000000.0, 9999999)

    def stealability(self):
        ratio = self.price/self.weight
        if ratio < 0.5:
            message = "Not so stealable..."
            return message

        elif ratio >= 0.5 and ratio < 1.0:
            message = "Kinda stealable."
            return message
        else:
            message = "Very stealable!"
            return message

    def explode(self):
        product_val = self.flammability * self.weight

        if product_val < 10:
            result = "fizzle"
            return result

        elif product_val >= 10 and product_val < 50:
            result = "...boom!"
            return result
        else:
            result = "...BABOOM!!"
            return result


class BoxingGlove(Product):

    def __init__(self, name=None):
        super().__init__(name=name)
        self.weight = 10

    def explode(self):
        useless = "...it's a glove."
        return useless

    def punch(self):
        if self.weight < 5:
            complaint = "That tickles."
            return complaint

        elif self.weight >= 5 and self.weight < 15:
            complaint = "Hey that hurt!"
            return complaint
        else:
            complaint = "OUCH!"
            return complaint

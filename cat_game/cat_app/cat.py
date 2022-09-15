from random import randint


class Cat:
    def __init__(self, cat_name=None, action=None, state=None, image=None):
        self.cat_name = cat_name
        self.age = randint(1, 7)
        self.satiety = randint(30, 60)
        self.happiness = randint(30, 80)
        self.action = action
        self.state = state
        self.image = image

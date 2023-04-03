class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, new_color):
        Animal.color = new_color

first_animal = Animal('Vasya',5)
second_animal = Animal ('Anfisa',6)
first_animal.change_color('red')
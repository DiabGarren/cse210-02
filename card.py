from math import randint as r
class Card:

    def __init__(self):
        self.prev_value
        self.value

    def next_card(self):
        next_value = r(0, 100)
        if next_value == self.prev_value:
            self.value = next_value
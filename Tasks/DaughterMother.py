import random

class Mother():
    color = "brown"
    _haircolor = color
    def __init__(self, haircolor):
        self._haircolor = haircolor

class Daughter(Mother):
    def print(self, _haircolor):
        Super().__init__(_haircolor)
        print(self, _haircolor)

d = Daughter
d.print()


from gameunit import *

class Hero(Attaker):
    def __init__(self):
        self._health = 100
        self._attack = 50
        self._exp = 0
        self._name = name






#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атак
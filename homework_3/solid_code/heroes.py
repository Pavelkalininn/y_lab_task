from abc import abstractmethod


class SuperHero:

    def __init__(self, name: str):
        self.name = name

    def find(self, place):
        place.get_antagonist()

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def ultimate(self):
        pass


class Superman(SuperHero):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent')

    def __incinerate_with_lasers(self):
        print('Wzzzuuuup!')

    def attack(self):
        print('Kick')

    def ultimate(self):
        self.__incinerate_with_lasers()


class ChackNorris(SuperHero):

    def __init__(self):
        super(ChackNorris, self).__init__('Chack Norris')

    def __fire_a_gun(self):
        print('PIU PIU')

    def __roundhouse_kick(self):
        print('Bump')

    def attack(self):
        self.__fire_a_gun()

    def ultimate(self):
        self.__roundhouse_kick()

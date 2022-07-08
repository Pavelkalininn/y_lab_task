from abc import abstractmethod, ABC
from typing import List, Optional


class Place(ABC):

    def __init__(self, name: Optional[str], coordinates: List[float] = None):
        self.name = name
        self.coordinates = coordinates

    @abstractmethod
    def get_antagonist(self):
        pass


class Kostroma(Place):

    def __init__(self):
        super(Kostroma, self).__init__('Kostroma')

    def get_antagonist(self):
        print('Orcs hid in the forest')


class Tokyo(Place):

    def __init__(self):
        super(Tokyo, self).__init__('Tokyo')

    def get_antagonist(self):
        print('Godzilla stands near a skyscraper')


class Planet(Place):

    def __init__(self):
        super(Planet, self).__init__(
            name=None,
            coordinates=[12.2845561, 13.4566456]
        )

    def get_antagonist(self):
        print('Planet attacked by Tanos')

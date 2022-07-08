from heroes import SuperHero
from places import Place


class MassMediaNews:

    def __init__(self, hero: SuperHero, place: Place):
        self.place = place.name or place.coordinates
        self.hero_name = hero.name

    def create_news(self):
        print(f'{self.hero_name} saved the {self.place}!')

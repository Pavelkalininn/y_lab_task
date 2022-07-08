from heroes import Superman, SuperHero, ChackNorris
from mass_medias import MassMediaNews
from places import Kostroma, Tokyo, Place, Planet


def save_the_place(hero: SuperHero, place: Place):
    """Saving incoming place by incoming superhero in action."""
    hero.find(place)
    hero.attack()
    hero.ultimate()
    MassMediaNews(hero, place).create_news()


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma())
    print('-' * 20)
    save_the_place(ChackNorris(), Tokyo())
    print('-' * 20)
    save_the_place(Superman(), Planet())

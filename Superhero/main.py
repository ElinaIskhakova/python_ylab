from antagonistfinder import AbstractPlace
from heroes import Superman, ChuckNorris,TV, Newspaper, AbstractHero, AbstractNotifier
from places import Kostroma, Tokyo, Planet



class SavePlace:

    def find_enemy(self):
        return self.place.get_antagonist()

    def notify(self):
        self.notifier.publicize(f'{self.hero.name} saved the {self.place.name}!')

    def __init__(self, hero: AbstractHero, place: AbstractPlace, notifier: AbstractNotifier):
        self.place = place
        self.hero = hero
        self.notifier = notifier

        self.find_enemy()
        hero.attack()
        self.notify()
        
if __name__ == '__main__':
    SavePlace(Superman(), Kostroma(), TV())
    print('-' * 20)
    SavePlace(ChuckNorris(), Planet(), Newspaper())
    print('-' * 20)
    SavePlace(ChuckNorris(), Tokyo(), Newspaper())

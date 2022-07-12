
from abc import ABC, abstractmethod

# По SOLID: Вынесено оповещение в отдельный класс, занимающийся выводом информации.
class AbstractNotifier(ABC):
    @abstractmethod
    def publicize(self, text):
        pass


class Newspaper(AbstractNotifier):
    def publicize(self, text):
        print(f'Today in newspaper: {text}')


class TV(AbstractNotifier):
    def publicize(self, text):
        print(f'Watch on the first channel: {text}')


# По SOLID: Создать классы-миксины для каждого оружия
class Gun:
    def fire_a_gun(self):
        print('PIU PIU')

class Laser:
    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')

class Karate:
    def roundhouse_kick(self):
        print('Bump')

  # По SOLID: Каждого супергероя реализовать как наследника SuperHero и вместо изменения базового класса переопределять нужные методы

class AbstractHero(ABC):

    @property
    def name(self):
        raise NotImplementedError

    @abstractmethod
    def attack(self):
        pass

class AbstractSuperHero(AbstractHero):

    @abstractmethod
    def ultimate(self):
        pass


class Superman(Karate, Laser, AbstractSuperHero):
    name = 'Clark Kent'

    def ultimate(self):
        self.incinerate_with_lasers()

    def attack(self):
        self.roundhouse_kick()
        self.ultimate()


class ChuckNorris(Gun, Karate, AbstractHero):
    name = 'Chuck Norris'

    def attack(self):
        self.roundhouse_kick()
        self.fire_a_gun()
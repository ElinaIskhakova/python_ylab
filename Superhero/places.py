from abc import ABC, abstractmethod

 # По SOLID: Создать абстрактный класс Place, обязывающий реализовать метод для поиска злодея

class AbstractPlace(ABC):

    @property
    def name(self):
        raise NotImplementedError(
                'Определите run в %s.' % (self.__class__.__name__))

    @abstractmethod
    def get_antagonist(self):
        pass

class Kostroma(AbstractPlace):
    name = 'Kostroma'

    def get_antagonist(self):
        print('Orcs hid in the forest')


class Tokyo(AbstractPlace):
    name = 'Tokyo'

    def get_antagonist(self):
        print('Godzilla stands near a skyscraper')

class Planet(AbstractPlace):

    coordinates = [13, 4]

    @property
    def name(self):
        return ','.join(map(str, self.coordinates))

    def get_antagonist(self):
        print('WARNING! Aliens!!!')        

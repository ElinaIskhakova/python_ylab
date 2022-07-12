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
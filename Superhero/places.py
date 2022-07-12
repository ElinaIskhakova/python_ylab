from antagonistfinder import AbstractPlace


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

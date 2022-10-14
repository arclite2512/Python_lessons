from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, name):
        pass

    @abstractmethod
    def tissue_consumption(self):
        pass

    def __add__(self, other):
        return self.tissue_consumption + other.tissue_consumption


class Coat(Clothes):
    def __init__(self, the_size, name='default'):
        super().__init__(name)
        self.name, self.the_size = name, the_size

    @property
    def tissue_consumption(self):
        return self.the_size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height, name='default'):
        super().__init__(name)
        self.name, self.height = name, height

    @property
    def tissue_consumption(self):
        return 2 * self.height + 0.3


coat = Coat(23)
print(f'Расход ткани на пальто: {coat.tissue_consumption:.2f}')

costume = Costume(23, name='super')
print(f'Расход ткани на костюм: {costume.tissue_consumption:.2f}')

print(f'Общий расход ткани: {coat + costume:.2f}')

class Road:
    _required_mass = 25
    _thickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self):
        return self._length * self._width * self._required_mass * self._thickness / 1000


road = Road(20, 5000)
print(f'{road.asphalt_mass():.0f}т.')

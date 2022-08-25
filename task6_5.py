class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки ручкой {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки карандашом {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки маркером {self.title}")


stationery = Stationery('Стандарт')
stationery.draw()

pen = Pen('Шариковая')
pen.draw()

pencil = Pencil('Простой')
pencil.draw()

handle = Handle('Маркер для доски')
handle.draw()

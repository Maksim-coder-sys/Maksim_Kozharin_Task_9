class Stationery:
    title = ''
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


s = Stationery(' ')
pe = Pen('ручкой')
pn = Pencil('карандашом')
h = Handle('маркером')
s.draw()
pe.draw()
pn.draw()
h.draw()

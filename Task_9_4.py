class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        if self.is_police ==1:
            print(f'Автомобиль принадлежит полиции {self.name} {self.color} едет')
        else:
            print(f'Автомобиль  не принадлежит полиции {self.name} {self.color} едет')
    def stop(self):
        if self.is_police == 1:
            print(f'Автомобиль принадлежит полиции {self.name} {self.color} остановился')
        else:
            print(f'Автомобиль  не принадлежит полиции {self.name} {self.color} остановился')
    def turn(self, direction):
        self.direction = direction
        if self.is_police == 1:
            print(f'Автомобиль принадлежит полиции {self.name} {self.color} повернул {self.direction}')
        else:
            print(f'Автомобиль  не принадлежит полиции {self.name} {self.color} повернул {self.direction}')

    def show_speed(self):
        if self.is_police == 1:
            print(f'Автомобиль принадлежит полиции {self.name} {self.color} скорость{self.speed} км/ч')
        else:
            print(f'Автомобиль  не принадлежит полиции {self.name} {self.color} скорость {self.speed} км/ч')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            if self.is_police == 1:
                print(f'Скорость автомобиля принадлежащего полиции {self.name} цвета {self.color} превышает допустимую')
            else:
                print(f'Скорость автомобиля  не принадлежащего полиции {self.name} цвета {self.color} превышает допустимую')
        else:
            print(f'Скрость автомобиля {self.name} цвета {self.color} {self.speed} км/ч')

class SportCar(Car):
    def show_speed(self):
        if self.is_police == 1:
            print(f'Скорость автомобиля принадлежащего полиции {self.name} цвета {self.color} {self.speed} км/ч')
        else:
            print(f'Скорость автомобиля не принадлежащего полиции {self.name} цвета {self.color} {self.speed} км/ч')
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            if self.is_police == 1:
                print(f'Скорость автомобиля принадлежащего полиции {self.name} цвета {self.color} превышает допустимую')
            else:
                print(
                    f'Скорость автомобиля  не принадлежащего полиции {self.name} цвета {self.color} превышает допустимую')
        else:
            print(f'Скрость автомобиля {self.name} цвета {self.color} {self.speed} км/ч')

class PoliceCar(Car):
    def show_speed(self):
        print(f'Скорость автомобиля принадлежавшего полиции {self.name} цвета {self.color} {self.speed} км/ч')
c = Car(50, 'синий', 'Шевроле', 0)
c.go()
c.stop()
c.turn('налево')
c.show_speed()
w = TownCar(70, 'красный', 'Нива', 1)
w.show_speed()
p = PoliceCar(60, 'белый','мерседес', 1)
p.show_speed()
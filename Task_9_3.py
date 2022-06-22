class Worker:
    def __init__(self, name, surname, position, income = {}):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        name_surname = self.surname + ' ' + self.name
        print(f'Полное имя: {name_surname}')
    def get_total_income(self):
        many = self._income["wage"] + self._income["bonus"]
        print(f'Общий доход {many}')


p = Position('Иван', 'Иванов', 'Инженер', {"wage": 300, "bonus": 50})
p.get_full_name()
p.get_total_income()
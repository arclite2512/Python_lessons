class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name, self.surname, self.position = name, surname, position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}, должность - {self.position}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


worker_position = Position('Иванов', 'Александр', 'кладовщик', 55000, 150)
print(worker_position.name, worker_position.surname, worker_position.position, worker_position._income, end='\n\n')
print(worker_position.get_full_name())
print(worker_position.get_total_income())

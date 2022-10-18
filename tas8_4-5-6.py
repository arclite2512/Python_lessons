class Warehouse:
    __storage = []
    __summary = {}

    def push(self, equipment):
        if not isinstance(equipment, OfficeEquipment):
            raise Exception('Склад может принимать только оргтехнику')
        self.__storage.append(equipment)
        if self.__summary.get(equipment.type) is not None:
            self.__summary[equipment.type] += 1
        else:
            self.__summary.setdefault(equipment.type, 1)

    def report_items(self):
        for item in self.__storage:
            print(item)

    def report_total(self):
        for k, v in self.__summary.items():
            print(f'{k}: {v} шт')


class OfficeEquipment:
    def __init__(self, type: str, model: str, cost: float, sn: str):
        self.type = str(type)
        self.model = str(model)
        self.cost = float(cost)
        self.sn = str(sn)

    def __str__(self):
        return f"{self.type} {self.model}"


class Printer(OfficeEquipment):
    def __init__(self, model: str, cost: float, is_colorful: bool, sn: str):
        self.is_colorful = is_colorful
        super().__init__('Принтер', model, cost, sn)


class Scanner(OfficeEquipment):
    def __init__(self, model: str, cost: float, dpi: str, sn: str):
        self.dpi = dpi
        super().__init__('Сканер', model, cost, sn)


class Copier(OfficeEquipment):
    def __init__(self, model: str, cost: float, is_colorful: bool, dpi: str, velocity: int, sn: str):
        self.is_colorful = is_colorful
        self.dpi = dpi
        self.velocity = velocity
        super().__init__('МФУ', model, cost, sn)


if __name__ == '__main__':
    printer01 = Printer('Epson 400', 15500.12, True, '6SS549876548')
    printer02 = Printer('HP Laser 45rm', 9600, False, 'G63425SFG5')
    scanner01 = Scanner('Epson  V33', 7810, '4800x4800', '65456721FF5')
    scanner02 = Scanner('Canon  700', 9800.40, '2400x2400', '31313131AAA')
    copier01 = Copier('Canon 25SD', 4399.63, True, '4800x600', 8, 'FG8#WEHF')
    copier02 = Copier('Brother 3020WHR', 23100, False, '2400x600', 30, '9BB600052133')
    copier03 = Copier('HP LaserJet M249', 17604.70, False, '1200x1200', 22, '9B1114848554')

    warehouse = Warehouse()
    warehouse.push(printer01)
    warehouse.push(printer02)
    warehouse.push(scanner01)
    warehouse.push(scanner02)
    warehouse.push(copier01)
    warehouse.push(copier02)
    warehouse.push(copier03)

    warehouse.report_items()
    warehouse.report_total()

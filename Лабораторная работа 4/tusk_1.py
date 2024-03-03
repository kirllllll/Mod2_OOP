class Car:
    def __init__(self, label: str, model: str, year: int, color: str):
        """
        Создание и подготовка к работе объекта «Car»
        :param label: Марка машины.
        :param model: Модель.
        :param year: Год выпуска.
        :param color: Цвет.
        """
        self.label = label
        self.model = model
        self.year = year
        self.color = color

    def mileage(self, quantity: int) -> str:
        """
        Данный метод вводит информацию о пробеге техники.
        :param quantity: Пробег транспорта в км.
        :return: Строка с информацией о транспорте(включая пробег).
        """
        return f"{self.label} {self.model} прошел в общем количестве {quantity} км."

    def __str__(self) -> str:
        """
        Магический метод необходимый
        для представления информации
        о технике в текстовом виде.
        :return: Строка с информацией о машине.
        """
        return f"{self.year} {self.color} {self.label} {self.model}"

    def __repr__(self) -> str:
        """
        Магический метод необходимый для передачи машинного кода.
        :return: Строка с информацией о машине.
        """
        return f"Car(label='{self.label}', model='{self.model}', year={self.year}, color='{self.color}')"


class Car(Car):
    def __init__(self, label: str, model: str, year: int, color: str, num_doors: int):
        """
        Создание сегмента класса "Советский грузовик ЗИЛ-131".
        :param label: Марка машины.
        :param model: Модель.
        :param year: Год выпуска.
        :param color: Цвет.
        :param num_doors: Количество дверей.
        """
        super().__init__(brand, model, year, color)
        self.num_doors = num_doors

    def start_engine(self) -> str:
        """
        Метод, выдающий информацию о запуске вдигателя.
        :return: Строка о запуске двигателя.
        """
        return f"{self.label} {self.model} завелся."

    def __str__(self) -> str:
        """
        Перегрузка магического метода для получения строки с объектом в текстовой форме.
        :return: Строка с информацией.
        """
        return f"{super().__str__()}, {self.num_doors} дверей"

    def __repr__(self) -> str:
        """
        Перегрузка магического метода для получения строки для внутреннего представления.
        :return: Строка с информацией.
        """
        return f"Car(label='{self.label}', model='{self.model}', year={self.year}, color='{self.color}', num_doors={self.num_doors})"


if __name__ == "__main__":
    # Создание параметров для использования класса
    car1 = Car(label="ЗИЛ-131", model="ЗИЛ-131Н1", year=1966, color="Blue", num_doors=2)
    print(car1.mileage(1130))  # Вывод: ЗИЛ-131 проехал 1130 км.
    print(car1.start_engine())  # Вывод: ЗИЛ-131 завелся.
    print(str(car1))  # Вывод: 1966 Blue ЗИЛ-131Н1, 2 дверей
    print(repr(car1))  # Вывод: Car(label='ЗИЛ-131', model='ЗИЛ-131Н1', year=1966, color='Blue', num_doors=2)
    pass
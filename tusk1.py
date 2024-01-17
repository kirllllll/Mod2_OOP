import doctest


class Garage:
    def __init__(self, zhiguli: int, mazda: int, hummer: int):
        """
        Создание и подготовка к работе объекта "Гараж"

        :param zhiguli: Легковой автомобиль малого класса семейства "Жигули"
        :param mazda: Среднеразмерный автомобиль японской компании "Mazda"
        :param hummer: Гражданский полноразмерный внедорожник "Hummer"

        Примеры:
        >>> garage = Garage(1, 1, 1) # инициализация экземпляра класса
        """

        self.parking_spaces = 4  # Общее количество парковочных мест в гараже

        if not isinstance(zhiguli, int):
            raise TypeError("Количество транспортных средств должно быть типа int")
        if zhiguli < 0:
            raise ValueError("Количество транспортных средств не может быть отрицательным числом")
        if zhiguli > self.parking_spaces:
            raise ValueError("Количество транспортных средств не может быть больше количества парковочных мест")
        self.zhiguli = zhiguli

        if not isinstance(mazda, int):
            raise TypeError("Количество транспортных средств должно быть типа int")
        if mazda < 0:
            raise ValueError("Количество транспортных средств не может быть отрицательным числом")
        if mazda > self.parking_spaces:
            raise ValueError("Количество транспортных средств не может быть больше количества парковочных мест")
        self.mazda = mazda

        if not isinstance(hummer, int):
            raise TypeError("Количество транспортных средств должно быть типа int")
        if hummer < 0:
            raise ValueError("Количество транспортных средств не может быть отрицательным числом")
        if hummer > self.parking_spaces:
            raise ValueError("Количество транспортных средств не может быть больше количества парковочных мест")
        self.hummer = hummer

        if zhiguli + mazda + hummer > self.parking_spaces:
            raise ValueError("Слишком много транспортных средств, недостаточно места в гараже")

    def add_zhiguli(self, zhiguli: int) -> None:
        """
        Добавление легкового автомобиля "Жигули" в автопарк

        :param zhiguli: Легковой автомобиль малого класса семейства "Жигули"
        :raise ValueError: Если общее количество транспортных средств превышает возможное,
            то вызываем ошибку

        Примеры:
        >>> garage = Garage(1, 0, 0)
        >>> garage.add_zhiguli(3)
        """

        if not isinstance(zhiguli, int):
            raise TypeError("Количество машин должно быть типа int")
        if zhiguli < 0:
            raise ValueError("Количество транспортных средств не может быть отрицательным числом")
        if self.zhiguli + self.mazda + self.hummer + zhiguli > self.parking_spaces:
            raise ValueError("Слишком много транспортных средств, недостаточно места в гараже")

        self.zhiguli += zhiguli  # Добавляем легковой автомобиль "Жигули" в автопарк

    def add_mazda(self, mazda: int) -> None:
        """
        Добавление среднеразмерного автомобиля "Mazda" в автопарк

        :param mazda: Среднеразмерный автомобиль японской компании "Mazda"
        :raise ValueError: Если общее количество транспортных средств превышает возможное,
            то вызываем ошибку

        Примеры:
        >>> garage = Garage(1, 1, 1)
        >>> garage.add_mazda(1)
        """

        if not isinstance(mazda, int):
            raise TypeError("Количество машин должно быть типа int")
        if mazda < 0:
            raise ValueError("Количество транспортных средств не может быть отрицательным числом")
        if self.zhiguli + self.mazda + self.hummer + mazda > self.parking_spaces:
            raise ValueError("Слишком много транспортных средств, недостаточно места в гараже")

        self.mazda += mazda  # Добавляем среднеразмерный автомобиль "Mazda" в автопарк

    def add_hummer(self, hummer: int) -> None:
        """
        Добавление внедорожника "Hummer" в автопарк

        :param hummer: Гражданский полноразмерный внедорожник "Hummer"
        :raise ValueError: Если общее количество транспортных средств превышает возможное,
            то вызываем ошибку

        Примеры:
        >>> garage = Garage(1, 1, 1)
        >>> garage.add_hummer(1)
        """

        if not isinstance(hummer, int):
            raise TypeError("Количество машин должно быть типа int")
        if hummer < 0:
            raise ValueError("Количество транспортных средств не может быть отрицательным числом")
        if self.zhiguli + self.mazda + self.hummer + hummer > self.parking_spaces:
            raise ValueError("Слишком много транспортных средств, недостаточно места в гараже")

        self.hummer += hummer  # Добавляем гражданский полноразмерный внедорожник "Hummer" в автопарк

    def hm_space(self) -> str:
        """
        Функция, которая проверяет количество свободных парковочных мест
        в гараже, если места есть, то скажет сколько свободно в данный момент

        :return: Дает ответ по наличию свободных мест в гараже
        """

        if self.zhiguli + self.mazda + self.hummer < 4:
            print(f'Еще есть место, можно поставить {4 - self.zhiguli - self.mazda - self.hummer} машины')
        else:
            print('Все парковочные места заняты, поставьте в другом месте')

class Borsch:
    def __init__(self, carrot_kg: float, beet_kg: float, meet_kg: float):
        """
        Создание и подготовка к работе объекта "Борщ"

        :param carrot_kg: Количество кг моркови на суп
        :param beet_kg: Количество кг свеклы на суп
        :param meet_kg: Количество кг мяса на суп

        Примеры:
        >>> borsch = Borsch(0.1, 0.5, 1.2)
        """

        if not isinstance(carrot_kg, (int, float)):
            raise TypeError("Количество кг моркови должно быть типа int или float")
        if carrot_kg < 0.1:
            raise ValueError("Слишком мало моркови на суп, не хватит даже на 2 порции")
        if carrot_kg > 0.4:
            raise ValueError("Слишком много моркови на суп, куда нам больше 8 порций")

        self.carrot_kg = carrot_kg

        if not isinstance(beet_kg, (int, float)):
            raise TypeError("Количество кг свеклы должно быть типа int или float")
        if beet_kg < 0.5:
            raise ValueError("Слишком мало свеклы на суп, не хватит даже на 2 порции")
        if carrot_kg > 2:
            raise ValueError("Слишком много свеклы на суп, куда нам больше 8 порций")

        self.beet_kg = beet_kg

        if not isinstance(meet_kg, (int, float)):
            raise TypeError("Количество кг моркови должно быть типа int или float")
        if meet_kg < 0.3:
            raise ValueError("Слишком мало мяса на суп, не хватит даже на 2 порции")
        if carrot_kg > 1.2:
            raise ValueError("Слишком много мяса на суп, куда нам больше 8 порций")

        self.meet_kg = meet_kg

    def add_carrot(self, carrot_kg: float) -> None:
        """
        Добавляем морковь в суп

        :param carrot_kg: Количество кг моркови на суп
        :raise ValueError: Если моркови не хватает на пару порций или проций больше 8,
            то вызываем ошибку


        Примеры:
        >>> borsch = Borsch(1, 1, 1)
        >>> borsch.add_carrot(1)  #NameError: name 'borsch' is not defined. Did you mean: 'Borsch'?
        """

        if not isinstance(carrot_kg, (int, float)):
            raise TypeError("Количество кг моркови должно быть типа int или float")
        if self.carrot_kg + carrot_kg < 0.1:
            raise ValueError("Слишком мало моркови на суп, не хватит даже на 2 порции")
        if self.carrot_kg + carrot_kg > 0.4:
            raise ValueError("Слишком много моркови на суп, куда нам больше 8 порций")

        self.carrot_kg += carrot_kg  # Добавляем морковь в суп

    def add_beet(self, beet_kg: float) -> None:
        """
        Добавляем морковь в суп

        :param beet_kg: Количество кг моркови на суп
        :raise ValueError: Если моркови не хватает на пару порций или проций больше 8,
            то вызываем ошибку


        Примеры:
        >>> borsch = Borsch(1, 1, 1)
        >>> borsch.add_beet(1)  #NameError: name 'borsch' is not defined. Did you mean: 'Borsch'?
        """

        if not isinstance(beet_kg, (int, float)):
            raise TypeError("Количество кг свеклы должно быть типа int или float")
        if self.beet_kg + beet_kg < 0.1:
            raise ValueError("Слишком мало свеклы на суп, не хватит даже на 2 порции")
        if self.beet_kg + beet_kg > 0.4:
            raise ValueError("Слишком много свеклы на суп, куда нам больше 8 порций")

        self.beet_kg += beet_kg  # Добавляем свеклу в суп

    def add_meet(self, meet_kg: float) -> None:
        """
        Добавляем морковь в суп

        :param meet_kg: Количество кг моркови на суп
        :raise ValueError: Если моркови не хватает на пару порций или проций больше 8,
            то вызываем ошибку


        Примеры:
        >>> borsch = Borsch(1, 1, 1)
        >>> borsch.add_meet(1)  #NameError: name 'borsch' is not defined. Did you mean: 'Borsch'?
        """

        if not isinstance(meet_kg, (int, float)):
            raise TypeError("Количество кг мяса должно быть типа int или float")
        if self.meet_kg + meet_kg < 0.1:
            raise ValueError("Слишком мало мяса на суп, не хватит даже на 2 порции")
        if self.meet_kg + meet_kg > 0.4:
            raise ValueError("Слишком много мяса на суп, куда нам больше 8 порций")

        self.meet_kg += meet_kg  # Добавляем мясо в суп

    def portion_counter(self) -> str:
        """
        Функция, которая вычисляет общее возможное количество порций
        и вычисляет остаток продуктов

        :return: Сообщает количество порций и остатка овощей

        Примеры:
        >>> borsch = Borsch(1, 0.7, 1)
        >>> borsch.portion_counter()  #NameError: name 'borsch' is not defined. Did you mean: 'Borsch'?
        """
        ...


class Track:
    def __init__(self, song: int, words: int):
        """
        Создание и подготовка к работе объекта "Звуковая орожка"
        :param song: Количество песен
        :param words: Количество слов

        Примеры:
        >>> track = Track(3, 15)
        """

        if not isinstance(song, int):
            raise TypeError("Количество слов должно быть типа int")
        if song < 1:
            raise ValueError("Меньше 1 песни не записывают в студии")
        if song > 3:
            raise ValueError("Не хватит времени на запись")

        self.song = song

        if not isinstance(words, int):
            raise TypeError("Количество слов должно быть типа int")
        if words < 20:
            raise ValueError("Не хватает слов на песню, нужно дописать текст")
        if words > 60:
            raise ValueError("На 1 песню не больше 20 слов, больше не нужно")

        self.words = words

    def word_counter(self) -> str:
        """
        Функция позволяет оценить количество слов, необходимое для того,
        чтобы закончить запись

        :return: Количество слов для полноценной песни

        Примеры:
        >>> track = Track(3, 15)
        >>> track.word_counters()
        """
        ...

    def song_removal(self, song: int) -> None:
        """
        Позволяет отменить запись еще одной песни, если слов слишком мало

        :param song: Количество песен

        :raise ValueError: Если количество песен обнуляется,
        возвращается ошибка

        Примеры:
        >>> track = Track(3, 15)
        >>> track.song_removal(1)
        """

        if not isinstance(song, int):
            raise TypeError("Количество кг мяса должно быть типа int или float")
        if song < 1:
            raise ValueError("Количество песен не может быть отрицательным числом")
        if song - song < 1:
            raise ValueError("Меньше 1 песни не записывают в студии")
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass

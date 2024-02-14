class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)

        self.pages = pages

        @property
        def pages(self) -> int:
            return self._pages

        @pages.setter
        def pages(self, new_pages: int) -> None:
            if not isinstance(new_pages, int):
                raise TypeError("Количество страниц должно быть типа int")

            if new_pages <= 0:
                raise ValueError("Количество страниц должно быть положительным числом")

            self._pages = new_pages

    def __str__(self):
        return f"Книга бумажная {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
            return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise  TypeError("Продолжительность должна быть типа float")

        if new_duration <= 0:
            raise  ValueError("Продолжительность не может быть отрицательным")

        self._duration = new_duration

        def __str__(self):
            return f"Аудиокнига {self.name}. Автор {self.author}. Продолжительность {self.duration}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, author={self.duration!r})"

b1 = Book("Михайлов", "Диплом")
pb = PaperBook("Михайлов", "Диплом", 70)
ab = AudioBook("Михайлов", "Диплом", 15.0)

print(pb.duration)
ab.duration = 10.2
print(pb.duration)

"""
E:\Course Python английский\Инкапсуляция, наследование, полиморфизм\Лабораторная 3\task1\main.py:82: SyntaxWarning: invalid escape sequence '\C'
  """
Traceback (most recent call last):
  File "E:\Course Python английский\Инкапсуляция, наследование, полиморфизм\Лабораторная 3\task1\main.py", line 74, in <module>
    b1 = Book("Михайлов", "Диплом")
         ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "E:\Course Python английский\Инкапсуляция, наследование, полиморфизм\Лабораторная 3\task1\main.py", line 4, in __init__
    self.name = name
    ^^^^^^^^^
AttributeError: property 'name' of 'Book' object has no setter
"""



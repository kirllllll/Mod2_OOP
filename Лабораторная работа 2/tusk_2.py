BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book

class Book:
    def __init__(self, id_: str, name: str, pages: int):
        """

        :param id_: идентификатор книги
        :param name: название книги
        :param pages: количество страниц в книге
        """
        self.id_ = id_
        self.name = name
        self.pages = pages



    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id={self.__class__.__name__}(id_ ={self.id_}, name={self.name!r}, pages={self.pages})'


# TODO написать класс Library

class Library:

    def __int__(self, books=None):
        if books is None:
            books = []

        self.books = books


    def get_next_book_id(self) -> int:
        if self.books is None:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, id_) -> int:
        books_lst = [ebook.id for ebook in self.books]
        if id_ in books_lst:
            return books_lst.idnex(id_)
        raise ValueError("Книги с запрашиваемым id не существует")






if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

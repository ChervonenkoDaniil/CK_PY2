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
    """
    Описывает книги, помещающиеся в библиотеку
    """

    def __init__(self, id_, pages: int, name: str):
        """
        Инициализирует параметры класса Book
        Создает и подготавливает к работе данный класс

        :param id_: Параметр идентификатора книги
        :param pages: Параметр количества страниц книги
        :param name: Параметр названия книги
        """
        if not isinstance(id_, int):
            raise TypeError("This parameter should have int type, check your dict for mistake")

        self.book_id = id_

        if not isinstance(pages, int):
            raise TypeError("This parameter should have int type, check your dict for mistake")
        if pages <= 0:
            raise ValueError("This parameter value should be greater than 0")
        self.book_pages = pages

        if not isinstance(name, str):
            raise TypeError("This parameter should have str type, check your dict for mistake")
        self.book_name = name

    def __str__(self) -> str:
        return f'Книга "{self.book_name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.book_id!r}, name={self.book_name!r}, pages={self.book_pages!r})'


# TODO написать класс Library
class Library:
    """
    Описывает библиотеку, куда помещаются книги
    """

    def __init__(self, books=[]):  # Инициализируем список книг
        # При инициализации пустого списка PyCharm обозначает это как предупреждение, о том, что значение по умолчанию
        # изменяемо, поэтому, для устранения предупреждения, в качестве этого значения выбрал None
        """
        Инициализирует параметры класса Library
        Создает и подготавливает к работе данный класс

        :param books: Список книг, располагающихся в библиотеке
        """
        self.book_list = books

    def get_next_book_id(self) -> int:  # Увеличиваем id последней книги на 1
        """
        Показывает значение идентификатора для следующей книги

        :return: Значение последнего идентификатора, увеличенное на 1
        """
        return 1 if len(self.book_list) == 0 else [i.book_id for i in self.book_list][-1] + 1

    # При предполагаемом соблюдении порядка сортировки книг в порядке возрастания:
        # return len(self.book_list) + 1

    def get_index_by_book_id(self, id_for_search: int) -> int:
        """
        Показывает, есть ли книга в наличии, по ее идентификатору

        :param id_for_search: ID книги для осуществления запроса
        :return: Индекс книги в списке, при ее наличии, или возвращает ValueError
        """
        if not isinstance(id_for_search, int):
            raise ValueError("This parameter should have int type, check your dict for mistake")

        book_index = [index for index, books in enumerate(self.book_list) if books.book_id == id_for_search]
        if not book_index:
            raise ValueError("Книги с запрашиваемым id не существует")
        else:
            return book_index[0]

    # При предполагаемом соблюдении порядка сортировки книг в порядке возрастания:
        # return id_for_search - 1 (вместо enumerate)


if __name__ == '__main__':
    empty_library = Library()  # Инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # Проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # Инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # Проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # Проверяем индекс книги с id = 1

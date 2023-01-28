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

    def __init__(self, id_, pages: int, name: str):
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
    id_list = [book_dict["id"] for book_dict in BOOKS_DATABASE]  # для удобства дальнейшей работы и отсутствия
                                                                 # повторений, сразу выведем список id книг
    # При предполагаемом соблюдении порядка сортировки книг в порядке возрастания отказаться от параметра

    def __init__(self, books=None):  # инициализируем список книг
        self.book_list = books
        if books is None:
            self.book_list = []

    def get_next_book_id(self) -> int:  # увеличиваем id последней книги на 1
        return 1 if len(self.book_list) == 0 else self.id_list[-1] + 1
        # При предполагаемом соблюдении порядка сортировки книг в порядке возрастания:
        # return len(self.book_list) + 1

    def get_index_by_book_id(self, id_for_search: int) -> int:
        if not isinstance(id_for_search, int):
            raise ValueError("This parameter should have int type, check your dict for mistake")
        if id_for_search not in self.id_list:
            raise ValueError("Книги с запрашиваемым id не существует")
        for index, id_ in enumerate(self.id_list):
            if id_ == id_for_search:
                return index
    # При предполагаемом соблюдении порядка сортировки книг в порядке возрастания:
    # return id_for_search - 1 (вместо enumerate)


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

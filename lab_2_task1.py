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

    def __init__(self, id_, pages: int, name: str):  # Инициализируем параметры класса, вводим ограничения
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

    def __str__(self) -> str:  # Вызываем метод экземпляра __str__
        return f'Книга "{self.book_name}"'

    def __repr__(self) -> str:   # Вызываем метод экземпляра __repr__
        return f'Book(id_={self.book_id!r}, name={self.book_name!r}, pages={self.book_pages!r})'


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__

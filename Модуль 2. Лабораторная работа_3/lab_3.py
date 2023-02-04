class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """
        Инициализирует параметры родительского класса
        :param name: Наименование книги
        :param author: Автор книги
        """
        #  Вводим приватные параметры для ограничения доступа пользователей к редактированию
        self.__name = name
        self.__author = author

    # Вводим Getter-ы в надежде, что никакой подлец не будет редактировать параметры
    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"


class PaperBook(Book):
    """Класс, описывающий книгу в бумажном исполнении"""
    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализирует параметры класса PaperBook
        :param name: Наименование книги (из базового класса)
        :param author: Автор книги (из базового класса)
        :param pages: Количество страниц книги
        """
        super().__init__(name, author)
        self.pages = pages

    #  Создаем Setter для фильтрации подающихся значений
    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, actual_pages: int):
        if not isinstance(actual_pages, int):
            raise TypeError("Значение должно быть типа int")
        if actual_pages <= 0:
            raise ValueError("Значение должно быть больше 0")
        self._pages = actual_pages

    #  Для добавления параметра из вложенного класса необходимо в любом случае использовать перегрузку
    #  Вопрос касается целесообразности для отображения пользователю количества страниц
    #  Если отображение необходимо, следует перегрузить параметр следующим образом
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.pages} стр."
    #  При отсутствии необходимости, следует унаследовать данный метод из базового класса, т.е
    #  не прописывать в данном классе

    #  Для анализа машиной необходимо учитывать все параметры класса,таким образом следует обязательно перегрузить метод
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self._pages})"


class AudioBook(Book):
    """Класс, описывающий аудиокнигу"""
    def __init__(self, name: str, author: str, duration: float):
        """
        Инициализирует параметры класса AudioBook
        :param name: Наименование книги (из базового класса)
        :param author: Автор книги (из базового класса)
        :param duration: Продолжительность книги в часах
        """
        super().__init__(name, author)
        self.duration = duration

    #  Создаем Setter для фильтрации подающихся значений
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, actual_duration: float):
        if not isinstance(actual_duration, float):
            raise TypeError("Значение должно быть типа float")
        if actual_duration <= 0.0:
            raise ValueError("Значение должно быть больше 0")
        self._duration = actual_duration

    #  Для добавления параметра из вложенного класса необходимо в любом случае использовать перегрузку
    #  Вопрос касается целесообразности для отображения пользователю количества страниц
    #  Если отображение необходимо, следует перегрузить параметр следующим образом
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration} ч."

    #  При отсутствии необходимости, следует унаследовать данный метод из базового класса, т.е
    #  не прописывать в данном классе

    #  Для анализа машиной необходимо учитывать все параметры класса,таким образом следует обязательно перегрузить метод
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self._duration})"


if __name__ == '__main__':
    Donny_Book = PaperBook("Как быть крутым и еще президентом", "Дональд Трамп", 1)  # Книга в процессе написания
    print(str(Donny_Book))
    Donny_Book.pages = 2  # Книга дописана
    print(repr(Donny_Book))

    Donny_Audio = AudioBook("Как быть крутым и еще президентом", "Дональд Трамп", 0.1)
    # Скоро будет озвучена полная версия
    print(str(Donny_Audio))
    Donny_Audio.duration = 0.15  # Озвучка бестселлера окончена
    print(repr(Donny_Audio))

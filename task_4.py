class Game:
    """
    Описывает основные параметры игры
    Является базовым классом
    """
    def __init__(self, name: str, author: str, durability: float):
        """
        Инициализирует параметры, обязательные для дочерних классов
        Подготавливает к работе класс Game
        :param name: Указывается название игры
        :param author: Указывается автор игры
        :param durability: Указывается длительность геймплея (в часах)
        """
        self.__name = name
        if not isinstance(self.__name, str):
            raise TypeError("This parameter should have 'str' type")

        self.__author = author
        if not isinstance(self.__author, str):
            raise TypeError("This parameter should have 'str' type")

        self.__durability = durability
        if not isinstance(self.__durability, float):
            raise TypeError("This parameter should have 'float' type")
        if self.__durability <= 0:
            raise ValueError("This parameter value should be > 0")

    @property
    def name(self) -> str:
        """
        Getter для параметра name
        Вводится для запрета изменения названия у существующей игры
        :return: Значение параметра self._name
        """
        return self.__name

    @property
    def author(self) -> str:
        """
        Getter для параметра author
        Вводится для запрета изменения автора у существующей игры
        :return: Значение параметра self._author
        """
        return self.__author

    @property
    def durability(self) -> float:
        """
        Getter для параметра durability
        Вводится для запрета изменения продолжительности существующей игры (с учетом всех DLC)
        :return: Значение параметра self._durability
        """
        return self.__durability

    def your_progress(self, try_number: int, your_gameplay_time: float) -> str:
        """
        Наследуется дочерними классами
        Вычисляет прогресс игрока, основываясь на его времени забега с учетом первой попытки
        :param try_number: Указывается номер попытки
        :param your_gameplay_time: Указывается время забега (в часах)
        :raise TypeError: Номер попытки не формата int
        :raise ValueError: Номер попытки <= 0
        :raise TypeError: Время забега не формата float
        :raise TypeError: Время забега < 0
        :return:
        """
        if not isinstance(try_number, int):
            raise TypeError("This parameter should have 'int' type")
        if try_number <= 0:
            raise ValueError("This parameter value should be > 0")

        if not isinstance(your_gameplay_time, float):
            raise TypeError("This parameter should have 'float' type")
        if your_gameplay_time < 0:
            raise ValueError("This parameter value should be >= 0")

        if try_number == 1:
            if your_gameplay_time > self.__durability * 2.5:
                raise ValueError("Nobody loves you, nasty cheater")
            return f'You have completed {your_gameplay_time * 100 / (self.__durability * 3)}% of game'
        else:
            if your_gameplay_time > self.__durability:
                raise ValueError("Nobody loves you, nasty cheater")
            return f'You have completed {your_gameplay_time*100 /self.__durability}% of game'

    @staticmethod
    def guide_book() -> str:
        """
        Перегружается в дочерних классах
        Прикладывается описание к игре
        """
        guide = guide_0
        return guide

    def __str__(self):  # Метод наследуется в дочерних классах
        return f"You're playing {self.name} by {self.author} now"

    def __repr__(self):  # Метод наследуется в дочерних классах ввиду отсутствия дополнительных параметров
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, " \
               f"durability={self.durability!r})"


class SekiroShadowsDieTwice(Game):
    """Описывается игра Sekiro:Shadows Die Twice."""
    def __init__(self, name: str, author: str, durability: float):
        """
        Является дочерним от класса Game
        Все параметры базового класса наследуются
        Инициализирует параметры класса SekiroShadowsDieTwice и подгатавливает его к работе
        """
        super().__init__(name=name, author=author, durability=durability)

    @staticmethod
    def guide_book() -> str:
        """Метод из базового класса перегружается"""
        guide = guide_0 + guide_1
        return guide


class DevilMayCry3(Game):
    """Описывается игра Devil May Cry 3. Dante's Awakening."""
    def __init__(self, name: str, author: str, durability: float):
        super().__init__(name, author, durability)

    @staticmethod
    def guide_book() -> str:
        """Метод из базового класса перегружается"""
        guide = guide_0 + guide_2
        return guide


guide_0 = "I glad to welcome you to this game. Followed by a must-read description."
guide_1 = "\nGood choice, bruh. So, your goal on first 5 minutes is not ti die, if you would can lol.\n" \
          "If you are, you are loser and close the game for saving your nerves, but if you're not, " \
          "also close this, man, i'm not joking, keeping time with your friends, or, if find the \n" \
          "girlfriend if you want to lost your nerves. \nShe's like this game in terms of destruction" \
          "your psyche."
guide_2 = "\nThis is really a good game. \nIf you don't die in the first mission, you will die in the next one. " \
          "\nBecause game developers are merciless to gamers and put the boss on the second level. " \
          "\nHe is really easy to kill, but my hands are crooked, and I killed him the third time. " \
          "\nBut I believe in you, just pass the first level. And remember - even the devil may cry " \
          "when he losing a loved one."


if __name__ == "__main__":
    Sekiro = SekiroShadowsDieTwice("", "", 0.1)
    Sekiro._Game__name = "Sekiro:Shadows Die Twice."
    Sekiro._Game__author = "Hidetaka Miyazaki."
    Sekiro._Game__durability = 30.0
    print(str(Sekiro))
    print(repr(Sekiro))
    print(Sekiro.your_progress(1, 70.0))
    print(Sekiro.guide_book())
    DMC3 = DevilMayCry3("", "", 0.1)
    DMC3._Game__name = "Devil May Cry 3. Dante's Awakening."
    DMC3._Game__author = "Hideaki Itsuno."
    DMC3._Game__durability = 55.0
    print(str(DMC3))
    print(repr(DMC3))
    print(DMC3.your_progress(3, 45.0))
    print(DMC3.guide_book())
    pass

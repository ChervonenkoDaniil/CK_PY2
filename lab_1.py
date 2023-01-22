# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Character:
    """
    Описывает характеристики персонажа данного недорпг
    """
    def __init__(self, health, mana, level: int):
        """
        Инициализирует параметры класса Character
        Создает и подготавливает к работе данный класс

        :param health: Параметр здоровья персонажа
        :param mana: Параметр маны персонажа
        :param level: Параметр уровня персонажа
        """

        if not isinstance(health, int):
            raise TypeError('Здоровье - это деньги, а деньги - это число')
        if health < 0:
            raise ValueError('Здоровье должно быть больше или равно 0, ниже некуда')
        self.char_health = health

        if not isinstance(mana, int):
            raise TypeError('Мана - это зелья, а зелья - это деньги, а деньги - это число')
        if mana < 0:
            raise ValueError('Мана должна быть больше или равна 0, ниже некуда')
        self.char_mana = mana

        if not isinstance(level, int):
            raise TypeError('Уровень - это прогресс, а прогресс требует денег, а деньги - это число')
        if level < 1:
            raise ValueError('Прогресс должен с чего-то начинаться, так начнем же с единицы')
        self.char_level = level

    def everyone_dies(self) -> str:
        """
        Сообщает, жив ли персонаж, или мертв

        :return: Выводит надпись "You died hehehe", если игрок умер, и надпись "You haven't died yet, soldier", если нет

        Примеры:
        >>> Lost_Soul_Low_Skill = Character(0, 100, 50)
        >>> Lost_Soul_Low_Skill.everyone_dies()
        'You died hehehe'
         """
        return 'You died hehehe' if self.char_health == 0 else "You haven't died yet, soldier"

    def fireball_cast(self, mana_to_spell=50) -> str:
        """
        Описывает заклинание "Fireball"

        :param mana_to_spell: Количество маны для каста заклинания "Fireball"
        :return: Выводит надпись 'You will burn twice: now and in the Hell', если на заклинание хватает маны,
                 или 'OH SHUT I BURN MYSELF', если нет. В обоих случаях выводит текущее количество маны

        Примеры:
        >>> Lost_Soul_Low_Skill = Character(0, 0, 50)
        >>> Lost_Soul_Low_Skill.fireball_cast()
        'OH SHUT I BURN MYSELF, current mana value = 0'
        >>> Lost_Soul_Low_Skill = Character(0, 100, 50)
        >>> Lost_Soul_Low_Skill.fireball_cast()
        'You will burn twice: now and in the Hell, current mana value = 50'
        """
        return 'OH SHUT I BURN MYSELF, current mana value = ' + str(int(self.char_mana)) \
                if self.char_mana < mana_to_spell else \
                'You will burn twice: now and in the Hell, current mana value = ' + \
                str(int(self.char_mana - mana_to_spell))

    def farming_creeps_and_level_increase(self, lvl_you_need: int, lvl_1_health=100, lvl_1_mana=100) -> str:
        """
        Описывает характеристики персонажа после бессмысленных и зверских убийств мельньких мобиков

        :param lvl_you_need: уровень, ради которого бедные мобики умирали от руки персонажа
        :param lvl_1_health: Базовое значение здоровья персонажа на 1 уровне
        :param lvl_1_mana: Базовое значение маны персонажа на 1 уровне
        :raise TypeError: Если значение необходимого уровня указано не числом
        :raise ValueError: Если значение уровня персонажа больше необходимого
        :raise ValueError: Если значение здоровья персонажа на каждом уровне больше заложенного этого недорпг
        :raise ValueError: Если значение маны персонажа на каждом уровне больше заложенного этого недорпг
        :return: Возвращает информацию о текущем состоянии игрока

        Примеры:
        >>> Lost_Soul_Low_Skill = Character(15, 10, 4)
        >>> Lost_Soul_Low_Skill.farming_creeps_and_level_increase(6)
        '496 HP 318 MP 6 LVL DEAD BODIES = 21'
        """
        if not isinstance(lvl_you_need, int):
            raise TypeError('Уровень - это прогресс, а прогресс требует денег, а деньги - это число')
        if self.char_level > lvl_you_need:
            raise ValueError('Ты убил слишком многих для того, чтобы начать деградировать?')
    
        counter_of_future_victims = 0  # Вводим количество будущих жертв, которые будут убиты персонажем\
    # для апгрейда уровня с текущего до необходимого
        while self.char_level != lvl_you_need:  # Запускаем цикл увеличения уровня с текущего на необходимый
            mobs = 6 + self.char_level  # Увеличиваем количество бедных мобиков, неоходимых для лвлапа
            counter_of_future_victims += mobs  # Увеличиваем количество мобиков, которые будут убиты во имя прогресса
            while mobs != 0:  # ДА НАЧНЕТСЯ РЕЗНЯ
                mobs -= 1
            self.char_level += 1  # После резни персонаж увеличивает уровень
            self.char_health *= 1.05 * self.char_level  
            # Здоровье персонажа не восстанавливается, но увеличивается на коэффициент 1.05 * текущий уровень игрока
            self.char_mana *= 1.03 * self.char_level
            # Мана персонажа не восстанавливается, но увеличивается на коэффициент 1.03 * текущий уровень игрока
            if self.char_health > lvl_1_health * 1.05 * self.char_level or\
                self.char_mana > lvl_1_mana * 1.03 * self.char_level:
                raise ValueError('Читер уходи ты не нужен')  # Проверка на читы
            # Проблема заключается именно в данных проверках - при условии, если на как минимум одном уровне здоровье и/ 
            # /или мана персонажа будут превышать значения, основанные на их установленных показателях на 1 уровне и 
            # дальнейшем их изменении с учетом коэффициентов приведения, то игрок - читер, так как каким то образом
            # изменил свои характеристики и законы их увеличения
            # Суть проблемы - при записи описания метода через заглушки, следует ли соблюдать табуляцию проверок
            # То есть первые две проверки, касающиеся параметра lvl_you_need остаются на уровне 3 данного документа, 
            # а третья проверка по логике должна переноситься на уровень 4, так как мошенничество может произойти
            # на любом из лвлов игрока, с добавлением перед ней заглушки от создания параметра counter_of_future_victims
            # Или эти проверки должны быть расположены также на разных уровнях, но без создания заглушек?
            # Или их можно расположить на одном уровне в цикле while self.char_level != lvl_you_need?
            # Тогда стоит ли ставить несколько заглушек, как обозначение промежутков между проверками?

        return str(int(self.char_health)) + ' HP ' + str(int(self.char_mana)) + ' MP ' + str(int(self.char_level)) \
               + ' LVL DEAD BODIES = ' + str(int(counter_of_future_victims))


class Weapon:
    """
    Описывает характеристики оружия персонажа
    """
    def __init__(self, damage, durability: int):
        """
        Инициализирует параметры класса Weapon
        Создает и подготавливает к работе данный класс

        :param damage: Параметр урона оружием
        :param durability: Параметр прочности оружия
        """

        if not isinstance(damage, int):
            raise TypeError("Урон определяется числом")
        if damage < 0:
            raise ValueError("Урон должен быть больше или равнятся 0")
        self.weapon_damage = damage

        if not isinstance(durability, int):
            raise TypeError("Прочность оружия определяется числом")
        if durability < 0 or durability > 100:
            raise ValueError("Прочность оружия должна быть больше или равняться 0")
        self.weapon_durability = durability

    def weapon_upgrade(self) -> str:
        """
        Изменяет урон и прочность оружия

        :return: Выводит сообщение о том, что оружие улучшено, его текущий урон и прочность
        """
        ...
        return 'Your stick is upgraded to M4A4: damage-' + str(self.weapon_damage) + ', durability-' + \
               str(self.weapon_durability) + '. Now you can kill mobs easily. Good luck, Butcher.'

    def weapon_destruction(self) -> str:
        """
        Уведомляет о том, что оружие сломано

        :return: Выводит сообщение о том, что оружие улучшено, его текущий урон и прочность
        Примеры:
        >>> Stick_of_Truth = Weapon(100,0)
        >>> Stick_of_Truth.weapon_destruction()
        'Your weapon is destroyed! Find a new weapon quickly.'
        """
        return 'Your weapon is destroyed! Find a new weapon quickly.' if self.weapon_durability == 0 else None


class Armour:
    """
    Описывает характеристики брони персонажа
    """
    def __init__(self, capacity, damage_resistance: int):
        """
        Инициализирует параметры класса Armour
        Создает и подготавливает к работе данный класс

        :param capacity: Параметр емкости брони
        :param damage_resistance: Параметр сопротивления урону брони
        """

        if not isinstance(capacity, int):
            raise TypeError("Прочность брони определяется числом")
        if capacity < 0 or capacity > 100:
            raise ValueError("Прочность брони быть больше или равняться 0")
        self.armour_capacity = capacity

        if not isinstance(damage_resistance, int):
            raise TypeError("Сопротивление к урону определяется числом")
        if damage_resistance < 0 or damage_resistance > 100:
            raise ValueError("Сопротивление к урону должно быть в пределах от 0 до 100")
        self.damage_resistance = damage_resistance

    def armour_cleaning(self) -> str:
        """
        Увеличивает атрибут емкости брони на 20
        Если self.armour_capacity >= 80, увеличивает значение до максимального (100)

        :return: Выводит сообщение о увеличении атрибута емкости брони

        Примеры:
        >>> Chum_Bucket = Armour(1, 15)
        >>> Chum_Bucket.armour_cleaning()
        'You clean your armour! Capacity = 21'
        """
        return 'You clean your armour! Capacity = ' + str(self.armour_capacity + 20) if self.armour_capacity < 80 else \
                'You clean your armour! Capacity = 100'

    def the_revenge_of_mobs(self, cobolt_atack: bool) -> str:
        """
        Уменьшает значение сопротивления к урону из-за царапины на доспехе

        :param cobolt_atack: Подкрался ли к персонажу подлый кобальт и поцарапал ли он доспех персонажа
        :return: Царапина довольно сильная, так что уведомляет игрока, что сопротивление урону равно 0"

        Примеры:
        >>> Chum_Bucket = Armour(100,100)
        >>> Chum_Bucket.the_revenge_of_mobs(True)
        'Vile cobolt scratched your armour. Your damage resistanse equals 0'
        """
        return 'Vile cobolt scratched your armour. Your damage resistanse equals 0' if cobolt_atack is True else None


if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

import doctest

class teacher:

    def __init__(self, surname: str = None, num_of_les_p_day: int = None):
        """
        Создание объекта класса "teacher":
        :param surname: фамилия преподавателя
        :param num_of_les_p_day: количество пар в день
        Пример:
        >>> teacher0 = teacher("Rozov", 3)
        """
        self.add_data(surname, num_of_les_p_day)

    def add_data(self, surname: str = None, num_of_les_p_day: int = None):
        """
        Добавление данных в объект:
        :param surname: фамилия преподавателя
        :param num_of_les_p_day: количество пар в день
        """
        self.surname = surname
        if num_of_les_p_day >= 0:
            self.num_of_les_p_day = num_of_les_p_day
        else:
            raise ValueError("Количество пар не может быть отрицательным")
    def print_data(self):
        print(self.surname, self.num_of_les_p_day)


class bird:

    def __init__(self, name: str = None, age: int = None, breed: str = None):
        """
        Создание объекта класса "bird":
        :param name: имя птици (str)
        :param age: возраст птици (int)
        :param breed: порода птици (str)

        Примеры:
        >>> bird1 = bird("keha", 3, "parrot")
        """
        self.add_data(name, age, breed)

    def add_data(self, name: str = None, age: int = None, breed: str = None):
        """
        Функция добавления данных в объект

        :param name: имя птици (str)
        :param age: Возраст птици (int)
        :param breed: порода птици (str)
        """
        self.name = name
        if age >= 0:
            self.age = age
        else:
            raise ValueError("Значение не может быть отрицательным")
        self.breed = breed

    def print_data(self):
        print(self.name, self.age, self.breed)



class student:

    def __init__ (self, surname: str = None, course: int = 0, list_in_un: bool = False):
        """
        Создание объета класса "student":
        :param surname: фамилия студента
        :param course: курс обучения студента
        :param list_in_un: числится ли в университете
        Пример:
        >>> student0 = student("Strelkov", 2, True)
        """
        self.add_data(surname, course, list_in_un)

    def add_data (self, surname: str = None, course: int = 0, list_in_un: bool = None):
        """
        Добавление данных в объект:
        :param surname: фамилия студента
        :param course: курс обучения студента
        :param list_in_un: числится ли в университете
        """
        self.surname = surname
        if course >= 0:
            self.course = course
        else:
            raise ValueError("Значение не может быть отрицательным")
        self.list_in_un = list_in_un
        if self.course > 4:
            self.list_in_un = False

    def print_data(self):
        print(self.surname, self.course, self.list_in_un)

class Human:
    def __init__(self, name, surname, age):
        """
        Создание объекта класса "Human":
        :param name: Имя человека (str)
        :param surname: Фамилия человека (str)
        :param age: Возраст человека (int)
        Пример:
        >>> human1 = Human("Arsenii", "Strelkov", 20)
        """
        # Проверки для имени
        if not isinstance(name, str):
            raise TypeError("Некорректное имя")
        if not name.isalpha():
            raise ValueError("Имя может содержать только буквы")
        if name[0].islower():
            raise ValueError("Имя должно начинаться с большой буквы")
        self.name = name

        # Проверки для фамилии
        if not isinstance(surname, str):
            raise TypeError("Фамилия введена некорректно")
        if not surname.isalpha():
            raise ValueError("Фамилия может содержать только буквы")
        if surname[0].islower():
            raise ValueError("Фамилия должна начинаться с большой буквы")
        self.surname = surname

        # Проверки для возраста
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        if age > 150:
            raise ValueError("Слишком большой возраст")
        self.age = age

    def __str__(self):
        return f"Имя: {self.name}, Фамилия: {self.surname}, Возраст: {self.age} лет"

    def __repr__(self):
        return f"Human({self.name!r}, {self.surname!r}, {self.age!r})"


class Student(Human):
    def __init__(self, name, surname, age, course=0):
        """
        Создание объекта класса "Student":
        :param course: Курс студента (int)
        Пример:
        >>> student1 = Student("Arsenii", "Strelkov", 20, 2)
        """
        super().__init__(name, surname, age)
        # Проверки для курса
        if not isinstance(course, int):
            raise TypeError("Курс должен быть целым числом")
        if course < 0:
            raise ValueError("Курс не может быть отрицательным")
        if course > 4:
            raise ValueError("Студент не может быть выше 4 курса")
        self.course = course

    def __str__(self):
        return super().__str__() + f", Курс: {self.course}"

    def __repr__(self):
        return f"Student({self.name!r}, {self.surname!r}, {self.age!r}, {self.course!r})"


class Teacher(Human):
    def __init__(self, name, surname, age, numoflessons=0):
        """
        Создание объекта класса "Teacher":
        :param numoflessons: Количество пар в неделю (int)
        Пример:
        >>> teacher1 = Teacher("Sergey", "Rozov", 56, 2)
        """
        super().__init__(name, surname, age)
        # Проверки для количества пар
        if not isinstance(numoflessons, int):
            raise TypeError("Количество пар должно быть целым числом")
        if numoflessons < 0:
            raise ValueError("Количество пар не может быть отрицательным")
        self.numoflessons = numoflessons

    def __str__(self):
        return super().__str__() + f", Количество пар: {self.numoflessons}"

    def __repr__(self):
        return f"Teacher({self.name!r}, {self.surname!r}, {self.age!r}, {self.numoflessons!r})"
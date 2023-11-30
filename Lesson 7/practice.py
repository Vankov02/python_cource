class Contact:
    def __init__(self, surname, name, phone_number):
        self.__surname = surname
        self.__name = name
        self.__phone_number = phone_number

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self.__phone_number = phone_number


human_1 = Contact("Масленников", "Иван", "79635754684")
print(human_1.phone_number)
print(human_1.name)
human_1.phone_number = "89635751847"
print(human_1.phone_number)
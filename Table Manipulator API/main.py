class Person():
    startAge = 18
    endAge = 60

    def __init__(self, name, surname, age=25):
        self.name = name
        self.surname = surname
        self.age = age
        self.isValidated = False
        if Person.validate(age):
            self.isValidated = True

    def __str__(self):
        return 'person name = ' + self.name

    def get_fio(self):
        return self.name + ' ' + self.surname

    @classmethod
    def validate(cls, age):
        return cls.startAge < age < cls.endAge

    def display_info(self):
        print(self)
        print('validated - ' + str(self.isValidated))

t = Person
p1 = Person('danek', 'ivanov')
p2 = Person('mark', 'nosatov', 16)
p2.display_info()
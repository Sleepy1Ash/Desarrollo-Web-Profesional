class Student:

    count = 0

    def __init__(self, name, age, language, city):
        self.name = name
        self.age = age
        self.language = language
        self.city = city
        Student.count += 1

    def __str__(self):
        return f'Name:{self.name},Age:{self.age},Lenguaje: {self.language},Ciudad: {self.city}'

    @staticmethod
    def get_total_students():
        return Student.count

    @classmethod
    def get_total_students_class(cls):
        return cls.count

if __name__ == '__main__':
    estudiante = Student('Juan',21,'Python', 'Lerma')
    print(Student.get_total_students())
    print(Student.get_total_students_class())
    estudiante.name = 'Josesito'
    #print(estudiante)

    estudiante_2 = Student('Ana', 21, 'Python', 'Lerma')
    print(Student.get_total_students())
    print(Student.get_total_students_class())
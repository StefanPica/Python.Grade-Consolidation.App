class Medie(object):
    def __init__(self, nume_student, medie):
        self.__nume_student = nume_student
        self.__medie = medie

    def get_nume_student(self):
        return self.__nume_student

    def get_medie(self):
        return self.__medie

    def __str__(self):
        return "Studentul: " + str(self.__nume_student) + " are media notelor: " + str(self.__medie)


class Student(object):
    def __init__(self, id_student, nume_student):
        self.__id_student = id_student
        self.__nume_student = nume_student

    def get_id_student(self):
        return self.__id_student

    def get_nume_student(self):
        return self.__nume_student

    def set_nume_student(self, value):
        self.__nume_student = value

    def __eq__(self, other):
        return self.__id_student == other.__id_student

    def __str__(self):
        return "[" + str(self.__id_student) + "] " + self.__nume_student

class Discipline(object):

    def __init__(self, id_disciplina, nume_disciplina, profesor_disciplina):
        self.__id_disciplina = id_disciplina
        self.__nume_disciplina = nume_disciplina
        self.__profesor_disciplina = profesor_disciplina

    def get_id_disciplina(self):
        return self.__id_disciplina

    def get_nume_disciplina(self):
        return self.__nume_disciplina

    def get_profesor_disciplina(self):
        return self.__profesor_disciplina

    def set_nume_disciplina(self, value):
        self.__nume_disciplina = value

    def set_profesor_disciplina(self, value):
        self.__profesor_disciplina = value

    def __eq__(self, other):
        return self.__id_disciplina == other.__id_disciplina

    def __str__(self):
        return "[" + str(self.__id_disciplina) + "] " + self.__nume_disciplina + " Profesorul: " + self.__profesor_disciplina

class Medie_Dis(object):
    def __init__(self, disciplina, medie):
        self.__disciplina = disciplina
        self.__medie = medie

    def get_disciplina(self):
        return self.__disciplina

    def get_profesor_disciplina(self, disciplina):
        return disciplina.get_profesor_disciplina()

    def get_medie(self):
        return self.__medie

    def __str__(self):
        return "Disciplina: " + str(self.__disciplina) + " are media notelor: " + str(self.__medie)
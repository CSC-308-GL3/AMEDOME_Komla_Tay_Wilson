class Grade:
    def __init__(self, code, libelle, taux):
        self.__code = code
        self.__libelle = libelle
        self.__taux = taux

    def getCode(self):
        return self.__code

    def getLibelle(self):
        return self.__libelle

    def tauxHoraire(self):
        return self.__taux


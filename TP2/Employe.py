from datetime import datetime


class Employe:
    def __init__(self, numero, nom, grade, dateEmbauche):
        self.__numero = numero
        self.__nom = nom
        self.__grade = grade
        self.__dateEmbauche = datetime.strptime(dateEmbauche, '%d/%m/%Y')

    def coutHoraire(self):
        anciennete = self.getAnciennete()
        tauxHoraire = self.__grade.tauxHoraire()

        if anciennete <= 5:
            return tauxHoraire * 1.05
        elif anciennete <= 10:
            return tauxHoraire * 1.08
        else:
            return tauxHoraire * 1.12

    def getNumero(self):
        return self.__numero

    def getNom(self):
        return self.__nom

    def getQualification(self):
        return self.__grade

    def getDateEmbauche(self):
        return self.__dateEmbauche

    def getAnciennete(self):
        today = datetime.now()
        delta = today - self.__dateEmbauche
        return int(delta.days // 365)
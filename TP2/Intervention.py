from datetime import datetime 


class Intervention:
    def __init__(self, numero, date, duree, tarifKm, technicien):
        self.__numero = numero
        self.__date = datetime.strptime(date, '%d/%m/%Y')
        self.__duree = int(duree)
        self.__tarifKm = float(tarifKm)
        self.__technicien = technicien

    def fraisKm(self, dist):
        return self.__tarifKm * dist

    def fraisMo(self):
        coutHoraire = self.__technicien.coutHoraire()
        dureeTotale = self.__duree + 59  
        return coutHoraire * (dureeTotale // 60 + 1)

    def affiche(self):
        print("Intervention n°{}, date : {}, duree : {} min".format(self.__numero, self.__date.strftime('%d/%m/%Y'), self.__duree))
        print("Technicien : {} ({})".format(self.__technicien.getNom(), self.__technicien.getQualification().getLibelle()))

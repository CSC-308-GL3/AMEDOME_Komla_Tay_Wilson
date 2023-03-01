class Client:
    def __init__(self, numero, nom, adresse, codePostal, ville, nbKm):
        self.__numero = numero
        self.__nom = nom
        self.__adresse = adresse
        self.__codePostal = codePostal
        self.__ville = ville
        self.__nbKm = nbKm

    def distance(self):
        return self.__nbKm
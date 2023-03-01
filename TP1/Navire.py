class Navire:
    def __init__(self, noNavire, nomNavire, libelleFret, qteFret):
        self._noNavire = noNavire,
        self._nomNavire = nomNavire,
        self._libelleFret = libelleFret,
        self._qteFret = qteFret

    ##Fonction obtenirQuantiteFret
    def obtenirQteFret(self):
        return self._qteFret

    ##Fonction decharger
    def decharger(self, qte):
        self._qteFret -= qte

    ##Fonction estDecharge
    def estDecharge(self):
        return self._qteFret == 0
        

    
        
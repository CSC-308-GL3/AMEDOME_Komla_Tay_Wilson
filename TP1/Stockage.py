class Stockage:

    def __init__(self, capaMax, capaDispo=-1):
        self._capaMax = capaMax
        if capaDispo == -1:
            self._capaDispo = capaMax
        else:
            self._capaDispo = capaDispo

    def getCapaDispo(self):
        return self._capaDispo

    def setCapaDispo(self, capaDispo):
        self._capaDispo = capaDispo

    def getCapaMax(self):
        return self._capaMax

    def stocker(self, qte):
        self._capaDispo -= qte

    def estVide(self):
        return self._capaDispo == self._capaMax

    def estRemplie(self):
        return self._capaDispo == 0

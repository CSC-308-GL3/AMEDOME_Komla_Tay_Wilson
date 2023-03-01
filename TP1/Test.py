from Navire import Navire
from Port import Port
from Stockage import Stockage


class Test:
    def __init__(self):
        self.port = Port()
        self.esmeralda = Navire("0092493603", "ESMERALDA", "sac de riz", 1000)

        hangar1 = Stockage(1000)
        hangar1.capaDispo = 500  # Rempli à moitié
        hangar2 = Stockage(1000)
        hangar2.capaDispo = 750  # Rempli au quart

        silo1 = Stockage(100)
        silo2 = Stockage(200)
        silo3 = Stockage(300)

        self.port.ajouteStockage(silo1)
        self.port.ajouteStockage(silo2)
        self.port.ajouteStockage(silo3)
        self.port.ajouteStockage(hangar1)
        self.port.ajouteStockage(hangar2)
        
        self.port.dechargement(self.esmeralda)

test = Test()
class Port:
    def __init__(self):
        self.tabStock = []

    def ajouteStockage(self, stockage):
        self.tabStock.append(stockage)

    def trouverZoneStockage(self, qte):
        for stockage in self.tabStock:
            if stockage.getCapaDispo >= qte:
                return stockage
        raise ValueError("Aucune zone de stockage n'a assez de capacité disponible")

    def dechargement(self, unNavire):
        qteRestante = unNavire.obtenirQteFret()
        
        for stockage in self.tabStock:
            qteMax = stockage.getCapaDispo()
            if qteRestante <= 0:
                break
            elif qteRestante <= qteMax:
                stockage.stocker(qteRestante)
                qteRestante = 0
            else:
                stockage.stocker(qteMax)
                qteRestante -= qteMax
        
        if qteRestante == 0:
            print(f"Déchargement réussi : {unNavire.obtenirQteFret()} déchargé.")
        else:
            print(f"Déchargement partiel : {unNavire.obtenirQteFret()} partiellement déchargé. Quantité restante : {qteRestante}")
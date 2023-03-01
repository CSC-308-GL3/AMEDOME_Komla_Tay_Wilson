class Contrat:
    def __init__(self, numero, date, client, montantContrat, interventions, nbIntervention):
        self.__numero = numero
        self.__date = date
        self.__client = client
        self.__montantContrat = montantContrat
        self.__interventions = interventions
        self.__nbIntervention = nbIntervention

    def montant(self):
        return self.__montantContrat

    def ecart(self): 
        coutKm = sum([intervention.fraisKm(self.__client.distance()) for intervention in self.__interventions])
        coutMo = sum([intervention.fraisMo() for intervention in self.__interventions])
        return self.__montantContrat - (coutMo + coutKm)


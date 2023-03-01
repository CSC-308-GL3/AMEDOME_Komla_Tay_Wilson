from Client import Client
from Employe import Employe
from Grade import Grade
from Intervention import Intervention
from Contrat import Contrat


grade1 = Grade(32,"Technicien Informaticien",1000)
employe1 = Employe(1,"ABALO",grade1,"01/01/2021" )


intervention1 = Intervention(123,"01/01/2023",8,100,employe1)
intervention2 = Intervention(124,"03/01/2023",4,100,employe1)

client1 = Client(1,"HONO","Totsi","BB345","Lomé",3)


contrat1 = Contrat(12,"03/01/2023",client1,100000,[intervention1,intervention2],2)



ecart = contrat1.ecart()


print("L'écart est de", ecart, " de francs cfa.")

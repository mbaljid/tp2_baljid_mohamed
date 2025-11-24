from Bank import CompteBancaire
from Bank import Client
import time
cli = Client("Yassir")
cli.compte.deposer(2000)
time.sleep(2)
cli.compte.retirer(150)
print(cli.compte)
print("Solde accessible (lecture) :", cli.compte.solde)
cli.compte.operationshow()
cli.afficher()

#cli.compte.solde=500

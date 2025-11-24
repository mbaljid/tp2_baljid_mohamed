from datetime import datetime
class CompteBancaire :
    def __init__(self, titulaire, sold_initial=0):
        self._titulaire=titulaire
        self.__solde=sold_initial
        self._operations=[]

    #method de deposer    
    def deposer(self, montant):
        if montant<=0:
            raise ValueError("\n error montant negative")
        else:
            self.__solde+=montant
            datetime_now=datetime.now().isoformat(timespec="seconds")
            self._operations.append(f"{datetime_now}:{self._titulaire}deposer:{montant}$")
    #method de retirer 
    def retirer(self, montant):
        if 0< montant < self.__solde:
            self.__solde-=montant
            datetime_now=datetime.now().isoformat(timespec="seconds")
            self._operations.append(f"\n{datetime_now}:{self._titulaire}retirer:{montant}$\n")
        else:   
            print("\n solde insuffisants ou montant invalide. ")
    #method pour le releve d'operations 
    def operationshow(self):
        for i in self._operations:
            print(i)
    
    
            
    @property
    def solde(self):
        return self.__solde
    
    def __str__(self):
        return f"Titulaire:{self._titulaire}, solde: {self.solde} $"
    




class Client:
    def __init__(self, nom):
        self.nom = nom
        self.compte = CompteBancaire(nom)

    def afficher(self):
        print(f"Client : {self.nom}, Solde : {self.compte.solde}$")
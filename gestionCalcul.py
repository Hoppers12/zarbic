from Pile import Pile

class Zarbic :

    def __init__(self):
        self.pile_valeur = Pile()

    def depiler_2_valeurs(self):
        return [self.pile_valeur.depiler(),self.pile_valeur.depiler()]

    def empiler(self,val):
        return self.pile_valeur.ajouter_valeur(val)

    def calculBinaire(self,val1,val2,operateur) :
        match operateur :
            case '+' :
                return self.pile_valeur.ajouter_valeur(val1 + val2)
            case '-':
                return self.pile_valeur.ajouter_valeur(val2 - val1)
            case '*':
                return self.pile_valeur.ajouter_valeur(val1 * val2)
            case '/':
                return self.pile_valeur.ajouter_valeur(val1 / val2)
            case _:
                "Opérateur inconnu"

    def afficherResultat(self):
        while not self.pile_valeur.empty():
            element = self.pile_valeur.depiler()
            print("Element dépilé : ", element)

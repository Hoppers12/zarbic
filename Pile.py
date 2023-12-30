

import queue  # Import de la classe queue

class Pile:
    def __init__(self):
        self.pile_colis = queue.LifoQueue()  # Création d'une pile

    def empty(self):
        return self.pile_colis.empty()
    def ajouter_valeur(self,valeur):
        return self.pile_colis.put(valeur)

    def depiler(self):
        return self.pile_colis.get()





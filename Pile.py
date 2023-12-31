

import queue  # Import de la classe queue
''' Classe qui permet de manipuler une pile'''
class Pile:
    ''' Constructeur de la classe '''
    def __init__(self):
        self.pile_colis = queue.LifoQueue()  # Création d'une pile

    ''' Fonction qui teste si la pile est vide'''
    def empty(self):
        return self.pile_colis.empty()
    ''' Fonction qui empile une valeur'''
    def ajouter_valeur(self,valeur):
        return self.pile_colis.put(valeur)

''' Fonction qui dépile'''
    def depiler(self):
        return self.pile_colis.get()





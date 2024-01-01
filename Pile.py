'''Importe la classee queue
qui permet de manipuler des piles/file
'''
import queue  # Import de la classe queue
''' La 
Classe qui permet de manipuler une pile
'''
class Pile:
    '''Le
        Constructeur de la classe '''
    def __init__(self):
        self.pile_colis = queue.LifoQueue()  # Création d'une pile

    ''' la
     Fonction qui teste si la pile est vide
    '''
    def empty(self):
        '''Cette méthode retourne si la pile est vide ou non'''
        return self.pile_colis.empty()
    ''' la
    Fonction qui empile une valeur
    '''
    def ajouter_valeur(self,valeur):
        '''Cette fonction ajoute un valeur dans la pile
        elle prend en paramètre la valeur a ajouter '''
        return self.pile_colis.put(valeur)

    ''' la 
     Fonction qui dépile
    '''
    def depiler(self):
        ''' Cette méthode dépile l'élément le plus haut de la pile'''
        return self.pile_colis.get()





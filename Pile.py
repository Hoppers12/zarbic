'''Importe la classee queue
qui permet de manipuler des piles/file
'''
import queue  # Import de la classe queue
 #Classe qui permet de manipuler une file

class Pile:
    """Une classe représentant une pile (stack) en informatique.

        Cette classe implémente les opérations de base d'une pile :
        - push : pour ajouter un élément au sommet de la pile.
        - pop : pour retirer l'élément du sommet de la pile.
        - peek : pour voir l'élément du sommet sans le retirer.
        - isEmpty : pour vérifier si la pile est vide.
        - size : pour obtenir la taille actuelle de la pile.

        Attributes:
        elements (list): Une liste contenant les éléments de la pile.
        """
    #Le constructeur de la pile
    def __init__(self):
        self.pile_colis = queue.LifoQueue()  # Création d'une pile

    #Fonction qui teste si la pile est vide
    def empty(self):
        """
           Retourne si la pile est vide ou non.
           Args : objet courant
       """
        return self.pile_colis.empty()
       #La fonction qui empile une valeur

    def ajouter_valeur(self,valeur):
        """Cette fonction ajoute un valeur dans la pile
        elle prend en paramètre la valeur a ajouter """
        return self.pile_colis.put(valeur)

    #Fonction qui dépile
    def depiler(self):
        """ Cette méthode dépile l'élément le plus haut de la pile"""
        return self.pile_colis.get()





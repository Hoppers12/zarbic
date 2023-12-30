from gestionFichier.gestionFichier import *
from gestionCalcul.gestionCalcul import Zarbic
from Pile import Pile

# Utilisation de la fonction pour lire un fichier.txt
nom_du_fichier = 'fichier.txt'
resultat = lire_fichier(nom_du_fichier)

tableau = contenu_en_tableau(nom_du_fichier)

print(tableau)
calcul = Zarbic()
#Pour chaque element du tableau on l'empile sauf si il s'agit d'un opérateur.
#Dans ce cas là on dépile 2 éléments et on fait l'opération entre eux
for element in tableau :

    if (element == '+' or element == '-' or element == '*' or element =='/'):
        val_a_depiler = calcul.depiler_2_valeurs()
        val1 = int(val_a_depiler[0])
        val2 = int(val_a_depiler[1])
        print(val1,val2)
        calcul.calculBinaire(val1,val2,element)
    else :
        calcul.empiler(element)

calcul.afficherResultat()
print("Fin du calcul")
"""
Ce module gère la lecture de fichiers.
"""
def lire_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as fichier:
            contenu = fichier.read()
            return contenu
    except FileNotFoundError:
        return "Le fichier.txt n'existe pas."
    except PermissionError as e:
        return f"Erreur de permission : {str(e)}"
    except IOError as e:
        return f"Erreur lors de la lecture du fichier : {str(e)}"

'''retourne le contenu ds un tableau'''
def contenu_en_tableau(nom_fichier):
    contenu = lire_fichier(nom_fichier)
    if contenu.startswith("Une erreur s'est produite"):
        return contenu  # Gérer le cas d'erreur de lecture du fichier

    #Diviser contenu en utilisant l'espace comme séparateur et ranger les éléments dans un tableau
    elements = contenu.split()
    # Cette méthode divise par défaut en utilisant les espaces comme séparateurs
    return elements

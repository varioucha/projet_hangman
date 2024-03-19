# Déclaration de la variable globale en dehors de la fonction
nombre_erreurs = 0

def ma_fonction():
    global nombre_erreurs  # Indique que nous utilisons la variable globale
    nombre_erreurs += 1  # Modification de la variable globale à l'intérieur de la fonction


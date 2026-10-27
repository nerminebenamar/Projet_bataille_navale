"""
User Story : "Plouf dans l'eau"
Utilisateur : un joueur.
Story : On veut pouvoir gérer les tirs de l'adversaire.
Actions :
    - créer une grille à 5 lignes et 8 colonnes
    - afficher la grille à l'écran
    - demander à l'utilisateur de rentrer deux coordonnées x et y
    - tirer à l'endroit indiqué sur la grille
    - retour en 2 
"""

from grille import Grille

# créer une grille à 5 lignes et 8 colonnes
grille = Grille(5, 8)

while True:
    # afficher la grille à l'écran
    print(grille)

    # demander à l'utilisateur de rentrer deux coordonnées x et y
    try:
        ligne = int(input("Ligne : "))
        colonne = int(input("Colonne : "))
    except ValueError:
        print("Merci d'entrer des nombres entiers.")
        continue

    if not grille.dans_grille(ligne, colonne):
        print("Coordonnées en dehors de la grille.")
        continue

    # tirer à l'endroit indiqué sur la grille
    grille.tirer(ligne, colonne)
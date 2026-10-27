"""
Jeu de bataille navale (version un joueur).

Une grille de 8 lignes x 10 colonnes est générée avec un bateau de chaque
type, placés aléatoirement sans chevauchement. Le joueur tire tour à tour
sur la grille jusqu'à ce que tous les bateaux soient coulés.
"""

import random

from termcolor import colored

from grille import Grille
from bateau import PorteAvions, Croiseur, Torpilleur, SousMarin

TOUCHE = '💣'

TYPES_DE_BATEAUX = [PorteAvions, Croiseur, Torpilleur, SousMarin]

MESSAGES_COULE = {
    "PorteAvions": "💥 Le porte-avions a coulé !",
    "Croiseur": "💥 Le croiseur a coulé !",
    "Torpilleur": "💥 Le torpilleur a coulé !",
    "SousMarin": "💥 Le sous-marin a coulé !",
}

# couleur associée à chaque type de case affichée
COULEUR_VIDE = "blue"
COULEUR_RATE = "white"
COULEUR_TOUCHE = "red"
COULEURS_BATEAUX = {
    "PorteAvions": "magenta",
    "Croiseur": "yellow",
    "Torpilleur": "cyan",
    "SousMarin": "green",
}


def positions_libres(grille, longueur, vertical):
    """
    Renvoie la liste des couples (ligne, colonne) valides pour placer un
    bateau de la longueur et de l'orientation données, sans dépasser de la
    grille ni chevaucher un bateau déjà présent.
    """
    candidats = []

    if vertical:
        for colonne in range(grille.colonnes):
            for ligne in range(grille.lignes - longueur + 1):
                cases = [(ligne + i, colonne) for i in range(longueur)]
                if all(grille.valeur(l, c) == grille.vide for (l, c) in cases):
                    candidats.append((ligne, colonne))
    else:
        for ligne in range(grille.lignes):
            for colonne in range(grille.colonnes - longueur + 1):
                cases = [(ligne, colonne + i) for i in range(longueur)]
                if all(grille.valeur(l, c) == grille.vide for (l, c) in cases):
                    candidats.append((ligne, colonne))

    return candidats


def placer_aleatoirement(grille, classe_bateau, longueur):
    """
    Place aléatoirement un bateau de la classe donnée sur la grille, parmi
    tous les emplacements (case, orientation) ne produisant aucun
    chevauchement, puis renvoie le bateau créé.
    """
    candidats = []
    for vertical in (True, False):
        for (ligne, colonne) in positions_libres(grille, longueur, vertical):
            candidats.append((ligne, colonne, vertical))

    ligne, colonne, vertical = random.choice(candidats)
    bateau = classe_bateau(ligne, colonne, vertical=vertical)
    grille.ajoute(bateau)
    return bateau


def afficher_pour_joueur(grille, bateaux):
    """
    Construit l'affichage tel que le joueur doit le voir : les bateaux non
    encore touchés restent invisibles, les impacts sont marqués, et un
    bateau coulé est révélé avec sa marque sur toutes ses cases.
    Chaque case est colorée avec termcolor.
    """
    taille = grille.lignes * grille.colonnes
    affichage = [colored(grille.vide, COULEUR_VIDE)] * taille

    # on reporte les tirs dans l'eau (ratés)
    for indice, case in enumerate(grille.grille):
        if case == 'x':
            affichage[indice] = colored('x', COULEUR_RATE)

    # on reporte les bateaux touchés / coulés
    for bateau in bateaux:
        if bateau.coulé(grille):
            couleur = COULEURS_BATEAUX[type(bateau).__name__]
            for (ligne, colonne) in bateau.positions():
                affichage[grille.indice(ligne, colonne)] = colored(
                    bateau.marque, couleur
                )
        else:
            for (ligne, colonne) in bateau.positions_touchees(grille):
                affichage[grille.indice(ligne, colonne)] = colored(
                    TOUCHE, COULEUR_TOUCHE
                )

    lignes_texte = []
    for ligne in range(grille.lignes):
        debut = ligne * grille.colonnes
        fin = debut + grille.colonnes
        lignes_texte.append(''.join(affichage[debut:fin]))
    return '\n'.join(lignes_texte)


def demander_coordonnees(grille):
    """Demande au joueur des coordonnées valides et les renvoie."""
    while True:
        try:
            ligne = int(input(colored(f"Ligne (0-{grille.lignes - 1}) : ", "cyan")))
            colonne = int(input(colored(f"Colonne (0-{grille.colonnes - 1}) : ", "cyan")))
        except ValueError:
            print(colored("Merci d'entrer des nombres entiers.", "red"))
            continue

        if not grille.dans_grille(ligne, colonne):
            print(colored("Coordonnées en dehors de la grille, réessayez.", "red"))
            continue

        return ligne, colonne


def jouer():
    grille = Grille(8, 10)

    bateaux = [
        placer_aleatoirement(grille, classe, classe(0, 0).longueur)
        for classe in TYPES_DE_BATEAUX
    ]

    coups = 0

    while any(not bateau.coulé(grille) for bateau in bateaux):
        print()
        print(afficher_pour_joueur(grille, bateaux))
        ligne, colonne = demander_coordonnees(grille)

        if grille.valeur(ligne, colonne) in ('x', TOUCHE):
            print(colored("Vous avez déjà tiré ici, choisissez une autre case.", "yellow"))
            continue

        coups += 1
        bateau_touche = None
        for bateau in bateaux:
            if (ligne, colonne) in bateau.positions():
                bateau_touche = bateau
                break

        if bateau_touche is not None:
            grille.tirer(ligne, colonne, touche=TOUCHE)
            print(colored("Touché !", "red", attrs=["bold"]))
            if bateau_touche.coulé(grille):
                nom_classe = type(bateau_touche).__name__
                print(colored(MESSAGES_COULE[nom_classe], COULEURS_BATEAUX[nom_classe], attrs=["bold"]))
        else:
            grille.tirer(ligne, colonne, touche='x')
            print(colored("Dans l'eau...", "blue"))

    print()
    print(afficher_pour_joueur(grille, bateaux))
    print(colored(f"🏆 Tous les bateaux sont coulés en {coups} coups !", "green", attrs=["bold"]))


if __name__ == "__main__":
    jouer()
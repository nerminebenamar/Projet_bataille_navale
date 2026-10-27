"""
Module bateau : représente un bateau, indépendamment de la grille sur
laquelle il sera placé, ainsi que ses différents types (sous-classes).
"""


class Bateau:

    marque = '⛵'  # marque par défaut affichée sur la grille

    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    def positions(self):
        """
        Renvoie la liste des positions (ligne, colonne) occupées par le
        bateau, rangée par lignes croissantes (si vertical) ou colonnes
        croissantes (si horizontal).
        """
        positions = []
        for i in range(self.longueur):
            if self.vertical:
                positions.append((self.ligne + i, self.colonne))
            else:
                positions.append((self.ligne, self.colonne + i))
        return positions

    def chevauche(self, other):
        """Indique si self et other occupent au moins une case commune."""
        return bool(set(self.positions()) & set(other.positions()))

    def touche(self, grille):
        """Indique si au moins une case du bateau a été touchée."""
        return any(
            grille.valeur(ligne, colonne) not in (grille.vide, self.marque)
            for (ligne, colonne) in self.positions()
        )
 
    def positions_touchees(self, grille):
        """Renvoie la liste des positions du bateau qui ont été touchées."""
        return [
            (ligne, colonne)
            for (ligne, colonne) in self.positions()
            if grille.valeur(ligne, colonne) not in (grille.vide, self.marque)
        ]
    
    def coulé(self, grille):
        """Indique si toutes les cases du bateau ont été touchées."""
        return all(
            grille.valeur(ligne, colonne) == 'x' for (ligne, colonne) in self.positions()
        )


class PorteAvions(Bateau):
    marque = "🚢"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=4, vertical=vertical)


class Croiseur(Bateau):
    marque = "⛴"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=3, vertical=vertical)


class Torpilleur(Bateau):
    marque = "🚣"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)


class SousMarin(Bateau):
    marque = "🐟"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)
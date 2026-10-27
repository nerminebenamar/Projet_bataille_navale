"""
Module grille : représente le terrain de jeu de la bataille navale.

La grille est simulée par une simple liste (et non un tableau
bi-dimensionnel). La case d'indice (ligne, colonne) se trouve à l'indice
ligne * colonnes + colonne dans cette liste.
"""


class Grille:

    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.colonnes = colonnes
        self.vide = '∿' # caractère affiché pour une case vide
        self.grille = [self.vide] * (lignes * colonnes)

    def tirer(self, ligne, colonne, touche='x'):
        """Marque la case (ligne, colonne) avec le caractère touche."""
        self.grille[self.indice(ligne, colonne)] = touche

    def __str__(self):
        lignes_texte = []
        for ligne in range(self.lignes):
            debut = self.indice(ligne, 0)
            fin = debut + self.colonnes
            lignes_texte.append(''.join(self.grille[debut:fin]))
        return '\n'.join(lignes_texte)

    def ajoute(self, bateau):
        """
            Place un bateau sur la grille en marquant ses positions avec sa
            marque. Le placement n'est effectué que si toutes les positions du
            bateau sont dans la grille et sur des cases encore vierges.
    
            Renvoie True si le bateau a pu être placé, False sinon.
            """
        positions = bateau.positions()
    
        for (ligne, colonne) in positions:
            if not self.dans_grille(ligne, colonne):
                return False
            if self.valeur(ligne, colonne) != self.vide:
                return False
    
            for (ligne, colonne) in positions:
                self.grille[self.indice(ligne, colonne)] = bateau.marque
    
        return True
    



    def indice(self, ligne, colonne):
        """Convertit des coordonnées (ligne, colonne) en indice dans la liste."""
        return ligne * self.colonnes + colonne

    def dans_grille(self, ligne, colonne):
        """Indique si les coordonnées sont bien à l'intérieur de la grille."""
        return 0 <= ligne < self.lignes and 0 <= colonne < self.colonnes

    def valeur(self, ligne, colonne):
        """Renvoie le caractère présent à la case (ligne, colonne)."""
        return self.grille[self.indice(ligne, colonne)]

   

    
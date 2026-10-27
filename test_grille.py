import unittest
 
from grille import Grille
from bateau import Bateau
 
 
class TestGrille(unittest.TestCase):
 
    def test_init(self):
        g = Grille(5, 8)
        self.assertEqual(g.lignes, 5)
        self.assertEqual(g.colonnes, 8)
        self.assertEqual(len(g.grille), 40)
        self.assertTrue(all(case == g.vide for case in g.grille))
 
    def test_tirer(self):
        g = Grille(5, 8)
        g.tirer(2, 3)
        self.assertEqual(g.valeur(2, 3), 'x')
        # les autres cases ne sont pas modifiées
        self.assertEqual(g.valeur(0, 0), g.vide)
 
 
    def test_str(self):
        g = Grille(5, 8)
        g.tirer(2, 3)
        attendu = (
            "∿∿∿∿∿∿∿∿\n"
            "∿∿∿∿∿∿∿∿\n"
            "∿∿∿x∿∿∿∿\n"
            "∿∿∿∿∿∿∿∿\n"
            "∿∿∿∿∿∿∿∿"
        )
        self.assertEqual(str(g), attendu)
 
    def test_ajoute_bateau_horizontal(self):
        g = Grille(2, 3)
        b = Bateau(1, 0, longueur=2, vertical=False)
        self.assertTrue(g.ajoute(b))
        self.assertEqual(g.grille, ["∿", "∿", "∿", "⛵", "⛵", "∿"])
 
    def test_ajoute_bateau_hors_grille_vertical(self):
        g = Grille(2, 3)
        b = Bateau(1, 0, longueur=2, vertical=True)
        self.assertFalse(g.ajoute(b))
        self.assertEqual(g.grille, ["∿", "∿", "∿", "∿", "∿", "∿"])
 
    def test_ajoute_bateau_trop_long(self):
        g = Grille(2, 3)
        b = Bateau(1, 0, longueur=4, vertical=True)
        self.assertFalse(g.ajoute(b))
        self.assertEqual(g.grille, ["∿", "∿", "∿", "∿", "∿", "∿"])
 
    def test_ajoute_bateau_chevauchement(self):
        g = Grille(2, 3)
        g.ajoute(Bateau(0, 0, longueur=2, vertical=False))
        # ce second bateau chevauche le premier sur la case (0, 1)
        resultat = g.ajoute(Bateau(0, 1, longueur=2, vertical=False))
        self.assertFalse(resultat)
 
 
if __name__ == "__main__":
    unittest.main()
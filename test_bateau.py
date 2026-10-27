import unittest

from grille import Grille
from bateau import Bateau, PorteAvions, Croiseur, Torpilleur, SousMarin


class TestBateau(unittest.TestCase):

    def test_valeurs_par_defaut(self):
        b = Bateau(2, 3)
        self.assertEqual(b.ligne, 2)
        self.assertEqual(b.colonne, 3)
        self.assertEqual(b.longueur, 1)
        self.assertFalse(b.vertical)

    def test_positions_horizontal(self):
        b = Bateau(2, 3, longueur=3)
        self.assertEqual(b.positions(), [(2, 3), (2, 4), (2, 5)])

    def test_positions_vertical(self):
        b = Bateau(2, 3, longueur=3, vertical=True)
        self.assertEqual(b.positions(), [(2, 3), (3, 3), (4, 3)])

    def test_chevauchement_vrai(self):
        b1 = Bateau(0, 0, longueur=3)          # (0,0) (0,1) (0,2)
        b2 = Bateau(0, 2, longueur=2, vertical=True)  # (0,2) (1,2)
        self.assertTrue(b1.chevauche(b2))
        self.assertTrue(b2.chevauche(b1))

    def test_chevauchement_faux(self):
        b1 = Bateau(0, 0, longueur=3)          # (0,0) (0,1) (0,2)
        b2 = Bateau(1, 0, longueur=3)          # (1,0) (1,1) (1,2)
        self.assertFalse(b1.chevauche(b2))

    def test_touche_et_coule(self):
        g = Grille(3, 3)
        b = Bateau(0, 0, longueur=2)  # (0,0) et (0,1)
        g.ajoute(b)

        self.assertFalse(b.coulé(g))

        g.tirer(0, 0, touche='💣')
        self.assertFalse(b.coulé(g))

        g.tirer(0, 1, touche='💣')
        self.assertTrue(b.coulé(g))

    def test_sous_classes_longueur_et_marque(self):
        self.assertEqual(PorteAvions(0, 0).longueur, 4)
        self.assertEqual(PorteAvions(0, 0).marque, "🚢")

        self.assertEqual(Croiseur(0, 0).longueur, 3)
        self.assertEqual(Croiseur(0, 0).marque, "⛴")

        self.assertEqual(Torpilleur(0, 0).longueur, 2)
        self.assertEqual(Torpilleur(0, 0).marque, "🚣")

        self.assertEqual(SousMarin(0, 0).longueur, 2)
        self.assertEqual(SousMarin(0, 0).marque, "🐟")

    def test_ajout_sous_classe_a_la_grille(self):
        g = Grille(4, 4)
        pa = PorteAvions(0, 0, vertical=False)
        self.assertTrue(g.ajoute(pa))
        self.assertEqual(g.grille[0:4], ["🚢", "🚢", "🚢", "🚢"])


if __name__ == "__main__":
    unittest.main()
"""
User Story : "chevauchement"
Utilisateur : un joueur.
Story : Positionner des bateaux sans chevauchement.
Actions :
    - créer un bateau b1
    - créer un bateau b2
    - vérifier si les deux bateaux se chevauchent
"""

from bateau import Bateau

print("=== Cas 1 : deux bateaux qui se chevauchent ===")
b1 = Bateau(0, 0, longueur=3, vertical=False)   # (0,0) (0,1) (0,2)
b2 = Bateau(0, 2, longueur=2, vertical=True)    # (0,2) (1,2)
print("b1 :", b1.positions())
print("b2 :", b2.positions())
print("Chevauchement ?", b1.chevauche(b2))

print()
print("=== Cas 2 : deux bateaux qui ne se chevauchent pas ===")
b3 = Bateau(0, 0, longueur=3, vertical=False)   # (0,0) (0,1) (0,2)
b4 = Bateau(1, 0, longueur=3, vertical=False)   # (1,0) (1,1) (1,2)
print("b3 :", b3.positions())
print("b4 :", b4.positions())
print("Chevauchement ?", b3.chevauche(b4))
## Installation et lancement
 
Dans le terminal de VS Code :
 
    python -m venv .venv
    source .venv/bin/activate        (Windows : .venv\Scripts\activate)
    pip install -r requirements.txt
    python main.py
 
## Les fichiers
 
- grille.py : la classe Grille
- bateau.py : la classe Bateau et ses sous-classes
- test_grille.py et test_bateau.py : les tests
- story_grille.py : la user story "Plouf dans l'eau"
- story_bateau.py : la user story "chevauchement"
- main.py : le jeu complet
- requirements.txt : la liste des modules à installer (termcolor)

## Réponses aux questions de l'énoncé
 
### 1. Modèle UML de la grille (sans bateaux)
 
    Grille
    ------
    lignes
    colonnes
    ------
    tirer(ligne, colonne)
    afficher()

### 2. Simuler une matrice par une liste
 
On met les lignes les unes après les autres dans une seule liste de
taille L x C. La case (ligne, colonne) est à l'indice :
 
    indice = L * C + colonne
 
Exemple avec 2 lignes et 3 colonnes :
 
    (0,0) (0,1) (0,2)   -> indices 0 1 2
    (1,0) (1,1) (1,2)   -> indices 3 4 5

### 3. Mise à jour Modèle UML de la grille 
 
    Grille
    ------
    Matrice: liste de caractères
    nombre_colonnes: int
    ------
    Grille(nombre_lignes,nombre_colonnes)
    tirer(ligne, colonne)
    afficher()
 
 
### 5. La classe Bateau
 
Attributs, dans l'ordre : ligne, colonne, longueur (1 par défaut),
vertical (False par défaut).
 
La méthode positions() donne la liste des cases occupées 
 
### 6. Chevauchement
 
Deux bateaux se chevauchent s'ils ont au moins une case en commun.
C'est la méthode Bateau.chevauche(other). Voir story_bateau.py.
 
### 7. Placer un bateau sur la grille
 
Grille.ajoute(bateau) vérifie que toutes les cases du bateau sont dans
la grille (et libres), puis écrit sa marque dessus. Sinon, la grille
ne change pas.
 
### 8. Touché et coulé
 
- Grille.tirer(ligne, colonne, touche='x') : le paramètre touche choisit le caractère posé.
- Bateau.touche(grille) et Bateau.positions_touchees(grille) : savoir si le bateau est touché, et où.
- Bateau.coulé(grille) : vrai si toutes les cases du bateau ont été touchées.
### 9. Types de bateaux
 
Quatre sous-classes de Bateau :
 
- PorteAvions : longueur 4, marque 🚢
- Croiseur : longueur 3, marque ⛴
- Torpilleur : longueur 2, marque 🚣
- SousMarin : longueur 2, marque 🐟
Leur constructeur prend (ligne, colonne, vertical).
 
### 10. Le jeu
 
- Grille de 8 lignes et 10 colonnes, avec un bateau de chaque type.
- Placement au hasard : pour chaque bateau, on liste tous les placements possibles sans chevauchement, puis on en choisit un au hasard.
- Les bateaux sont cachés. Un tir raté affiche x, un bateau touché affiche 💣, et un bateau coulé est montré avec sa marque et un message.
- Le jeu s'arrête quand tous les bateaux sont coulés, et il affiche le nombre de coups.
## UML final
 
    Bateau
    ------
    ligne, colonne, longueur, vertical, marque
    ------
    positions(), chevauche(other), touche(grille),
    positions_touchees(grille), coulé(grille)
        ^
        |  (héritage)
        +-- PorteAvions (longueur 4, marque 🚢)
        +-- Croiseur    (longueur 3, marque ⛴)
        +-- Torpilleur  (longueur 2, marque 🚣)
        +-- SousMarin   (longueur 2, marque 🐟)
 
    Grille
    ------
    lignes, colonnes, vide, grille
    ------
    indice(), dans_grille(), valeur(), tirer(), ajoute(bateau), __str__()
 
Grille et Bateau ne se stockent pas l'un l'autre : ils se parlent
seulement par les paramètres de leurs méthodes (ajoute(bateau),
coulé(grille)).
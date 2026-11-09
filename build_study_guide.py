#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate a PDF study guide with likely exam questions for the algorithmics DS."""

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font("Arial", "I", 8)
            self.set_text_color(100, 100, 100)
            self.cell(0, 6, "Revision DS Algorithmique", align="C")
            self.ln(4)

    def footer(self):
        self.set_y(-12)
        self.set_font("Arial", "I", 8)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def section_title(self, title, num=""):
        self.set_font("Arial", "B", 14)
        self.set_text_color(0x1F, 0x38, 0x64)
        self.cell(0, 8, f"{num} {title}" if num else title)
        self.ln(6)
        self.set_line_width(0.5)
        self.line(1, self.get_y(), 210 - 1, self.get_y())
        self.ln(4)

    def sub_title(self, title):
        self.set_font("Arial", "B", 11)
        self.set_text_color(0x33, 0x33, 0x33)
        self.cell(0, 7, title)
        self.ln(8)

    def sub_sub_title(self, title):
        self.set_font("Arial", "B", 10)
        self.set_text_color(0x44, 0x44, 0x44)
        self.cell(0, 6, title)
        self.ln(7)

    def body(self, text, indent=0, highlight_keywords=None):
        self.set_font("Arial", "", 9)
        self.set_text_color(0x26, 0x26, 0x26)
        self.set_x(1 + indent)
        self.multi_cell(190 - 2 - indent, 5, text)
        self.ln(2)

    def code_block(self, text, color=0x44, bg=0xF7):
        self.set_font("Arial", "", 8.5)
        bg_rgb = (bg >> 16) & 0xFF, (bg >> 8) & 0xFF, bg & 0xFF
        color_rgb = (color >> 16) & 0xFF, (color >> 8) & 0xFF, color & 0xFF
        self.set_fill_color(*bg_rgb)
        self.set_text_color(*color_rgb)
        self.set_x(1)
        self.multi_cell(190 - 2, 5, text, fill=True)
        self.ln(2)

    def bullet(self, text, indent=6):
        self.set_font("Arial", "", 9)
        self.set_text_color(0x26, 0x26, 0x26)
        self.set_x(1 + indent)
        self.cell(4, 5, "-")
        self.multi_cell(190 - 2 - indent - 4, 5, text)
        self.ln(1)

    def question(self, qid, text):
        """Display a practice question"""
        self.set_font("Arial", "B", 9)
        self.set_text_color(0x1F, 0x38, 0x64)
        self.cell(0, 6, f"{qid} : {text}")
        self.ln(5)

    def question_answer(self, qid, question_text, answer_text):
        self.set_font("Arial", "B", 9)
        self.set_text_color(0x1F, 0x38, 0x64)
        self.cell(0, 6, f"{qid} : {question_text}")
        self.ln(5)
        self.set_font("Arial", "B", 8)
        self.set_text_color(0x55, 0x55, 0x55)
        self.cell(0, 5, f"Reponse : {answer_text}")
        self.ln(6)
        """Display a practice question with answer"""
        self.set_font("Arial", "B", 9)
        self.set_text_color(0x1F, 0x38, 0x64)
        self.cell(0, 6, f"{qid} : {question_text}")
        self.ln(5)
        self.set_font("Arial", "B", 8)
        self.set_text_color(0x55, 0x55, 0x55)
        self.cell(0, 5, f"Reponse : {answer_text}")
        self.ln(6)

pdf = PDF()
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=15)

# ---------- COVER ----------
pdf.add_page()
pdf.ln(30)
pdf.set_font("Arial", "B", 28)
pdf.set_text_color(0x1F, 0x38, 0x64)
pdf.cell(0, 12, "Revision DS Algorithmique", align="C")
pdf.ln(14)
pdf.set_font("Arial", "B", 24)
pdf.cell(0, 10, "Questions types et corrections", align="C")
pdf.ln(10)
pdf.set_font("Arial", "", 14)
pdf.set_text_color(0x55, 0x55, 0x55)
pdf.cell(0, 8, "2h | Sans documents | QCM + TP", align="C")
pdf.ln(20)
pdf.set_font("Arial", "I", 11)
pdf.set_text_color(0x88, 0x88, 0x88)
pdf.cell(0, 6, "Niveau : Bachelor 1 - Algorithmique", align="C")

# ---------- SECTION 1: COMPLEXITE ----------
pdf.add_page()
pdf.section_title("Complexite (12 pts)", "1.")

pdf.sub_title("Definitions cles")
pdf.body("La complexite d'un algorithme mesure le nombre d'operations elementaires effectuees en fonction de la taille de l'entree (n).")
pdf.body("Notations utilisees :")
pdf.bullet("O(1) : temps constant (acces direct)")
pdf.bullet("O(log n) : divise l'espace de recherche a chaque etape (ex: recherche dichotomique)")
pdf.bullet("O(n) : temps lineaire (parcours complet)")
pdf.bullet("O(n^2) : temps quadratique (boucles imbriquees)")
pdf.bullet("O(2^n) : temps exponentiel (tres lent, a eviter)")

pdf.question("C1", "Determiner la complexite de cet algorithme :")
pdf.code_block("""for i in range(n):
    print(i)
# Reponse : O(n) - 1 boucle simple -> n operations

for i in range(n):
    for j in range(n):
        print(i, j)
# Reponse : O(n^2) - 2 boucles imbriquees -> n * n = n^2 operations
""")

pdf.question("C2", "Donner la complexite de cet algorithme :")
pdf.code_block("""def recherche_chemin(n):
    k = 1
    while k < n:
        k = k * 2
# Reponse : O(log n) - k est double a chaque tour
# k = 2^t, quand 2^t >= n, t = log2(n)
# Le nombre de tours est log2(n)
""")

pdf.question("C3", "Comparaison :")
pdf.body("Recherche lineaire O(n) vs recherche dichotomique O(log n).")
pdf.body("Pour n = 1000, combien d'operations au maximum ?")
pdf.body("- Lineaire : 1000 operations (parcourt tout le tableau)")
pdf.body("- Dichotomique : log2(1000) approx 10 operations (divise par 2 a chaque tour)")
pdf.body("- Economie : 100 fois moins d'operations !")
pdf.code_block("""# Recherche lineaire
for i in range(n):      # n iterations max
    if tab[i] == valeur:
        return i

# Recherche dichotomique
while gauche <= droite: # log2(n) iterations max
    milieu = (gauche + droite) // 2
    if tab[milieu] == valeur:
        return milieu
    elif tab[milieu] < valeur:
        gauche = milieu + 1
    else:
        droite = milieu - 1
""")

pdf.question("C4", "Ex 7 (complexite logarithmique) :")
pdf.body("On divise par 2 a chaque tour. Compter le nombre de tours pour n = 1024 :")
pdf.body("- Tour 1 : 1024 / 2 = 512")
pdf.body("- Tour 2 : 512 / 2 = 256")
pdf.body("- Tour 3 : 256 / 2 = 128")
pdf.body("- Tour 4 : 128 / 2 = 64")
pdf.body("- Tour 5 : 64 / 2 = 32")
pdf.body("- Tour 6 : 32 / 2 = 16")
pdf.body("- Tour 7 : 16 / 2 = 8")
pdf.body("- Tour 8 : 8 / 2 = 4")
pdf.body("- Tour 9 : 4 / 2 = 2")
pdf.body("- Tour 10 : 2 / 2 = 1")
pdf.body("- 10 tours pour n = 1024. Donc O(log n) car 2^10 = 1024.")
pdf.code_block("""for i in range(1, n+1, i*2):  # OU whilst divise par 2
    # pas de boucle simple
    # mais c'est le principe de la dichotomie
""")

pdf.question("C5", "Ex 11 - Borne superieure d'operations :")
pdf.body("Pour n = 100, combien d'operations dans les cas suivants ?")
pdf.body("a) 1 boucle - O(n) = 100 operations")
pdf.body("b) 2 boucles imbriquees - O(n^2) = 100 * 100 = 10 000 operations")
pdf.body("c) 3 boucles imbriquees - O(n^3) = 100 * 100 * 100 = 1 000 000 operations")
pdf.body("- L'augmentation est exponentielle !")

# ---------- SECTION 2: GRAPHES ----------
pdf.add_page()
pdf.section_title("Graphes (representations, BFS, DFS, Dijkstra)", "2.")

pdf.question("G1", "Representation d'un graphe :")
pdf.body("Un graphe G = (S, A) avec S = {A, B, C, D}, A = {(A,B), (B,C), (C,D), (D,A), (A,C)}")
pdf.body("1. Matrice d'adjacence (3 lignes, 3 colonnes) :")
pdf.code_block("""      A  B  C  D
     ------------
A |   0  1  1  1
B |   0  0  1  0
C |   0  0  0  1
D |   1  0  0  0
""")
pdf.body("2. Liste d'adjacence :")
pdf.code_block("""A : [B, C, D]
B : [C]
C : [D]
D : [A]
""")
pdf.body("- Matrice d'adjacence : O(n^2) pour les operations")
pdf.body("- Liste d'adjacence : O(n + m) pour les operations (m = nombre d'aretes)")

pdf.question("G2", "Recherche en largeur (BFS) :")
pdf.body("Principe : explorer tous les voisins d'un noeud avant de descendre.")
pdf.body("Algorithme :")
pdf.code_block("""from collections import deque

def bfs(graphe, depart):
    visite = set()
    file = deque([depart])
    while file:
        sommet = file.popleft()
        if sommet not in visite:
            visite.add(sommet)
            # Ajouter les voisins non visites
            for voisin in graphe[sommet]:
                if voisin not in visite:
                    file.append(voisin)
    return visite
""")
pdf.body("Exemple de parcours a partir de A : A - B - C - D (suivant l'ordre des voisins)")

pdf.question("G3", "Recherche en profondeur (DFS) :")
pdf.body("Principe : explorer le plus profondement possible avant de revenir en arriere.")
pdf.code_block("""def dfs(graphe, depart, visite=None):
    if visite is None:
        visite = set()
    visite.add(depart)
    for voisin in graphe[depart]:
        if voisin not in visite:
            dfs(graphe, voisin, visite)
    return visite
""")
pdf.body("Exemple de parcours a partir de A : A - B - C - D (aller au bout, puis retourner)")

pdf.question("G4", "Algorithme de Dijkstra (plus court chemin) :")
pdf.body("But : trouver le plus court chemin d'un noeud source a tous les autres.")
pdf.body("Etapes :")
pdf.bullet("Initialiser : distance[source] = 0, autres = infinity")
pdf.bullet("Tant qu'il reste des sommets non visites :")
pdf.bullet("  - Choisir le sommet non visite avec la plus petite distance")
pdf.bullet("  - Marquer comme visite")
pdf.bullet("  - Mettre a jour les distances des voisins")
pdf.body("- Complexite : O(n^2) avec liste de sommets non visites")
pdf.body("- Complexite : O((n + m) log n) avec file de priorite (heap)")

# ---------- SECTION 3: PYTHON ----------
pdf.add_page()
pdf.section_title("Python (lecture de code, listes, chaines, comprehension)", "3.")

pdf.question("P1", "Lecture de traces (variables) :")
pdf.body("Exemple de code :")
pdf.code_block("""a = 5
b = 3
c = a + b
a = c - b
b = a * 2
# Valeurs finales : a = 5, b = 10, c = 8
""")
pdf.body("A savoir : suivre l'evolution des variables etape par etape")

pdf.question("P2", "Liste - Moyenne :")
pdf.body("Adapter le code pour calculer la moyenne d'une liste :")
pdf.code_block("""def moyenne(liste):
    s = 0
    for x in liste:
        s += x
    return s / len(liste)

# Exemple
print(moyenne([10, 20, 30]))  # 20.0
""")

pdf.question("P3", "Liste - MINIMUM sans min :")
pdf.body("Trouver le minimum d'une liste sans utiliser la fonction min() :")
pdf.code_block("""def minimum(liste):
    if not liste:
        return None
    m = liste[0]
    for x in liste[1:]:
        if x < m:
            m = x
    return m

# Exemple
print(minimum([5, 2, 8, 1, 9]))  # 1
""")

pdf.question("P4", "Chaines de caracteres :")
pdf.body("Operations courantes :")
pdf.code_block("""# Longueur
print(len("hello"))  # 5

# Acces par index
mot = "Python"
print(mot[0])   # P
print(mot[-1])  # n

# Slicing
print(mot[1:4])  # yth
print(mot[::-1])  # nohtyP (inverse)

# Concatenation
print("Hello" + "World")  # HelloWorld
""")

pdf.question("P5", "Comprehension de code Python :")
pdf.body("Quel est le resultat de ce code ?")
pdf.code_block("""# Exemple 1
carres = [x**2 for x in range(5)]
print(carres)  # [0, 1, 4, 9, 16]

# Exemple 2
pairs = [x for x in range(10) if x % 2 == 0]
print(pairs)  # [0, 2, 4, 6, 8]

# Exemple 3
noms = ["Alice", "Bob", "Charlie"]
notes = [15, 12, 18]
dico = {nom: note for nom, note in zip(noms, notes)}
print(dico)  # {'Alice': 15, 'Bob': 12, 'Charlie': 18}
""")

pdf.question("P6", "Fonction random :")
pdf.body("Creer une liste de n nombres aleatoires et calculer sa moyenne :")
pdf.code_block("""import random

def liste_alea_moyenne(n):
    liste = [random.randint(0, 100) for _ in range(n)]
    moyenne = sum(liste) / len(liste)
    return liste, moyenne

# Exemple
liste, moy = liste_alea_moyenne(5)
print(liste)  # ex: [45, 12, 78, 3, 90]
print(moy)    # moyenne
""")

# ---------- SECTION 4: ALGORITHMES DE TRI ----------
pdf.add_page()
pdf.section_title("Algorithmes de tri et recherche dichotomique", "4.")

pdf.question("T1", "Tri par insertion - Principe :")
pdf.body("La liste est divisee en partie triee et partie non triee.")
pdf.body("A chaque etape, on prend l'element suivant et on l'insere a sa place dans la partie triee.")
pdf.code_block("""def tri_insertion(liste):
    for i in range(1, len(liste)):
        cle = liste[i]
        j = i - 1
        while j >= 0 and liste[j] > cle:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = cle
    return liste

# Exemple
print(tri_insertion([5, 2, 8, 1, 9]))
# [1, 2, 5, 8, 9]
""")
pdf.body("- Complexite : O(n^2) dans le pire cas, O(n) dans le meilleur cas")

pdf.question("T2", "Tri par selection - Principe :")
pdf.body("Trouver le minimum et l'echanger avec le premier element non trie.")
pdf.code_block("""def tri_selection(liste):
    for i in range(len(liste)):
        min_idx = i
        for j in range(i+1, len(liste)):
            if liste[j] < liste[min_idx]:
                min_idx = j
        liste[i], liste[min_idx] = liste[min_idx], liste[i]
    return liste

# Exemple
print(tri_selection([5, 2, 8, 1, 9]))
# [1, 2, 5, 8, 9]
""")
pdf.body("- Complexite : O(n^2) - toujours le meme quel que soit le cas")

pdf.question("T3", "Tri a bulles - Principe :")
pdf.body("Comparer adjacents et les echanger si ils sont dans le mauvais ordre.")
pdf.code_block("""def tri_bulles(liste):
    n = len(liste)
    for i in range(n):
        echange = False
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
                echange = True
        if not echange:
            break
    return liste

# Exemple
print(tri_bulles([5, 2, 8, 1, 9]))
# [1, 2, 5, 8, 9]
""")
pdf.body("- Complexite : O(n^2) dans le pire cas, O(n) dans le meilleur cas")

pdf.question("T4", "Recherche dichotomique - Principe :")
pdf.body("La liste doit etre TRIEE.")
pdf.body("A chaque etape, on compare la valeur avec le milieu :")
pdf.bullet("Egalite - on a trouve")
pdf.bullet("Valeur < milieu - on cherche a gauche")
pdf.bullet("Valeur > milieu - on cherche a droite")
pdf.body("Indices : gauche, milieu, droite a chaque etape")
pdf.code_block("""def recherche_dichotomique(tab, valeur):
    gauche = 0
    droite = len(tab) - 1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if tab[milieu] == valeur:
            return milieu
        elif tab[milieu] < valeur:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    return -1  # pas trouve

# Exemple (liste triee)
tab = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(recherche_dichotomique(tab, 23))  # 5 (index de 23)
""")
pdf.body("- Complexite : O(log n) - tres efficace pour les grands tableaux")

# ---------- SECTION 5: QCM (Vocabulaire Graphes) ----------
pdf.add_page()
pdf.section_title("QCM - Vocabulaire des graphes", "5.")

pdf.question("Q1", "QCM - Graphes :")
pdf.question_answer("Q2", "Quelle est la difference entre un tableau d'adjacence et une matrice d'adjacence ?",
    "Reponse : Tableau = liste de voisins par sommet (O(n+m)), Matrice = matrice carree (O(n^2)).")

pdf.question_answer("Q3", "Quand utilise-t-on la recherche en profondeur (DFS) ?",
    "Reponse : Pour explorer tout le graphe, detecter les cycles, ou naviguer en profondeur.")

pdf.question_answer("Q4", "Quelle est la complexite de Dijkstra avec liste de priorite ?",
    "Reponse : O((n+m) log n)")

pdf.question_answer("Q5", "Qu'est-ce qu'un graphe densement connecte ?",
    "Reponse : Beaucoup d'aretes par rapport au nombre de sommets (m approx n^2)")

pdf.question_answer("Q6", "Qu'est-ce qu'un graphe peu dense ?",
    "Reponse : Peu d'aretes par rapport au nombre de sommets (m << n^2)")

pdf.question_answer("Q7", "Quelle structure pour les graphes si n est tres grand ?",
    "Reponse : Liste d'adjacence (plus efficace pour la plupart des cas)")

pdf.question_answer("Q8", "Quelle structure pour les graphes tres dense ?",
    "Reponse : Matrice d'adjacence (acces direct aux aretes)")

# ---------- CONCLUSION ----------
pdf.ln(10)
pdf.set_font("Arial", "B", 14)
pdf.set_text_color(0x1F, 0x38, 0x64)
pdf.cell(0, 8, "Conseils de revision", align="C")
pdf.ln(10)

pdf.body("1. Commence par la complexite (c'est le point bloquant pour toi)")
pdf.body("2. Pratique les questions de lecture de code (traces, variables)")
pdf.body("3. Revois les algorithmes de tri et la recherche dichotomique")
pdf.body("4. Les graphes : memorise les representations (tableau vs liste)")
pdf.body("5. Le plan : 2h -> 30 min QCM, 1h 30 min TP (graphes + python + complexite)")
pdf.body("6. Ne neglige pas les boucles imbriquees (O(n^2) c'est frequent)")
pdf.body("7. Pour la recherche dichotomique : toujours verifier que la liste est triee")

pdf.ln(10)
pdf.set_font("Arial", "I", 9)
pdf.set_text_color(0x77, 0x77, 0x77)
pdf.cell(0, 6, "Bon courage pour ton DS !", align="C")

# ---------- SAVE ----------
pdf.output(r"C:\Users\HP OMEN\Documents\Revision_DS_Algo.pdf")
print(f"PDF genere : C:\\Users\\HP OMEN\Documents\Revision_DS_Algo.pdf")

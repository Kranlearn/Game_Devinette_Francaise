#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate the TD corrections PDF and quiz using fpdf2."""
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font("Arial", "I", 8)
            self.set_text_color(100, 100, 100)
            self.cell(0, 6, "Corrigé TD Algorithmie - Bachelor 1", align="C")
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
        self.set_text_color(0x2E, 0x74, 0xB5)
        self.cell(0, 7, title)
        self.ln(8)

    def sub_sub_title(self, title):
        self.set_font("Arial", "B", 10)
        self.set_text_color(0x33, 0x33, 0x33)
        self.cell(0, 6, title)
        self.ln(7)

    def body(self, text, indent=0):
        self.set_font("Arial", "", 9)
        self.set_text_color(0x26, 0x26, 0x26)
        self.set_x(1 + indent)
        self.multi_cell(190 - 2 - indent, 5, text)
        self.ln(2)

    def code_block(self, text, color=0x44, bg=0xF7):
        # Not used, but kept for reference
        pass

    def bullet(self, text, indent=6):
        self.set_font("Arial", "", 9)
        self.set_text_color(0x26, 0x26, 0x26)
        self.set_x(1 + indent)
        self.cell(4, 5, "-")
        self.multi_cell(190 - 2 - indent - 4, 5, text)
        self.ln(1)

    def note(self, text):
        self.set_font("Arial", "I", 8.5)
        self.set_text_color(0x55, 0x55, 0x55)
        self.set_x(1)
        self.multi_cell(190, 5, text)
        self.ln(3)

pdf = PDF()
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_font("Arial", "", "C:/Windows/Fonts/arial.ttf")
pdf.add_font("Arial", "B", "C:/Windows/Fonts/arialbd.ttf")
pdf.add_font("Arial", "I", "C:/Windows/Fonts/ariali.ttf")

# ---------- COVER ----------
pdf.add_page()
pdf.ln(30)
pdf.set_font("Arial", "B", 28)
pdf.set_text_color(0x1F, 0x38, 0x64)
pdf.cell(0, 12, "Corrigé TD Algorithmie", align="C")
pdf.ln(14)
pdf.set_font("Arial", "", 15)
pdf.set_text_color(0x55, 0x55, 0x55)
pdf.cell(0, 8, "Python - Bachelor 1", align="C")
pdf.ln(20)
pdf.set_draw_color(0x1F, 0x38, 0x64)
pdf.set_line_width(0.8)
pdf.line(40, pdf.get_y(), 170, pdf.get_y())
pdf.ln(14)
pdf.set_font("Arial", "B", 11)
pdf.set_text_color(0x33, 0x33, 0x33)
pdf.cell(0, 8, "Variables • Conditions • Boucles • Listes • Chaînes • Complexité", align="C")
pdf.ln(6)
pdf.set_font("Arial", "I", 9)
pdf.set_text_color(0x77, 0x77, 0x77)
pdf.cell(0, 6, "Format : PDF | $ 600 " if False else "", align="C")
pdf.ln(12)
pdf.set_font("Arial", "I", 8)
pdf.set_text_color(0x99, 0x99, 0x99)
pdf.cell(0, 6, "Généré le 2026-11-01 — Pour les étudiants Bachelor 1", align="C")

# ---------- TABLE OF CONTENTS ----------
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.set_text_color(0x1F, 0x38, 0x64)
pdf.cell(0, 10, "Table des matières", align="C")
pdf.ln(14)

toc = [
    ("1.", "Variables (6 exercices)"),
    ("2.", "Conditions (7 exercices)"),
    ("3.", "Lecture de variables (traces) (6 exercices)"),
    ("4.", "Boucles for (7 exercices)"),
    ("5.", "Boucles while (6 exercices)"),
    ("6.", "Structures imbriquées (6 exercices)"),
    ("7.", "Chaînes de caractères (7 exercices)"),
    ("8.", "Listes / tableaux (8 exercices)"),
    ("9.", "Compréhension de code (12 exercices)"),
    ("10.", "Problèmes type « LeetCode light » (3 exercices)"),
    ("11.", "Quiz (12 questions) + Corrigé"),
]
for num, title in toc:
    pdf.set_font("Arial", "", 11)
    pdf.set_text_color(0x26, 0x26, 0x26)
    pdf.cell(12, 7, num)
    pdf.cell(0, 7, title)
    pdf.ln(8)

pdf.ln(10)
pdf.set_font("Arial", "I", 8.5)
pdf.set_text_color(0x77, 0x77, 0x77)
pdf.cell(0, 6, "Astuce : imprime ce corrigé et couvre les réponses pour t'entraîner sans regarder.", align="C")

# ---------- CHAPTER 1: VARIABLES ----------
pdf.add_page()
pdf.section_title("Variables", "1.")

pdf.sub_title("Exercice 1 — Surface d'un rectangle")
pdf.body("Énoncé : L et l sont réels (valeurs choisies). Afficher S = L × l.")
pdf.body("Corrigé (Python) :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """
L = float(input("Longueur L : "))
l = float(input("Largeur l : "))
S = L * l
print("Surface S =", S)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(4)
pdf.body("Justification : opération directe, pas de condition. Utilisation de float() pour les nombres décimaux.")
pdf.note("Tests : L=5, l=3 → S=15   |   L=2.5, l=4 → S=10   |   L=1.5, l=2 → S=3")
pdf.ln(6)

pdf.sub_title("Exercice 2 — Secondes → hh : mm : ss")
pdf.body("Énoncé : n=3923s, calculer heures, minutes, secondes.")
pdf.body("Corrigé (Python) :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """n = 3923
h = n // 3600
reste = n % 3600
m = reste // 60
s = reste % 60
print(f"{h:02d}:{m:02d}:{s:02d}")""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(4)
pdf.body("Justification : 1h=3600s, 1min=60s. D'abord //3600 pour les heures, puis sur le reste %3600, //60 pour les minutes, %60 pour les secondes.")
pdf.note("Tests : 3923→01:05:23 | 0→00:00:00 | 3661→01:01:01 | 90→00:01:30")
pdf.ln(6)

pdf.sub_title("Exercice 3 — Échange x, y")
pdf.body("Avec variable temporaire :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """x = 5
y = 3
tmp = x
x = y
y = tmp""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Sans variable (astuce Python) : x, y = y, x")
pdf.note("Exemple : x=5, y=3 → après échange : x=3, y=5. L'astuce Python évalue d'abord (y, x) = (3, 5) puis affecte simultanément.")
pdf.ln(6)

pdf.sub_title("Exercice 4 — Brut → net")
pdf.body("Entrée : salaire_brut, taux (%), Sorties : net, retenue.")
pdf.body("Corrigé (Python) :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """salaire_brut = float(input("Salaire brut : "))
taux = float(input("Taux de retenue (%): "))

retenue = salaire_brut * taux / 100
net = salaire_brut - retenue

print(f"Retenue : {retenue:.2f}")
print(f"Net : {net:.2f}")""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(4)
pdf.body("Justification : retenue = brut × taux / 100, puis net = brut − retenue.")
pdf.note("Tests : brut=1000, taux=10 → retenue=100, net=900")
pdf.ln(6)

pdf.sub_title("Exercice 5 — Prix TTC")
pdf.body("Entrées : prix_HT, TVA (%), Sorties : TTC, montant_TVA.")
pdf.body("Corrigé (Python) :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """prix_HT = float(input("Prix HT : "))
tva = float(input("Taux TVA (%) : "))

montant_tva = prix_HT * tva / 100
prix_ttc = prix_HT + montant_tva

print(f"Montant TVA : {montant_tva:.2f}")
print(f"Prix TTC : {prix_ttc:.2f}")""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(4)
pdf.body("Justification : montant_tva = HT × TVA / 100, TTC = HT + TVA.")
pdf.note("Tests : HT=100, TVA=20 → montant_tva=20, TTC=120")
pdf.ln(6)

pdf.sub_title("Exercice 6 — Mini-convertisseur EUR ↔ USD")
pdf.body("Menu : (1) EUR→USD, (2) USD→EUR, taux saisi.")
pdf.body("Corrigé (Python) :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """choix = int(input("1: EUR→USD, 2: USD→EUR : "))
montant = float(input("Montant : "))
taux = float(input("Taux : "))

if choix == 1:
    print(montant * taux)
elif choix == 2:
    print(montant / taux)
else:
    print("Choix invalide")""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(4)
pdf.body("Justification : EUR→USD = multiplier par taux ; USD→EUR = diviser par taux. L'exercice teste les conditions et la gestion des choix.")
pdf.note("Tests : choix=1, montant=10, taux=1.1 → 11.0 ; choix=2, montant=11, taux=1.1 → 10.0")
pdf.ln(4)

# ---------- CHAPTER 2: CONDITIONS ----------
pdf.add_page()
pdf.section_title("Conditions", "2.")

pdf.body("Exercice 1 — Parité")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """n = int(input("Entier : "))
if n % 2 == 0:
    print("pair")
else:
    print("impair")""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Règle : n % 2 donne le reste. 0 = pair, 1 = impair.")
pdf.note("Tests : 4→pair | 7→impair | 0→pair | -3→impair")
pdf.ln(5)

pdf.body("Exercice 2 — Signe")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """x = float(input("Réel : "))
if x > 0:
    print("positif")
elif x < 0:
    print("négatif")
else:
    print("nul")""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Ordre important : vérifier d'abord >0, puis <0, enfin le cas restant = 0.")
pdf.note("Tests : 5→positif | -3→négatif | 0→nul")
pdf.ln(5)

pdf.body("Exercice 3 — Mention (sur 20)")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """note = float(input("Note : "))
if note < 10:
    print("Insuffisant")
elif note < 12:
    print("Passable")
elif note < 14:
    print("AB")
elif note < 16:
    print("B")
else:
    print("TB")""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Ordre des conditions : du plus bas au plus haut. Les elif s'évaluent dans l'ordre, donc la première condition qui correspond est celle qui s'applique.")
pdf.note("Tests : 8→Insuffisant | 10→Passable | 12→AB | 14→B | 16→TB | 18→TB")
pdf.ln(5)

pdf.body("Exercice 4 — Max de 3 (sans max)")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """a, b, c = 10, 5, 8
max3 = a
if b > max3:
    max3 = b
if c > max3:
    max3 = c
print(max3)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Logique : initialisation avec a, puis comparer b, puis c. À la fin, max3 = le plus grand.")
pdf.note("Tests : 10,5,8→10 | 3,7,2→7 | -1,-5,-3→-1")
pdf.ln(5)

pdf.body("Exercice 5 — Année bissextile")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """annee = int(input("Année : "))
if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    print("bissextile")
else:
    print("non bissextile")""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Règles : divisible par 4 → bissextile ; sauf si divisible par 100 → pas bissextile ; sauf si divisible par 400 → bissextile.")
pdf.note("Tests : 2000→bissextile | 2004→bissextile | 1900→non | 2024→bissextile | 2025→non")
pdf.ln(5)

pdf.body("Exercice 6 — Feu tricolore")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """couleur = input("Couleur (rouge/jaune/vert) : ").lower()
if couleur == "rouge":
    print("stop")
elif couleur == "jaune":
    print("attention")
elif couleur == "vert":
    print("passe")
else:
    print("entrée invalide")""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Gestion des entrées invalides : l'else capture tout ce qui n'est pas reconnu.")
pdf.note("Tests : rouge→stop | jaune→attention | vert→passe | bleu→entrée invalide")
pdf.ln(5)

pdf.body("Exercice 7 — Tarif")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """age = int(input("Âge : "))
etudiant = input("Carte étudiant (oui/non) : ").lower() == "oui"
if age < 26 or etudiant:
    prix = "réduction"
elif age < 4:
    prix = "gratuit"
else:
    prix = "plein tarif"
print(prix)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Logique : age<26 ou card étudiant → réduction. age<4 → gratuit. Reste → plein tarif.")
pdf.note("Tests : 25+oui→réduction | 30+oui→réduction | 2+oui→gratuit | 30+o→plein tarif")
pdf.ln(4)

# ---------- CHAPTER 3: LECTURE DE VARIABLES ----------
pdf.add_page()
pdf.section_title("Lecture de variables (traces)", "3.")

pdf.body("Exercice 1 — Donner a, b, c : a=2; b=5; c=a+b; a=c-b; b=a*2")
pdf.body("Corrigé (table d'état) :")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.set_x(1)
pdf.multi_cell(0, 4.5, """| Instruction     | a  | b  | c  |
|----------------|----|----|----|
| initial       | ?  | ?  | ?  |
| a = 2         | 2  | ?  | ?  |
| b = 5         | 2  | 5  | ?  |
| c = a + b     | 2  | 5  | 7  |
| a = c - b     | 2  | 5  | 7  |
| b = a * 2     | 2  | 4  | 7  |""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Résultat final : a=2, b=4, c=7.")
pdf.note("Astuce : suivez l'impact de chaque ligne sur toutes les variables.")
pdf.ln(5)

pdf.body("Exercice 2 — Accumulation s =0; s+=3; s-=1; s+=s")
pdf.body("Corrigé (trace) :")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.set_x(1)
pdf.multi_cell(0, 4.5, """| Instruction | s  |
|-------------|----|
| s = 0       | 0  |
| s += 3      | 3  |
| s -= 1      | 2  |
| s += s      | 4  |""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Résultat final : s = 4. Remarque : à l'instruction s += s, on ajoute la valeur courante de s (2), donc 2+2=4.")
pdf.note("Piège classique : ne pas confondre s += s avec s = 1 (ou un autre nombre).")
pdf.ln(5)

pdf.body("Exercice 3 — Compteur et booléen")
pdf.body("Corrigé (trace) :")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.set_x(1)
pdf.multi_cell(0, 4.5, """| Instruction     | c | ok  |
|-----------------|---|-----|
| c = 0         | 0 | F   |
| c += 1        | 1 | F   |
| ok = (c % 2 == 0) | 1 | F   |
| c += 1        | 2 | F   |""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Résultat final : c=2, ok=False.")
pdf.note("Piège : la comparaison (c%2==0) est faite une fois que c=1, donc 1%2=1 ≠ 0 → ok reste False.")
pdf.ln(5)

pdf.body("Exercice 4 — Indices dans chaîne")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """mot = "python"  (longueur 6, indices 0 à 5)
i = 1
j = len(mot) - 2 = 6 - 2 = 4
mot[1] = "y"
mot[4] = "o"
x = mot[1] + mot[4] = "yo" """, align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Résultat : x = \"yo\".")
pdf.note("Rappel : les indices commencent à 0 (mot[0]='p', mot[5]='n').")
pdf.ln(5)

pdf.body("Exercice 5 — Liste et affectations")
pdf.body("Corrigé (trace) :")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.set_x(1)
pdf.multi_cell(0, 4.5, """| Instruction       | t          |
|-------------------|-----------|
| t = [2, 4, 6]     | [2, 4, 6] |
| t[1] = t[0]+t[2]  | [2, 8, 6] |
| t.append(t[1])    | [2, 8, 6, 8]|""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Résultat final : t = [2, 8, 6, 8].")
pdf.note("Piège : après t[1] = t[0]+t[2], la liste devient [2,8,6] AVANT l'append. L'append ajoute la nouvelle valeur de t[1] = 8.")
pdf.ln(5)

pdf.body("Exercice 6 — Échanges et somme")
pdf.body("Corrigé (trace) :")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.set_x(1)
pdf.multi_cell(0, 4.5, """| Instruction       | x | y | z |
|-------------------|---|---|---|
| x = 7, y = 3      | 7 | 3 | ? |
| x, y = y, x       | 3 | 7 | ? |
| z = x + y         | 3 | 7 | 10|
| y = z - x         | 3 | 7 | 10|""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Résultat : x=3, y=7, z=10. Affichage final : 3 7 10.")
pdf.note("Le échange x,y = y,x fonctionne en Python grâce à l'affectation simultanée.")
pdf.ln(4)

# ---------- CHAPTER 4: BOUCLE FOR ----------
pdf.add_page()
pdf.section_title("Boucles for", "4.")

pdf.body("Exercice 1 — Somme 1+2+...+n")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """n = int(input("n : "))
s = 0
for i in range(1, n + 1):
    s += i
print(s)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("range(1, n+1) parcourt 1 à n. s += i additionne chaque i.")
pdf.note("Tests : n=5 → 15 | n=1 → 1 | n=10 → 55")
pdf.ln(5)

pdf.body("Exercice 2 — Table de multiplication")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """n = int(input("n : "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("range(1, 11) → 1 à 10. f-string pour le formatage.")
pdf.note("Tests : n=3 → 3x1=3, 3x2=6, ..., 3x10=30")
pdf.ln(5)

pdf.body("Exercice 3 — Compter les multiples de 3 entre 1 et n")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """n = int(input("n : "))
count = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        count += 1
print(count)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("i % 3 == 0 détecte les multiples de 3. count incrémenté à chaque fois.")
pdf.note("Tests : n=10 → 3 (3,6,9) | n=100 → 33")
pdf.ln(5)

pdf.body("Exercice 4 — Somme des carrés 1²+...+n²")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """n = int(input("n : "))
s = 0
for i in range(1, n + 1):
    s += i * i
print(s)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Exactement comme l'exercice 1, mais on élève i au carré à chaque tour.")
pdf.note("Tests : n=3 → 1+4+9=14 | n=4 → 1+4+9+16=30")
pdf.ln(5)

pdf.body("Exercice 5 — Diviseurs positifs de n")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """n = int(input("n : "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("n % i == 0 détecte les diviseurs. On affiche chaque diviseur.")
pdf.note("Tests : n=6 → 1,2,3,6 | n=7 → 1,7 | n=12 → 1,2,3,4,6,12")
pdf.ln(5)

pdf.body("Exercice 6 — Suite signée")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """n = int(input("n : "))
s = 0
for k in range(1, n + 1):
    if k % 2 == 0:
        s += k
    else:
        s -= k
print(s)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("k%2==0 → pair → on ajoute k. Impair → on soustrait k.")
pdf.note("Tests : n=4 → -1+2-3+4=2 | n=5 → -1+2-3+4-5=-3")
pdf.ln(5)

pdf.body("Exercice 7 — Approximation de π (Leibniz)")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """N = int(input("N : "))
s = 0
for k in range(N):
    signe = 1 if k % 2 == 0 else -1
    s += signe / (2 * k + 1)
pi_approx = 4 * s
print(pi_approx)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Formule : π/4 ≈ 1 - 1/3 + 1/5 - 1/7 + ... Le signe alterne : +1 pour k pair, -1 pour k impair.")
pdf.note("Tests : N=1 → 4.0 | N=2 → 2.667 | N=100 → ~3.13")
pdf.ln(4)

# ---------- CHAPTER 5: BOUCLE WHILE ----------
pdf.add_page()
pdf.section_title("Boucles while", "5.")

pdf.body("Exercice 1 — Lire des entiers jusqu'à 0; afficher la somme")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """s = 0
n = int(input("Entier (0 pour finir) : "))
while n != 0:
    s += n
    n = int(input("Entier (0 pour finir) : "))
print("Somme =", s)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("La lecture est DANS la boucle pour que la condition soit re-lue à chaque itération.")
pdf.note("Tests : 5,3,0 → 8 | 7,2,1,0 → 10")
pdf.ln(5)

pdf.body("Exercice 2 — Deviner un nombre secret")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """secret = 7  # dans la vraie vie, secret = randint(1, 100)
essai = int(input("Taper un nombre : "))
while essai != secret:
    if essai < secret:
        print("trop petit")
    else:
        print("trop grand")
    essai = int(input("Taper un nombre : "))
print("gagné !")""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Boucle jusqu'à ce que essai == secret. On donne un indice à chaque tour.")
pdf.note("Tests : secret=7, essais=5→trop petit | 7→gagné !")
pdf.ln(5)

pdf.body("Exercice 3 — Doubler n tant que n ≤ 100")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """n = int(input("n : "))
while n <= 100:
    print(n)
    n = n * 2""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Tant que n ≤ 100, on affiche, puis on le double.")
pdf.note("Tests : n=30 → 30,60,120 (arrêt quand n>100) | n=150 → 150 seul")
pdf.ln(5)

pdf.body("Exercice 4 — Saisie contrôlée [1,10]")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """n = int(input("Entier [1,10] : "))
while n < 1 or n > 10:
    print("Retape : ")
    n = int(input())""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("La boucle continue tant que n n'est PAS dans [1,10] (c'est-à-dire <1 ou >10).")
pdf.note("Tests : 15→retape | 5→autorise")
pdf.ln(5)

pdf.body("Exercice 5 — Nombre de chiffres")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """n = int(input("n : "))
n = abs(n)  # pour les négatifs
compteur = 0
while n > 0:
    n = n // 10
    compteur += 1
print(compteur)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("n//10 supprime le dernier chiffre à chaque tour. On compte les tours.")
pdf.note("Tests : 123→3 | 7→1 | 0→0 (attention à ce cas limite)")
pdf.ln(5)

pdf.body("Exercice 6 — PGCD (Euclide)")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """a = int(input("a : "))
b = int(input("b : "))
while b != 0:
    a, b = b, a % b
print(a)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("PGCD(a,b) = PGCD(b, a%b). Boucle jusqu'à b=0, alors a est le PGCD.")
pdf.note("Tests : (30,18)→6 | (100,45)→5 | (7,13)→1")
pdf.ln(4)

# ---------- CHAPTER 6: STRUCTURES EMBRANEES ----------
pdf.add_page()
pdf.section_title("Structures imbriquées", "6.")

pdf.body("Exercice 1 — Carré n×n d'étoiles")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """n = int(input("n : "))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Double boucle : ligne i (externe) × colonne j (interne). end=\" \" évite de sauter de ligne à chaque étoile.")
pdf.note("Tests : n=3 → * * * | * * * | * * *")
pdf.ln(5)

pdf.body("Exercice 2 — Table de multiplication 1..n par 1..n")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """n = int(input("n : "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i} x {j} = {i * j}", end="\\t")
    print()""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("i = ligne (1..n), j = colonne (1..n). end=\"\\t\" pour un séparateur de tabulation.")
pdf.note("Tests : n=3 → 3 lignes × 3 colonnes de produits")
pdf.ln(5)

pdf.body("Exercice 3 — Compter les multiples de i pour chaque i de 1..k")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """n = int(input("n : "))
k = int(input("k : "))
for i in range(1, k + 1):
    count = 0
    for j in range(1, n + 1):
        if j % i == 0:
            count += 1
    print(f"i={i} : {count} multiples")""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Double boucle : i de 1 à k, j de 1 à n. Compte les multiples de i dans [1,n].")
pdf.note("Tests : n=5, k=3 → i=1:5 multiples | i=2:2 | i=3:1")
pdf.ln(5)

pdf.body("Exercice 4 — Maximum dans une matrice m×n")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """m = int(input("nb lignes : "))
n = int(input("nb colonnes : "))
matrice = []
for i in range(m):
    ligne = []
    for j in range(n):
        val = int(input(f"[{i}][{j}] : "))
        ligne.append(val)
    matrice.append(ligne)

max_val = matrice[0][0]
for i in range(m):
    for j in range(n):
        if matrice[i][j] > max_val:
            max_val = matrice[i][j]
print("Max =", max_val)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Lecture de la matrice, puis recherche du max en parcourant toutes les cases.")
pdf.note("Tests : matrice 2x2 [[3,7],[2,9]] → max=9")
pdf.ln(5)

pdf.body("Exercice 5 — Échiquier n×n avec # et .")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """n = int(input("n : "))
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("#", end=" ")
        else:
            print(".", end=" ")
    print()""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("i+j pair → #. Autrement → . La couleur alterne selon la somme des indices.")
pdf.note("Tests : n=3 → # . # / . # . / # . #")
pdf.ln(5)

pdf.body("Exercice 6 — Couples (i,j) avec i+j premier")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """def est_premier(x):
    if x < 2:
        return False
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return True

n = int(input("n : "))
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if est_premier(i + j):
            print(f"({i}, {j})")""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("i<j et i+j premier. La fonction est_premier teste la primalité avec une boucle jusqu'à sqrt(x).")
pdf.note("Tests : n=5 → (1,2),(1,4),(2,3),(2,5),(3,4) avec i+j = 3,5,5,7,7")
pdf.ln(4)

# ---------- CHAPTER 7: CHAÎNES ----------
pdf.add_page()
pdf.section_title("Chaînes de caractères", "7.")

pdf.body("Exercice 1 — Compter les lettres a/A")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """mot = input("Mot : ")
count = 0
for c in mot:
    if c == 'a' or c == 'A':
        count += 1
print(count)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Parcours chaque caractère. Comparaison avec 'a' et 'A'.")
pdf.note("Tests : 'abracadabra' → 5 | 'ABC' → 1")
pdf.ln(5)

pdf.body("Exercice 2 — Majuscule la première lettre")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """mot = input("Mot : ")
if len(mot) > 0:
    premier = mot[0].upper()
    reste = mot[1:].lower()
    print(premier + reste)
else:
    print(mot)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("mot[0] = premier caractère (majusculé), mot[1:] = le reste.")
pdf.note("Tests : 'hello'→'Hello' | 'WORLD'→'World'")
pdf.ln(5)

pdf.body("Exercice 3 — Extraire préfixe/suffixe")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """mot = input("Mot : ")
k = int(input("k : "))
prefixe = mot[:k]
suffixe = mot[-k:] if k > 0 and k <= len(mot) else mot
print("Préfixe :", prefixe)
print("Suffixe :", suffixe)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Mot[:k] = k premiers. Mot[-k:] = k derniers. Si k > longueur, on prend toute la chaine.")
pdf.note("Tests : 'python', k=2 → 'py', 'on' | k=10 → 'python', 'python'")
pdf.ln(5)

pdf.body("Exercice 4 — Palindrome (ignorer casse/espaces)")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """mot = input("Mot : ").lower().replace(" ", "")
if mot == mot[::-1]:
    print("c'est un palindrome")
else:
    print("non")""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("lower() pour minuscules, replace(" ","") pour enlever les espaces, [::-1] pour inverser.")
pdf.note("Tests : 'elle'→oui | 's radi'→oui | 'hello'→non")
pdf.ln(5)

pdf.body("Exercice 5 — Compter les voyelles")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """mot = input("Mot : ").lower()
voyelles = "aeiouy"
count = 0
for c in mot:
    if c in voyelles:
        count += 1
print(count)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("c in voyelles vérifie si le caractère est dans la chaine 'aeiouy'.")
pdf.note("Tests : 'algorithmie' → 4 | 'hello' → 2")
pdf.ln(5)

pdf.body("Exercice 6 — Remplacer un motif (sans replace)")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """mot = input("Mot : ")
motif = input("Motif : ")
remplacement = input("Remplacement : ")

resultat = ""
i = 0
while i < len(mot):
    if mot[i:i + len(motif)] == motif:
        resultat += remplacement
        i += len(motif)
    else:
        resultat += mot[i]
        i += 1
print(resultat)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("On parcourt la chaine. A chaque pas, on vérifie si le sous-motif correspond. Si oui, on ajoute le remplacement et on saute du bon nombre de caractères.")
pdf.note("Tests : 'ababa', motif='ba', remplacement='X' → 'aXa'")
pdf.ln(5)

pdf.body("Exercice 7 — Comparaison lexicographique sans <")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """def compare_lex(s1, s2):
    n1, n2 = len(s1), len(s2)
    for i in range(min(n1, n2)):
        if s1[i] < s2[i]:
            return -1
        if s1[i] > s2[i]:
            return 1
    if n1 < n2:
        return -1
    elif n1 > n2:
        return 1
    else:
        return 0

print(compare_lex("abc", "abd"))  # -1
print(compare_lex("abc", "abcd")) # -1
print(compare_lex("abc", "abc"))  # 0""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("On compare les caractères un par un. La première différence détermine l'ordre. Si tous égaux, on compare les longueurs.")
pdf.note("Tests : 'abc' vs 'abd' → -1 | 'abc' vs 'abcd' → -1 | 'abc' vs 'abc' → 0")
pdf.ln(4)

# ---------- CHAPTER 8: LISTES ----------
pdf.add_page()
pdf.section_title("Listes / tableaux", "8.")

pdf.body("Exercice 1 — Somme d'une liste")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """t = [3, 7, 2, 9]
s = sum(t)
# ou sans sum
s = 0
for x in t:
    s += x
print(s)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("sum(t) fait tout en une ligne. Avec boucle, on additionne chaque élément.")
pdf.note("Tests : [3,7,2,9]→21")
pdf.ln(5)

pdf.body("Exercice 2 — Maximum d'une liste (sans max)")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """t = [3, 7, 2, 9, 5]
max_val = t[0]
for x in t:
    if x > max_val:
        max_val = x
print(max_val)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("On initialise max_val avec t[0], puis on compare chaque élément.")
pdf.note("Tests : [3,7,2,9,5]→9 | [-5,-2,-10]→-2")
pdf.ln(5)

pdf.body("Exercice 3 — Compter les éléments égaux à v")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """t = [3, 7, 2, 7, 9, 7]
v = 7
count = 0
for x in t:
    if x == v:
        count += 1
print(count)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("On compare chaque élément avec v et on incrémente count.")
pdf.note("Tests : [3,7,2,7,9,7], v=7 → 3 | v=5 → 0")
pdf.ln(5)

pdf.body("Exercice 4 — Inverser une liste en place")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """t = [1, 2, 3, 4, 5]
n = len(t)
for i in range(n // 2):
    t[i], t[n - 1 - i] = t[n - 1 - i], t[i]
print(t)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("On échange le i-ème avec le (n-1-i)-ème. Boucle jusqu'à la moitié.")
pdf.note("Tests : [1,2,3,4,5]→[5,4,3,2,1] | [1,2,3,4]→[4,3,2,1]")
pdf.ln(5)

pdf.body("Exercice 5 — Fusionner deux listes triées (merge)")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """def fusionner(t1, t2):
    resultat = []
    i, j = 0, 0
    while i < len(t1) and j < len(t2):
        if t1[i] <= t2[j]:
            resultat.append(t1[i])
            i += 1
        else:
            resultat.append(t2[j])
            j += 1
    while i < len(t1):
        resultat.append(t1[i])
        i += 1
    while j < len(t2):
        resultat.append(t2[j])
        j += 1
    return resultat

print(fusionner([1, 3, 5], [2, 4, 6]))""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("On compare les éléments courants des deux listes et on ajoute le plus petit. Quand une liste est épuisée, on ajoute le reste.")
pdf.note("Tests : [1,3,5]+[2,4,6] → [1,2,3,4,5,6] | [1,3,5]+[2] → [1,2,3,5]")
pdf.ln(5)

pdf.body("Exercice 6 — Supprimer les doublons (garder le premier)")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """t = [3, 1, 3, 2, 1, 5]
seen = set()
resultat = []
for x in t:
    if x not in seen:
        seen.add(x)
        resultat.append(x)
print(resultat)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Un ensemble seen mémorise ce qui a déjà été rencontré. seen.add(x) puis resultat.append(x) si x est nouveau.")
pdf.note("Tests : [3,1,3,2,1,5] → [3,1,2,5]")
pdf.ln(5)

pdf.body("Exercice 7 — Recherche dichotomique (indice ou -1)")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """def recherche_dichotomique(t, v):
    g, d = 0, len(t) - 1
    while g <= d:
        m = (g + d) // 2
        if t[m] == v:
            return m
        elif t[m] < v:
            g = m + 1
        else:
            d = m - 1
    return -1

t = [1, 3, 5, 7, 9]
print(recherche_dichotomique(t, 5))  # 2
print(recherche_dichotomique(t, 4))  # -1""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("On coupe l'intervalle [g,d] en deux à chaque tour. m = milieu. Si t[m]==v, on retourne m. Sinon on ajuste les bornes.")
pdf.note("Tests : t=[1,3,5,7,9], v=5→2 | v=4→-1 | v=9→4 | v=0→-1")
pdf.ln(5)

pdf.body("Exercice 8 — Tri par sélection (en place)")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """def tri_selection(t):
    for i in range(len(t)):
        min_i = i
        for j in range(i + 1, len(t)):
            if t[j] < t[min_i]:
                min_i = j
        t[i], t[min_i] = t[min_i], t[i]
    return t

print(tri_selection([3, 1, 4, 1, 5]))""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Pour chaque position i, on cherche l'élément minimum dans la partie restante, puis on échange.")
pdf.note("Tests : [3,1,4,1,5] → [1,1,3,4,5]")
pdf.ln(4)

# ---------- CHAPTER 9: COMPRÉHENSION DE CODE ----------
pdf.add_page()
pdf.section_title("Compréhension de code (mix de notions)", "9.")

pdf.body("Exercice 1")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """s = 0
for i in range(1, 6):
    s += i * i
print(s)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(2)
pdf.body("Calcul : 1²+2²+3²+4²+5² = 1+4+9+16+25 = 55")
pdf.note("Résultat : 55")
pdf.ln(4)

pdf.body("Exercice 2")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """mot = "ALGO"
out = ""
for i in range(len(mot)):
    out += mot[-i - 1]
print(out)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(2)
pdf.body("Mot = ALGO (indices 0 à 3). À chaque tour, on prend mot[-i-1].")
pdf.note("Résultat : 'OGLA' (chaine inversée)")
pdf.ln(4)

pdf.body("Exercice 3")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """t = [3, 1, 4, 1, 5]
m = t[0]       # m = 3
for x in t:
    if x > m:
        m = x
    else:
        m = m
print(m)""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(2)
pdf.body("L'instruction else: m = m ne change rien (inutile), mais logiquement on garde m.")
pdf.note("Résultat : 5 (le maximum)")
pdf.ln(4)

pdf.body("Exercice 4 — Algorithme et complexité")
pdf.body("Corrigé :")
pdf.body("C'est le **tri par sélection**.")
pdf.body("Complexité : O(n²) (boucle doublée).")
pdf.note("à chaque tour i, on parcourt la partie non triée pour trouver le minimum, puis on échange.")
pdf.ln(4)

pdf.body("Exercice 5 — Recherche dichotomique")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """def bsearch(t, v):
    g, d = 0, len(t) - 1
    while g <= d:
        m = (g + d) // 2
        if t[m] == v:
            return m
        elif t[m] < v:
            g = m + 1
        else:
            d = m - 1
    return -1""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Predicate : t doit être **triée** ! Invariant : t[g-1] ≤ v et t[d+1] ≥ v si les parties ont des éléments.")
pdf.note("Résultat : l'index de v, ou -1 si pas trouvé.")
pdf.ln(4)

pdf.body("Exercice 6 — Euclide récursif (30, 18)")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """def pgcd(a, b):
    return a if b == 0 else pgcd(b, a % b)

print(pgcd(30, 18))""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Trace : pgcd(30,18)→pgcd(18,12)→pgcd(12,6)→pgcd(6,0)→6")
pdf.note("Résultat : 6")
pdf.ln(4)

pdf.body("Exercice 7 — Collatz, longueur pour n=13")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """def collatz_len(n):
    c = 1
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        c += 1
    return c

print(collatz_len(13))""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Trace : 13→40→20→10→5→16→8→4→2→1 (10 étapes)")
pdf.note("Résultat : 10")
pdf.ln(4)

pdf.body("Exercice 8 — Double boucle")
pdf.body("Corrigé :")
pdf.body("Calcule le nombre de paires (i, j) telles que j divise i (i multiple de j), pour i de 1 à n.")
pdf.body("Complexité : O(n²) car boucle doublée.")
pdf.note("Exemple n=3 → i=1: j=1 (1%1==0) →1 ; j=2 (1%2≠0) →0 ; j=3 (1%3≠0) →0. i=2: j=1 (2%1==0)→1. i=3: j=1→1. Total = 3.")
pdf.ln(4)

pdf.body("Exercice 9")
pdf.body("Corrigé :")
pdf.body("Cette fonction renvoie la chaîne avec **uniquement les caractères uniques**, en conservant l'ordre de première apparition.")
pdf.note("Exemple : mystery('algorithmie') → 'algorithme' (le 2ème 'i' est enlevé)")
pdf.ln(4)

pdf.body("Exercice 11 — Indices négatifs")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """s = "algorithmie"
print(s[-3:])   # 'it'
print(s[:-3])   # 'algorithm'
print(s[::-1])  # 'emihgrotala'
print(s[1::2])  # 'lothmii'""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("s[-3:] = 3 derniers caractères | s[:-3] = tout sauf les 3 derniers | s[::-1] = inversé | s[1::2] = avec pas de 2 à partir de l'indice 1.")
pdf.note("Résultats : it | algorithm | emihgrotala | lothmii")
pdf.ln(4)

pdf.body("Exercice 12 — Crible d'Ératosthène")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """def crible(N):
    prime = [True] * (N + 1)
    prime[:2] = [False, False]   # 0 et 1 ne sont pas premiers
    p = 2
    while p * p <= N:
        if prime[p]:
            for k in range(p * p, N + 1, p):
                prime[k] = False
        p += 1
    return [i for i in range(N + 1) if prime[i]]""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Marquage des multiples : si prime[p] est vrai, on strie tous les multiples de p commençant par p*p.")
pdf.note("Complexité : O(N log log N), très efficace.")
pdf.ln(4)

# ---------- CHAPTER 10: LEETCODE LIGHT ----------
pdf.add_page()
pdf.section_title("Problèmes type « LeetCode light »", "10.")

pdf.body("Exercice 1 — Deux sommes (indices)")
pdf.body("Entrée : liste d'entiers t et cible S. Sortie : deux indices (i,j) avec i<j et t[i]+t[j]==S, ou (-1,-1). Attendu : version O(n) avec un dictionnaire.")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """def deux_sommes(t, S):
    d = {}  # dictionnaire "complément → index"
    for i, x in enumerate(t):
        complément = S - x
        if complément in d:
            return [d[complément], i]
        d[x] = i
    return (-1, -1)

# Test
print(deux_sommes([2, 7, 11, 15], 9))  # [0, 1]""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Logique : au lieu de la double boucle O(n²), on utilise un dictionnaire pour stocker l'index de chaque élément vu. À chaque tour, on vérifie si le complément (S-x) est déjà dans le dictionnaire.")
pdf.note("Complexité : O(n) temps, O(n) espace")
pdf.ln(4)

pdf.body("Exercice 2 — Parenthèses valides")
pdf.body("Entrée : chaîne avec ()[] {}. Dire si elle est bien formée. Attendu : pile; chaque fermante correspond à la bonne ouvrante; vide à la fin.")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """def est_bien_forme(s):
    pile = []
    correspondance = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            pile.append(ch)
        elif ch in ')]}':   # clôture
            if not pile or pile[-1] != correspondance[ch]:
                return False
            pile.pop()
    return len(pile) == 0

# Tests
print(est_bien_forme("()"))      # True
print(est_bien_forme("()[]{}"))  # True
print(est_bien_forme("(]"))      # False
print(est_bien_forme("([)]"))    # False
print(est_bien_forme("{[]}"))    # True""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("On utilise une pile (liste). Les ouvrantes ( [ { ) sont empilées. Les fermantes vérifient que le sommet est la bonne ouvrante, puis on dépile.")
pdf.note("Cas limites : si une fermante vient et que la pile est vide → faux. À la fin, la pile doit être vide (tout bien fermé).")
pdf.ln(4)

pdf.body("Exercice 3 — Sous-tableau de somme maximale (Kadane)")
pdf.body("Entrée : liste d'entiers (positifs/négatifs). Sortie : valeur maximale d'une somme de sous-tableau contigu. Attendu : algorithme de Kadane en O(n).")
pdf.body("Corrigé :")
pdf.set_text_color(0x1A, 0x3B, 0x6E)
pdf.set_x(1)
pdf.multi_cell(0, 5, """def kadane(t):
    courant = t[0]
    meilleur = t[0]
    for x in t[1:]:
        courant = max(x, courant + x)
        meilleur = max(meilleur, courant)
    return meilleur

# Test
print(kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))""", align="L")
pdf.set_text_color(0x26, 0x26, 0x26)
pdf.ln(3)
pdf.body("Logique : courant = somme du meilleur sous-tableau qui se termine ici. meilleur = le maximum de tous les courant.")
pdf.note("Exemple : [-2,1,-3,4,-1,2,1,-5,4] → sous-tableau [4,-1,2,1] → somme = 6")
pdf.ln(4)

# ---------- QUIZ ----------
pdf.add_page()
pdf.section_title("Quiz — Entraînement actif (sans regarder le corrigé!)", "11.")

pdf.set_font("Arial", "B", 12)
pdf.set_text_color(0x1F, 0x38, 0x64)
pdf.cell(0, 8, "QUIZ — 12 questions pour vérifier ta compréhension", align="C")
pdf.ln(10)

# Quiz questions (QCM + justifications)
quiz = [
    ("Q1", "Quelle est la valeur de S après ce code ?\n    L=5, l=3, S=L*l", "S=15"),
    ("Q2", "Quelle est la sortie de ce code ?\n    n=3923, h=n//3600, m=(n%3600)//60, s=n%60", "01:05:23"),
    ("Q3", "Que contiennent x et y après x,y = y,x avec x=5, y=3 ?", "x=3, y=5 (échange simultané)"),
    ("Q4", "Quelle est la valeur de S après la boucle for i in range(1,6): s+=i*i", "1+4+9+16+25=55"),
    ("Q5", "Que fait ce code sur une chaîne ALGO ?", "Affiche OGLA (chaine inversée)"),
    ("Q6", "Quelle est la sortie du code : print(3%2==0 and 5>3 or not 7%2==0)", "True (car not 7%2==0 = not False = True)"),
    ("Q7", "Quel est le résultat du code : a=0; while a<3: a+=1; print(a)", "1, 2, 3 (la boucle tourne 3 fois)"),
    ("Q8", "Quelle est la complexité du tri par sélection ?", "O(n²)"),
    ("Q9", "Quelle est la sortie du code : t=[3,1,4,1,5]; m=t[0]; for x in t: m=max(m,x); print(m)", "5"),
    ("Q10", "Quel est le résultat de la recherche dichotomique pour 4 dans [1,3,4,7,9] ?", "2 (indice du 4)"),
    ("Q11", "Que calcule Kadane pour [-2,1,-3,4,-1,2,1,-5,4] ?", "6 (somme de [4,-1,2,1])"),
    ("Q12", "Que fait le crible d'Ératosthène avec N=10 ?", "Retourne les nombres premiers ≤ 10 : [2,3,5,7]"),
]

for q_id, question, answer in quiz:
    pdf.set_font("Arial", "B", 11)
    pdf.set_text_color(0x1F, 0x38, 0x64)
    pdf.cell(0, 7, f"{q_id} — {question}", align="L")
    pdf.ln(7)
    pdf.set_font("Arial", "B", 9)
    pdf.set_text_color(0x1F, 0x38, 0x64)
    pdf.cell(0, 6, f"Réponse : {answer}")
    pdf.ln(7)

# ---------- CORRIGÉ SÉPARÉ (à couvrir quand on s'entraîne) ----------
pdf.add_page()
pdf.set_font("Arial", "B", 14)
pdf.set_text_color(0x1F, 0x38, 0x64)
pdf.cell(0, 10, "Corrigé détaillé (à garder caché !)", align="C")
pdf.ln(12)

pdf.body("NB : ce corrigé est destiné à être utilisé après le quiz. Ne le consultez pas avant d'avoir essayé !", indent=2)

# Save the PDF
output_path = r"C:\Users\HP OMEN\AppData\Local\hermes\attachments\TD_Corrections_Algorithmie.pdf"
pdf.output(output_path)
print(f"PDF généré avec succès : {output_path}")
print(f"Nombre total de pages : {pdf.page_no()}")

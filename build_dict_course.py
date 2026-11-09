#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate a PDF course on Dictionnaires (Dictionaries) in Python."""

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font("Arial", "I", 8)
            self.set_text_color(100, 100, 100)
            self.cell(0, 6, "Cours Python - Dictionnaires", align="C")
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

    def sub_title(self, title):
        self.set_font("Arial", "B", 11)
        self.set_text_color(0x33, 0x33, 0x33)  # Noir, pas de bleu
        self.cell(0, 7, title)
        self.ln(8)

    def sub_sub_title(self, title):
        self.set_font("Arial", "B", 10)
        self.set_text_color(0x33, 0x33, 0x33)
        self.cell(0, 6, title)
        self.ln(7)

    def body(self, text, indent=0, highlight_keywords=None):
        """
        Affiche un paragraphe avec coloration optionnelle des mots-clés.
        highlight_keywords: dictionnaire {mot_a_souligner: couleur_hex}
        """
        self.set_font("Arial", "", 9)
        self.set_text_color(0x26, 0x26, 0x26)
        self.set_x(1 + indent)
        
        # Si pas de mots clés, sortie normale
        if highlight_keywords is None or not highlight_keywords:
            self.multi_cell(190 - 2 - indent, 5, text)
            self.ln(2)
            return
        
        # Split le texte par les mots clés pour les mettre en valeur
        import re
        # Construire le regex: trier les mots par ordre décroissant de longueur
        sorted_keywords = sorted(highlight_keywords.keys(), key=len, reverse=True)
        pattern = '|'.join(re.escape(kw) for kw in sorted_keywords)
        
        # Diviser le texte en segments
        parts = re.split(f'({pattern})', text)
        
        for part in parts:
            if not part:
                continue
            if part in highlight_keywords:
                # Mot clé: mettre en gras et couleur
                self.set_font("Arial", "B", 9)
                self.set_text_color(int(highlight_keywords[part], 16))
                self.cell(190 - 2 - indent, 5, part)
            else:
                # Texte normal
                self.set_font("Arial", "", 9)
                self.set_text_color(0x26, 0x26, 0x26)
                self.cell(190 - 2 - indent, 5, part)
        self.ln(2)

    def code_block(self, text, color=0x44, bg=0xF7):
        self.set_font("Arial", "", 8.5)
        # Convert hex color to RGB tuple
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

pdf = PDF()
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=15)

# ---------- COVER ----------
pdf.add_page()
pdf.ln(30)
pdf.set_font("Arial", "B", 28)
pdf.set_text_color(0x1F, 0x38, 0x64)
pdf.cell(0, 12, "Cours Python", align="C")
pdf.ln(14)
pdf.set_font("Arial", "B", 24)
pdf.cell(0, 10, "Les Dictionnaires", align="C")
pdf.ln(12)
pdf.set_font("Arial", "", 14)
pdf.set_text_color(0x55, 0x55, 0x55)
pdf.cell(0, 8, "Méthodes, manipulation et exemples", align="C")
pdf.ln(20)
pdf.set_font("Arial", "I", 11)
pdf.set_text_color(0x88, 0x88, 0x88)
pdf.cell(0, 6, "Niveau : Debutant / Intermediaire", align="C")
pdf.ln(10)
pdf.set_font("Arial", "B", 10)
pdf.set_text_color(0x99, 0x99, 0x99)
pdf.cell(0, 6, "Version 1.0 - 2026", align="C")

# ---------- INTRODUCTION ----------
pdf.add_page()
pdf.intro_title = "Introduction"
pdf.section_title("Qu'est-ce qu'un dictionnaire ?", "I.")
pdf.body("En Python, un dictionnaire est une structure de données qui stocke des éléments sous forme de paires clé-valeur.")
pdf.body("Contrairement aux listes (où l'on accède aux éléments par un indice numérique), les dictionnaires utilisent des clés uniques pour accéder aux valeurs.")
pdf.body("Caractéristiques principales :")
pdf.bullet("Clés uniques et immuables (chaînes, nombres, tuples)")
pdf.bullet("Accès rapide par clé (complexité O(1) en moyenne)")
pdf.bullet("Ordre de insertion conservé en Python 3.7+")
pdf.bullet("Modifiable (mutable) : on peut ajouter, modifier, supprimer des éléments")

# ---------- CREATION ----------
pdf.section_title("Création de dictionnaires", "II.")
pdf.sub_title("Méthode 1 : Avec des accolades")
pdf.body("La syntaxe la plus courante utilise des accolades {} avec des paires clé:valeur séparées par des virgules.")
pdf.body("Exemple :")
pdf.code_block("""# Création d'un dictionnaire
etudiant = {
    "nom": "Dupont",
    "prenom": "Jean",
    "age": 20,
    "specialite": "Informatique"
}
print(etudiant)
# Résultat : {'nom': 'Dupont', 'prenom': 'Jean', 'age': 20, 'specialite': 'Informatique'}
""")
pdf.body("Exemple 2 :")
pdf.code_block("""# Dictionnaire vide
vide = {}
print(vide)  # {}

# Avec des valeurs
scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
print(scores)  # {'Alice': 95, 'Bob': 87, 'Charlie': 92}
""")
pdf.sub_title("Méthode 2 : Avec la fonction dict()")
pdf.body("La fonction dict() crée un dictionnaire à partir de différents arguments.")
pdf.code_block("""# Avec des paires clé=valeur
etudiant = dict(nom="Dupont", prenom="Jean", age=20)
print(etudiant)  # {'nom': 'Dupont', 'prenom': 'Jean', 'age': 20}

# A partir d'une liste de tuples
donnees = [("nom", "Dupont"), ("prenom", "Jean")]
etudiant2 = dict(donnees)
print(etudiant2)  # {'nom': 'Dupont', 'prenom': 'Jean'}
""")

# ---------- ACCES ----------
pdf.section_title("Accès et modification", "III.")
pdf.sub_title("Accéder à une valeur")
pdf.body("Pour récupérer une valeur, on utilise la clé entre crochets [] ou la méthode get().")
pdf.code_block("""# Accès avec les crochets
print(etudiant["nom"])     # Dupont
print(etudiant["age"])     # 20

# Accès avec get() - plus safe
print(etudiant.get("nom"))     # Dupont
print(etudiant.get("adresse")) # None (pas d'erreur)
print(etudiant.get("adresse", "Inconnue"))  # Inconnue
""")
pdf.body("La méthode get() est recommandée car elle ne lève pas d'erreur si la clé n'existe pas.")
pdf.sub_title("Modifier ou ajouter un élément")
pdf.body("Pour modifier une valeur existante ou ajouter une nouvelle clé, on utilise la même syntaxe.")
pdf.code_block("""# Modifier une valeur existante
etudiant["age"] = 21
print(etudiant)  # {'nom': 'Dupont', 'prenom': 'Jean', 'age': 21}

# Ajouter une nouvelle clé
etudiant["email"] = "jean.dupont@univ.fr"
print(etudiant)  # Ajoute la clé 'email'

# Méthode update() pour fusionner
etudiant.update({"phone": "0123456789", "adresse": "12 rue Exemple"})
print(etudiant)
""")

# ---------- SUBTITRES ----------
pdf.section_title("Suppression d'éléments", "IV.")
pdf.body("Pour supprimer un élément d'un dictionnaire, on utilise del ou la méthode pop().")
pdf.code_block("""# Supprimer avec del
del etudiant["phone"]
print(etudiant)

# Supprimer avec pop()
email = etudiant.pop("email")
print(email)        # "jean.dupont@univ.fr"
print(etudiant)     # sans email

# Pop avec valeur par défaut
ville = etudiant.pop("ville", "Paris")  # retourne "Paris" si la clé n'existe pas
""")
pdf.sub_title("Tester si une clé existe")
pdf.body("La méthode in permet de vérifier si une clé est présente.")
pdf.code_block("""if "nom" in etudiant:
    print("La clé 'nom' existe")
else:
    print("La clé 'nom' n'existe pas")

# Condition avec get()
if etudiant.get("adresse"):
    print("L'adresse est définie")
""")

# ---------- ITERATION ----------
pdf.section_title("Itération sur un dictionnaire", "V.")
pdf.body("On peut parcourir un dictionnaire de plusieurs façons : par les clés, par les valeurs, ou par les paires clé-valeur.")
pdf.sub_sub_title("Par les clés")
pdf.code_block("""for cle in etudiant:
    print(cle, "=>", etudiant[cle])
""")
pdf.sub_sub_title("Par les valeurs")
pdf.code_block("""for valeur in etudiant.values():
    print(valeur)
""")
pdf.sub_sub_title("Par les paires (clé, valeur)")
pdf.code_block("""for cle, valeur in etudiant.items():
    print(f"{cle} => {valeur}")
""")

# ---------- METHODES ESLAIRE ----------
pdf.section_title("Méthodes essentielles", "VI.")
pdf.sub_sub_title("keys()")
pdf.body("Retourne une vue des clés du dictionnaire.")
pdf.code_block("""cles = etudiant.keys()
print(cles)  # dict_keys(['nom', 'prenom', 'age'])
print(list(cles))  # ['nom', 'prenom', 'age']
""")
pdf.sub_sub_title("values()")
pdf.body("Retourne une vue des valeurs.")
pdf.code_block("""vals = etudiant.values()
print(vals)  # dict_values(['Dupont', 'Jean', 21])
""")
pdf.sub_sub_title("items()")
pdf.body("Retourne une vue des paires clé-valeur.")
pdf.code_block("""pairs = etudiant.items()
print(pairs)  # dict_items([('nom', 'Dupont'), ('prenom', 'Jean'), ('age', 21)])
""")
pdf.sub_sub_title("clear()")
pdf.body("Supprime tous les éléments du dictionnaire.")
pdf.code_block("""etudiant.clear()
print(etudiant)  # {}
""")
pdf.sub_sub_title("copy()")
pdf.body("Retourne une copie superficielle du dictionnaire.")
pdf.code_block("""nouveau = etudiant.copy()
print(nouveau)  # {'nom': 'Dupont', 'prenom': 'Jean', 'age': 21}
""")

# ---------- COMPREHENSION ----------
pdf.section_title("Compréhension de dictionnaire", "VII.")
pdf.body("La compréhension de dictionnaire permet de créer un dictionnaire en une seule ligne.")
pdf.code_block("""# Carré des nombres pairs
carrés = {x: x**2 for x in range(6) if x % 2 == 0}
print(carrés)  # {0: 0, 2: 4, 4: 16}

# Conversion de listes en dictionnaire
noms = ["Alice", "Bob", "Charlie"]
notes = [15, 12, 18]
dico = {nom: note for nom, note in zip(noms, notes)}
print(dico)  # {'Alice': 15, 'Bob': 12, 'Charlie': 18}
""")
pdf.body("Cette syntaxe est concise et souvent plus efficace que une boucle for classique.")

# ---------- EXERCICES ----------
pdf.section_title("Exercices pratiques", "VIII.")
pdf.sub_title("Exercice 1 : Comptage de mots")
pdf.body("Écrire un programme qui compte le nombre d'occurrences de chaque mot dans une chaîne.")
pdf.code_block("""def compter_mots(texte):
    liste = texte.lower().split()
    dico = {}
    for mot in liste:
        dico[mot] = dico.get(mot, 0) + 1
    return dico

texte = "Python est un langage Python facile"
print(compter_mots(texte))
# {'python': 2, 'est': 1, 'un': 1, 'langage': 1, 'facile': 1}
""")
pdf.sub_title("Exercice 2 : Fusion de dictionnaires")
pdf.body("Fusionner deux dictionnaires en un seul.")
pdf.code_block("""# Méthode 1 : update()
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1.update(d2)
print(d1)  # {'a': 1, 'b': 3, 'c': 4}

# Méthode 2 : {**d1, **d2}
fusion = {**d1, **d2}
print(fusion)  # {'a': 1, 'b': 3, 'c': 4}
""")
pdf.sub_title("Exercice 3 : Tri d'un dictionnaire")
pdf.body("Trier un dictionnaire par valeurs décroissantes.")
pdf.code_block("""notes = {"Alice": 15, "Bob": 12, "Charlie": 18, "Diana": 14}
# Tri par valeurs
tri = dict(sorted(notes.items(), key=lambda x: x[1], reverse=True))
print(tri)
# {'Charlie': 18, 'Alice': 15, 'Diana': 14, 'Bob': 12}
""")

# ---------- POINTS DE VIGILANCE ----------
pdf.section_title("Points de vigilance", "IX.")
pdf.body("Voici les erreurs fréquentes à éviter :")
pdf.bullet("Utiliser une clé inexistante avec [] -> lève une KeyError")
pdf.bullet("Ne pas confondre une clé avec un index (dico[0] n'a pas de sens si les clés sont des chaînes)")
pdf.bullet("Un dictionnaire ne peut pas avoir de clés en double (la seconde écrashe la première)")
pdf.bullet("Les clés doivent être immuables (pas de listes comme clés)")
pdf.bullet("Les clés doivent être uniques : dico = {'a': 1, 'a': 2} donne {'a': 2}")
pdf.code_block("""# Erreur fréquente
dico = {}
dico["a"] = 1
dico["a"] = 2  # Remplace la valeur
print(dico)  # {'a': 2}

# Bonne pratique : vérifier avant l'accès
if "cle" in dico:
    print(dico["cle"])
""")

# ---------- CONCLUSION ----------
pdf.section_title("En résumé", "X.")
pdf.body("Un dictionnaire Python est un conteneur mutable qui stocke des paires clé-valeur.")
pdf.body("Points clés :")
pdf.bullet("Accès via des clés (pas des indices numériques)")
pdf.bullet("Clés uniques et immuables")
pdf.bullet("Méthodes utiles : keys(), values(), items(), get(), pop()")
pdf.bullet("Compréhension de dictionnaire pour créer rapidement")
pdf.bullet("Utile pour les données structurées et les correspondances")

pdf.ln(10)
pdf.set_font("Arial", "I", 9)
pdf.set_text_color(0x77, 0x77, 0x77)
pdf.cell(0, 6, "Fin du cours - N'hésitez pas à pratiquer avec des exemples !", align="C")

# ---------- SAVE ----------
pdf.output(r"C:\Users\HP OMEN\OneDrive\01_Projet_Manager\Cours_Dictionnaires_Python.pdf")
print(f"PDF généré : C:\\Users\\HP OMEN\\OneDrive\\01_Projet_Manager\\Cours_Dictionnaires_Python.pdf")

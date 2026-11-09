"""
Module principal du jeu de devinette d'expressions françaises.
Ce module contient la logique principale du jeu.
"""

import random
import datetime

# Liste de phrases françaises (expressions idiomatiques)
EXPRESSIONS = [
    "mieux vaut un œuf que deux autres qui ne sont pas",
    "à petit bout par petit bout",
    "tendre une careueuse",
    "faire la fête",
    "haut lieu",
    "il pleut des cordes",
    "la bouche en l'air",
    "donner un coup de fil",
    "prendre un tarif",
    "s'arracher la moustache",
    "se noyer dans un verre d'eau",
    "avoir le cafard",
    "un tour de jambe",
    "mettre la charrue avant le bœuf",
    "tirer les conséquences",
    "faire la grasse matinée",
    "se casser la tête",
    "être aux abois",
    "faire la paix",
    "faire plus vite qu'un fou",
    "avoir un poil dans la main",
    "tomber dans de bonnes griffes",
    "avoir la pêche",
    "être dans l'œuf",
    "être dans la lune",
    "vert de gris",
    "tirer les filons",
    "se faire une image",
    "mettre en veille",
    "passer à la vitesse du son",
    "être dans le rouge",
    "faire la morale",
    "en avoir marre",
    "couvrir de poulets",
    "devenir un légume",
    "avoir l'air du coup",
    "faire la tournée",
    "donner rendez-vous",
    "être dans l'engrenage",
    "mettre les dents longues",
    "être de bonne faculté",
    "passer à la vitesse du son",
]

# Expressions plus courtes pour les débutants
EXPRESSIONS_COURTES = [
    "faire la fête",
    "avoir le cafard",
    "être dans l'œuf",
    "avoir la pêche",
    "mieux vaut un œuf",
    "faire la morale",
    "tendre une careueuse",
    "donner rendez-vous",
    "être aux abois",
    "se casser la tête",
]


def choisir_expression_journee():
    """
    Choisit une expression selon la date du jour.
    Les jours pairs utilisent des expressions plus courtes.
    """
    jour = datetime.date.today().day
    semaine = datetime.date.today().isocalendar()[1]

    # Si c'est un jour pair, utilise des expressions plus courtes
    if jour % 2 == 0:
        return random.choice(EXPRESSIONS_COURTES)
    else:
        return random.choice(EXPRESSIONS)


def afficher_expression_cachée(expression):
    """
    Affiche l'expression avec les lettres masquées.
    Les premières et dernières lettres sont visibles.
    """
    # Masquer tous les caractères sauf les premières et dernières
    if len(expression) <= 4:
        return expression  # Pas assez long pour masquer
    else:
        debut = expression[0]
        fin = expression[-1]
        milieu = "_" * (len(expression) - 2)
        return debut + milieu + fin


def afficher_indications():
    """Affiche les indices pour l'utilisateur."""
    print("📝 Indices :")
    print("  • La réponse fait environ 3-6 mots")
    print("  • Cherche des expressions idiomatiques françaises")
    print("  • Exemples : 'faire la fête', 'avoir le cafard'")


def verifier_reponse(reponse, expression):
    """
    Vérifie si la réponse est correcte.
    
    Returns:
        tuple: (booléen de réussite, message d'erreur)
    """
    # Nettoyer la réponse
    reponse = reponse.strip().lower()
    expression = expression.lower()

    # Comparaison simple
    if reponse == expression:
        return True, "Parfait ! 🎉"

    # Vérifier si la réponse est l'une des mots
    mots_expression = expression.split()
    if reponse in mots_expression:
        return False, "Presque ! Essaye encore."

    return False, "Pas exactement. Essaye encore !"


def jouer():
    """
    Fonction principale du jeu.
    Gère le flux de jeu complet.
    """
    print("=" * 50)
    print("🎯 JEU : DEVINE L'EXPRESSION FRANÇAISE")
    print("=" * 50)
    print("💡 Chaque jour, une nouvelle expression est cachée.")
    print("💡 Trouve la réponse complète pour gagner !")
    print("=" * 50)
    print()

    # Choisir l'expression du jour
    expression = choisir_expression_journee()
    afficher_indications()

    # Afficher l'expression masquée
    print("\n🔍 Expression cachée :")
    print("   " + afficher_expression_cachée(expression))
    print()

    # Demander la réponse
    reponse = input("👉 Ta réponse : ").strip()

    # Vérifier la réponse
    correct, message = verifier_reponse(reponse, expression)

    if correct:
        print("🎉 TU AS GAGNÉ !")
        print(f"✅ La bonne réponse était : {expression}")
        print("🎉 Félicitations ! Tu as deviné l'expression.")
    else:
        print(f"❌ {message}")
        print(f"💡 La réponse était : {expression}")

    # Affichage de statistiques (optionnel)
    print(f"\n📅 Jour du jeu : {datetime.date.today().strftime('%d/%m/%Y')}")
    print(f"📝 Expression jouée : {expression}")


if __name__ == "__main__":
    jouer()

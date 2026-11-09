#!/usr/bin/env python
"""
Script de setup pour le projet de devinette d'expressions françaises.

Ce script permet d'installer les dépendances et de préparer le projet.
"""

import subprocess
import sys
import os


def run_command(command, description=None):
    """
    Exécute une commande shell et affiche les résultats.
    
    Args:
        command (str): Commande shell à exécuter
        description (str): Description de la commande (optionnel)
    
    Returns:
        bool: True si la commande a réussi, False sinon
    """
    if description:
        print(f"\n🔧 {description}...")
    
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        print(f"✅ {description} réussi !")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de {description}:")
        print(e.stderr)
        return False


def installer_dependencies():
    """Installe les dépendances du projet."""
    print("📦 Installation des dépendances...")
    return run_command("python -m pip install -r requirements.txt", "Installation des dépendances")


def creer_structure_dossiers():
    """Crée la structure de dossiers recommandée."""
    print("📁 Création de la structure des dossiers...")
    
    directories = [
        "src",
        "src/jeu",
        "tests",
        "scripts",
        "docs",
        "data",
        "output"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"  ✅ Création de {directory}")
    
    return True


def creer_fichiers_vides():
    """Crée les fichiers de configuration vides."""
    print("📄 Création des fichiers de configuration...")
    
    files = [
        "src/__init__.py",
        "tests/__init__.py",
        "scripts/__init__.py",
        ".gitignore",
        "requirements.txt",
        "README.md",
        "main.py",
        "LICENSE"
    ]
    
    for file in files:
        if not os.path.exists(file):
            with open(file, 'w') as f:
                pass
            print(f"  ✅ Création de {file}")
    
    return True


def afficher_liens_ressources():
    """Affiche les liens vers les ressources utiles."""
    print("\n🔗 Ressources utiles :")
    print("  • Documentation Python : https://docs.python.org/3/")
    print("  • Documentation fpdf2 : https://fpdf2.readthedocs.io/")
    print("  • Git : https://git-scm.com/doc")
    print("  • GitHub : https://docs.github.com/")


def main():
    """Fonction principale du script de setup."""
    print("=" * 60)
    print("🎯 SCRIPT DE SETUP DU PROJET")
    print("=" * 60)
    print()
    
    # Vérifier les dépendances
    if not installer_dependencies():
        print("❌ Erreur lors de l'installation des dépendances")
        return False
    
    # Créer la structure des dossiers
    if not creer_structure_dossiers():
        print("❌ Erreur lors de la création des dossiers")
        return False
    
    # Créer les fichiers vides
    if not creer_fichiers_vides():
        print("❌ Erreur lors de la création des fichiers")
        return False
    
    # Afficher les ressources
    afficher_liens_ressources()
    
    print("\n" + "=" * 60)
    print("✅ INSTALLATION TERMINÉE AVEC SUCCÈS !")
    print("=" * 60)
    print("\n🚀 Pour démarrer le jeu, exécute :")
    print("   python main.py")
    print("\n🔍 Lancer les tests avec :")
    print("   pytest tests/")
    print("\n📖 Consultez le README.md pour plus d'informations.")
    print("=" * 60)
    
    return True


if __name__ == "__main__":
    main()

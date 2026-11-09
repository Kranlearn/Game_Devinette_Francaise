"""
Tests pour le jeu de devinette d'expressions françaises.
"""

import unittest
from src.jeu import (
    choisir_expression_journee,
    afficher_expression_cachée,
    verifier_reponse,
    EXPRESSIONS,
    EXPRESSIONS_COURTES,
)


class TestJeu(unittest.TestCase):
    """Tests unitaires pour le jeu de devinette."""

    def test_choisir_expression_journee(self):
        """Test de la fonction de sélection d'expression."""
        expression = choisir_expression_journee()
        self.assertIsInstance(expression, str)
        self.assertGreater(len(expression), 0)

    def test_afficher_expression_cachée(self):
        """Test de la fonction de masquage d'expression."""
        expression = "test"
        resultat = afficher_expression_cachée(expression)
        self.assertEqual(resultat, "test")  # Trop court, pas de masquage

        expression = "bonjour"
        resultat = afficher_expression_cachée(expression)
        self.assertEqual(len(resultat), len(expression))
        self.assertEqual(resultat[0], "b")  # Première lettre
        self.assertEqual(resultat[-1], "r")  # Dernière lettre

    def test_verifier_reponse_correcte(self):
        """Test de vérification avec réponse correcte."""
        reponse = "bonjour"
        expression = "bonjour"
        resultat, message = verifier_reponse(reponse, expression)
        self.assertTrue(resultat)
        self.assertIn("Parfait", message)

    def test_verifier_reponse_incorrecte(self):
        """Test de vérification avec réponse incorrecte."""
        reponse = "hello"
        expression = "bonjour"
        resultat, message = verifier_reponse(reponse, expression)
        self.assertFalse(resultat)
        self.assertIn("Pas exactement", message)

    def test_expressions_definies(self):
        """Test que les listes d'expressions sont bien définies."""
        self.assertGreater(len(EXPRESSIONS), 0)
        self.assertGreater(len(EXPRESSIONS_COURTES), 0)
        self.assertNotEqual(EXPRESSIONS, EXPRESSIONS_COURTES)


if __name__ == "__main__":
    unittest.main()

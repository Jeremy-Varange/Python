import unittest
from Question import Question

class TestQCM(unittest.TestCase):
    def setUp(self):
        # Liste des questions avec leurs réponses
        self.questions = [
            ("Qu'est-ce qu'une attaque de phishing ?", ["Un logiciel malveillant", "Une tentative d'usurpation d'identité en ligne", "Un virus informatique"], "b"),
            ("Quel est l'objectif principal d'un pare-feu ?", ["Protéger contre les virus", "Contrôler le trafic réseau", "Améliorer les performances du système"], "b"),
            ("Quel protocole cryptographique est couramment utilisé pour sécuriser les communications sur Internet ?", ["HTTP", "HTTPS", "FTP"], "b"),
            ("Qu'est-ce qu'un logiciel antivirus ?", ["Un programme qui détecte et supprime les logiciels malveillants", "Un programme qui empêche les attaques de déni de service", "Un outil pour optimiser les performances du système"], "a"),
            ("Quelle est la meilleure pratique pour créer un mot de passe fort ?", ["Utiliser des mots courants", "Utiliser le même mot de passe pour plusieurs comptes", "Utiliser une combinaison de lettres, chiffres et caractères spéciaux"], "c"),
            ("Qu'est-ce qu'une authentification à deux facteurs (MFA) ?", ["Un processus de vérification en deux étapes", " La protection d'un réseau par deux pare-feu", "L'utilisation de deux logiciels antivirus simultanément"], "a"),
            ("Quel est l'objectif principal d'un VPN ?", ["Améliorer la vitesse de connexion Internet", "Masquer l'adresse IP de l'utilisateur", "Augmenter la capacité de stockage du système"], "b"),
            ("Que signifie l'acronyme 'DDoS' ?", ["Défense et Détection des Systèmes", "Distribution Délibérée de Services", "Déni de Service Distribué"], "c"),
            ("Quel type d'attaque implique l'envoi de données malveillantes dans le but de tromper un système pour qu'il effectue des actions non autorisées ?", ["Attaque par force brute", "Attaque par ingénierie sociale", "Attaque par injection SQL"], "c"),
            ("Que fait un pare-feu d'application Web (WAF) ?", ["Surveiller et filtrer le trafic HTTP vers une application Web", "Protéger contre les attaques au niveau du réseau", "Analyser les fichiers malveillants sur un ordinateur"], "a")
        ]

        # Liste des instances de Question
        self.questions_instances = [Question(enonce, choix, reponse) for enonce, choix, reponse in self.questions]

    def test_est_correcte(self):
        # Teste la méthode est_correcte de la classe Question pour chaque question du QCM

        for i, question in enumerate(self.questions_instances, start=1):
            with self.subTest(question=f"Question {i}"):
                # Teste le cas où la réponse utilisateur est correcte
                question.reponse_utilisateur = question.reponse  # Définit la réponse de l'utilisateur comme correcte
                self.assertTrue(question.est_correct(question.reponse_utilisateur), f"Réponse attendue pour la question {i} : {question.reponse}")

                # Teste le cas où la réponse utilisateur est incorrecte
                reponse_incorrecte = [choix for choix in question.choix if choix != question.reponse][0]
                question.reponse_utilisateur = reponse_incorrecte  # Définit la réponse de l'utilisateur comme incorrecte
                self.assertFalse(question.est_correct(question.reponse_utilisateur), f"Réponse attendue pour la question {i} : {question.reponse}")

if __name__ == '__main__':
    unittest.main()

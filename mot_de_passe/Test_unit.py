import unittest
from main import Testeur_mdp, Gen_mdp, EFF

class Test_unit(unittest.TestCase):
    def setUp(self):
        self.password_calculator = Testeur_mdp(0)
        self.password_generator = Gen_mdp()
        self.passphrase_generator = EFF()

    def test_calculate_strength(self):

        # Test de force faible
        weak_password = "password"
        self.assertEqual(self.password_calculator.calculate_strength(weak_password), "La force du mot de passe password est très faible")

        # Test de force moyenne
        medium_password = "P@ssw0rd"
        self.assertEqual(self.password_calculator.calculate_strength(medium_password), "La force du mot de passe P@ssw0rd est très faible")

        # Test de force forte
        strong_password = "Str0ngP@ssw0rd&&@sscdjd!"
        self.assertEqual(self.password_calculator.calculate_strength(strong_password), "La force du mot de passe Str0ngP@ssw0rd&&@sscdjd! est fort")

    def test_generate_password(self):

        # Test de génération de mot de passe
        generated_password = self.password_generator.generate_password(4, 4, 4, 4)
        self.assertEqual(len(generated_password), 16)

    def test_generate_passphrase(self):

        # Test de génération de passphrase
        generated_passphrase = self.passphrase_generator.generate_passphrase()
        self.assertEqual(len(generated_passphrase), 6)

if __name__ == '__main__':
    unittest.main()

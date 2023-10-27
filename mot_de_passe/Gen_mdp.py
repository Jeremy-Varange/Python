import random
import string
import math

class Gen_mdp:
    def __init__(self):
        self.alphabet = string.ascii_letters + string.digits + "!#$*%?,"
        self.special_chars = "&[|]@^µ§:/ ;.,<>°²³"

    # Génère un mot de passe en fonction du nombre spécifié de caractères minuscules, majuscules, chiffres et spéciaux
    def generate_password(self, lowercase_count, uppercase_count, digit_count, special_count):
        lowercase_chars = ''.join(random.choice(string.ascii_lowercase) for _ in range(lowercase_count)) #génère une chaîne de caractères (lowercase_chars) composée de lowercase_count lettres minuscules aléatoires.
        uppercase_chars = ''.join(random.choice(string.ascii_uppercase) for _ in range(uppercase_count))
        digit_chars = ''.join(random.choice(string.digits) for _ in range(digit_count))
        special_chars = ''.join(random.choice(self.special_chars) for _ in range(special_count))

        # Concatène les caractères générés et mélange le mot de passe
        password = lowercase_chars + uppercase_chars + digit_chars + special_chars
        password = ''.join(random.sample(password, len(password)))

        return password

    # Demande à l'utilisateur de saisir ses critères et le programme vérifie également les données saisies
    def verifier_input(self, texte):
        while True:
            try:
                return int(input(texte))
            except ValueError:
                print("Erreur : Veuillez entrer un chiffre valide.")
import math

class Testeur_mdp:
    def __init__(self, alphabet_size):
        self.alphabet_size = alphabet_size

    # Évaluation de la force du mot de passe en fonction de la valeur de strength
    def calculate_strength(self, password):
        password_length = len(password)
        self.alphabet_size = self.determine_alphabet_size(password)
        strength = password_length * math.log2(self.alphabet_size)
        print(f"L'entropie est égale à {math.floor(strength)} bits")
        if strength <= 64:
            return f"La force du mot de passe {password} est très faible"
        elif strength > 64 and strength < 80:
            return f"La force du mot de passe {password} est faible"
        elif strength >= 80 and strength < 100:
            return f"La force du mot de passe {password} est moyen"
        elif strength >= 100:
            return f"La force du mot de passe {password} est fort"

    # Détermination de la taille de l'alphabet en fonction des caractères présents dans le mot de passe
    def determine_alphabet_size(self, password):

        # Si le mot de passe contient des caractères spéciaux étendus
        if any(char in "&[|]@^µ§:/ ;.,<>°²³" for char in password):
            return 90

        # Si le mot de passe contient des caractères spéciaux standards
        elif any(char in "!#$*%?" for char in password):
            return 70

        # Si le mot de passe contient à la fois des lettres et des chiffres
        elif any(char.isalpha() for char in password) and any(char.isdigit() for char in password):
            return 62

        # Si le mot de passe contient à la fois des lettres minuscules, majuscules et des chiffres
        elif any(char.isalpha() for char in password) and any(char.islower() for char in password) and any(
                char.isupper() for char in password):
            return 52

        # Si le mot de passe contient uniquement des lettres
        elif any(char.isalpha() for char in password):
            return 26

        # Si le mot de passe contient des chiffres et des lettres majuscules
        elif any(char.isdigit() for char in password) and any(
                char.isalpha() and char.upper() <= 'Z' for char in password):
            return 36

        # Si le mot de passe contient des chiffres et des lettres majuscules jusqu'à F
        elif any(char.isdigit() for char in password) and any(
                char.isalpha() and char.upper() <= 'F' for char in password):
            return 16

        # Si le mot de passe contient uniquement des 0 et des 1
        elif all(char in '01' for char in password):
            return 2

        # Si le mot de passe contient uniquement des chiffres
        elif any(char.isdigit() for char in password):
            return 10

        # Par défaut, retourne 70 (taille par défaut)
        else:
            return 70




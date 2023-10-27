import random

class EFF:
    def __init__(self):
        # Charger la liste de mots depuis le fichier EFF
        self.wordlist = self.load_wordlist()

    def load_wordlist(self):
        # Charger la liste de mots depuis le fichier EFF
        with open('wordlist.txt', 'r', encoding='utf-8') as file:
            return file.readlines()

    def roll_dice(self):
        # Simuler le lancer de dés
        return [random.randint(1, 6) for _ in range(5)]

    def find_word(self, dice_number):
        # Fonction qui recherche le mot correspondant au résultat des dés dans la liste de mots
        # Parcours chaque ligne dans la liste de mots
        for line in self.wordlist:
            # Si la ligne commence par le résultat des dés
            if line.startswith(str(dice_number) + '\t'):
                # Récupère le mot en le séparant à partir de la tabulation et le retourne en supprimant les espaces inutiles
                return line.split('\t')[1].strip()

        # Si aucun mot n'est trouvé pour le résultat des dés, retourne None
        return None

    def generate_passphrase(self):
        # Fonction qui génère une passphrase en lançant les dés plusieurs fois
        passphrase = []

        # Pour chaque lancer de dé
        for _ in range(6):
            # Simule le lancer de dés et convertit le résultat en un nombre
            dice_results = self.roll_dice()
            dice_number = int(''.join(map(str, dice_results)))

            # Recherche le mot correspondant au résultat des dés
            word = self.find_word(dice_number)

            # Si un mot est trouvé, l'ajoute à la passphrase, sinon affiche une erreur
            if word is not None:
                passphrase.append(word)
            else:
                print(f"Erreur: Impossible de trouver un mot pour le résultat des dés {dice_results}")

        # Retourne la passphrase sous forme de chaîne de caractères avec des tirets entre chaque mot
        return '-'.join(passphrase)

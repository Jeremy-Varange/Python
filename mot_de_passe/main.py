from Testeur_mdp import Testeur_mdp
from Gen_mdp import Gen_mdp
from EFF import EFF

# Menu
while True:
    print("<==============Menu==============>")
    print("1 - Testeur de la force d'un mot de passe")
    print("2 - Générateur de mot de passe aléatoire avec sa force")
    print("3 - Générateur de passphrase selon ma méthode de dés de l'EFF")
    print("4 - Quitter")
    password_calculator = Testeur_mdp(0)
    try:
        choix_menu = int(input("Veuillez choisir votre outil (1/2/3/4) : "))
    except ValueError:
        print("Veuillez saisir un nombre entier.")
        continue
    # Testeur de la force d'un mot de passe
    if choix_menu == 1:
        print("\n<============Testeur de la force d'un mot de passe============>\n")

        mdp_utilisateur = input("Entrez votre mot de passe: ")
        print(password_calculator.calculate_strength(mdp_utilisateur))

    # Générateur de mot de passe aléatoire avec sa force
    elif choix_menu == 2:
        print("\n<============Générateur de mot de passe aléatoire avec sa force============>\n")
        password_generator = Gen_mdp()
        try:
            nb_min = password_generator.verifier_input("Entrez le nombre de caractères minuscules: ")
            nb_maj = password_generator.verifier_input("Entrez le nombre de caractères majuscules: ")
            nb_chiffre = password_generator.verifier_input("Entrez le nombre de chiffres: ")
            nb_spec = password_generator.verifier_input("Entrez le nombre de caractères spéciaux: ")
        except ValueError:
            print("Veuillez saisir un nombre entier.")
            continue

        password = password_generator.generate_password(nb_min, nb_maj, nb_chiffre, nb_spec)

        print(f"Mot de passe généré: {password}")
        print(password_calculator.calculate_strength(password))

    # Générateur de passphrase selon ma méthode de dés de l'EFF
    elif choix_menu == 3:
        print("\n<============Générateur de passphrase selon ma méthode de dés de l'EFF============>\n")
        passphrase_generator = EFF()
        passphrase = passphrase_generator.generate_passphrase()
        print(passphrase)
        print(password_calculator.calculate_strength(passphrase))
    elif choix_menu == 4:
        break

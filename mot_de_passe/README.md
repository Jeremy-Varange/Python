# Projet 2 : Générateur et testeur de mot de passe

Voici une reformulation en paragraphe :

Développez un programme intégrant divers outils de sécurité. L'un de ces outils consiste en un testeur de mot de passe évaluant sa robustesse en se fondant sur l'entropie et en respectant les critères énoncés par l'ANSSI, disponibles à l'adresse suivante : https://www.ssi.gouv.fr/administration/precautionselementaires/calculer-la-force-dun-mot-de-passe/.

Une autre fonctionnalité du programme inclut un générateur de mots de passe aléatoires. L'utilisateur aura la possibilité de définir des critères tels que le nombre de minuscules, de majuscules, de chiffres et de caractères spéciaux. Le mot de passe généré sera présenté avec son entropie et sa force.

Par ailleurs, le programme comportera également un générateur de passphrase, s'inspirant de la méthode des dés de l'EFF. Pour plus de clarté et de modularité, le code sera structuré en utilisant des classes et des objets. De plus, il sera organisé en plusieurs fichiers distincts, importés en tant que modules pour assurer une meilleure lisibilité du code.

## Fonctionnalités

Voici la liste des fonctionnalités du programme que vous avez décrit :

1. **Testeur de Mot de Passe :**
   - Évalue la robustesse d'un mot de passe.
   - Basé sur l'entropie.
   - Respecte les critères de l'ANSSI.

2. **Générateur de Mot de Passe Aléatoire :**
   - Permet à l'utilisateur de définir des critères.
   - Nombre de minuscules, de majuscules, de chiffres, de caractères spéciaux.
   - Affiche le mot de passe généré avec son entropie et sa force.

3. **Générateur de Passphrase :**
   - Utilise la méthode des dés de l'EFF.
   - Génère des passphrases sécurisées.

4. **Utilisation de Classes et d'Objets :**
   - Organisation du code en utilisant des classes et des objets pour une meilleure structure.
   
5. **Modularité du Code :**
   - Séparation du code en plusieurs fichiers distincts.
   - Importation des fichiers en tant que modules pour une meilleure gestion du code.

Chaque fonctionnalité vise à renforcer la sécurité des informations sensibles en fournissant des outils permettant de créer et d'évaluer des éléments d'identification sécurisés.

## Installation

1. Clonez ce dépôt sur votre machine locale :

   ```
   git clone https://github.com/Jeremy-Varange/Python.git
   ```

2. Accédez au répertoire du projet :

   ```
   cd Python/
   ```

3. Lancez l'application :

   ```
   python main.py
   ```

4. Lancez les tests unitaires

   ```
   python Test.py
   ```

## Utilisation

Pour utiliser le programme, suivez ces étapes :

1. **Testeur de Mot de Passe :**
   - Choisissez l'option 1.
   - Entrez le mot de passe que vous souhaitez évaluer.
   - Le programme affichera la force du mot de passe en fonction de l'entropie.

2. **Générateur de Mot de Passe Aléatoire :**
   - Choisissez l'option 2.
   - Suivez les instructions pour définir les critères du mot de passe.
   - Le programme générera un mot de passe aléatoire et affichera son entropie et sa force.

3. **Générateur de Passphrase :**
   - Choisissez l'option 3.
   - Le programme utilisera la méthode des dés de l'EFF pour créer une passphrase sécurisée.

4. **Quitter le Programme :**
   - Choisissez l'option 4 pour quitter le programme.

À chaque étape, suivez les instructions affichées à l'écran et interagissez avec le programme en saisissant les informations requises. Les outils de sécurité vous permettent d'évaluer la robustesse des mots de passe, de générer des mots de passe aléatoires et des passphrases sécurisées.

## Auteurs

Codé par Jérémy VARANGE

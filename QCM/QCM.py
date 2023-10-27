import random
from Question import Question

class QCM:
    def __init__(self):
        self.questions = []
        self.choix_faux = []
        self.score = 0

    def ajouter_question(self, question):
        self.questions.append(question)

    def nb_lettre(self, nombre):
        return chr(ord('a') + nombre - 1)

    def demarrer_QCM(self):
        try:
            random.shuffle(self.questions)

            for i, question in enumerate(self.questions, start=1):
                while True:
                    print(f"Question {i}: {question.enonce}")

                    # Liste des indices des réponses, y compris la réponse correcte
                    indices = [str(x) for x in range(1, len(question.choix) + 1)]

                    # Mélanger les indices
                    random.shuffle(indices)

                    # Afficher les choix dans l'ordre mélangé
                    for index in indices:
                        print(f"{self.nb_lettre(int(index))}){question.choix[int(index) - 1]}")

                    choix_utilisateur = input("Quel est votre choix ? (a/b/c)").lower()

                    if choix_utilisateur in ['a', 'b', 'c']:
                        break
                    else:
                        print("Veuillez saisir une réponse valide (a/b/c).")

                if question.est_correct(choix_utilisateur):
                    self.score += 1
                else:
                    self.choix_faux.append(i)

            self.resultats()

        except Exception as e:
            print(f"Erreur: {e}")

    def resultats(self):
        print(f"Votre score : {self.score}/{len(self.questions)}\n")
        for num_question, index in enumerate(self.choix_faux, start=1):
            print(
                f"La réponse à la question {index} ({self.questions[index - 1].enonce}) est la réponse {self.questions[index - 1].reponse}")
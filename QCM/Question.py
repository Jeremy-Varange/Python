class Question:
    def __init__(self, enonce, choix, reponse):
        self.enonce = enonce
        self.choix = choix
        self.reponse = reponse

    def est_correct(self, choix_utilisateur):
        return choix_utilisateur.lower() == self.reponse.lower()
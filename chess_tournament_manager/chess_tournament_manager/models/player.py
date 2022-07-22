class Player:
    def __init__(self, lastname="", firstname="", date_of_birth="", sexe="", rank="", score=""):
        self.lastname = lastname
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.sexe = sexe
        self.rank = rank
        self.score = score
        
    def __repr__(self):
        return f"Nom : {self.firstname}, Prénom : {self.lastname}, Date de naissance : {self.date_of_birth}, Genre : {self.sexe}, Rang : {self.rank}, Score : {self.score}"
    
    def add_player_infos(self):
        self.firstname = input("Veuillez entrer le nom de famille du joueur : ")
        self.lastname = input("Veuillez entrer le prénom du joueur : ")
        self.date_of_birth = input("Veuillez la date de naissance du joueur : ")
        self.sexe = input("Veuillez entrer le sexe du joueur : ")
        self.rank = input("Veuillez entrer le classement du joueur : ")
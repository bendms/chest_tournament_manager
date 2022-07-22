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
        
    def update_score(self, match, user_response):
    # for match in self.list_of_match:
        if user_response == "1" :
            match.player_1_result += 1
        elif user_response == "2":
            match.player_2_result += 1
        elif user_response == "0":
            match.player_1_result += 0.5
            match.player_2_result += 0.5
        else:
            print("Veuillez entrer 0, 1 ou 2")
        print(f"\n#### Le match a bien été mis à jour ####\n", match, "\n\n")
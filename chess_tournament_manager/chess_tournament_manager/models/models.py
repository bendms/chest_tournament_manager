from typing import List
from models.player import Player

class Tournament:
    def __init__(self, name="", location="", date="", nb_rounds=4, players=[], time_control="", description=""):
        self.name = name
        self.location = location
        self.date = date
        self.nb_rounds = nb_rounds
        self.players: List[Player] = []
        self.time_control = time_control
        self.description = description


    
    def create_new_tournament(self):
        if self.name == "":
            self.name = input("Veuillez entrer le nom du tournois : ")
            print(f"Le tournois se nomme '{self.name}'")
    
    def add_player(self, player):
        self.players.append(player)
        print(f"Voici la liste des joueurs : ")
        for player in self.players: 
            print(f"- {player.firstname} {player.lastname} -> classement : {player.rank}")
    
    def create_pair_of_players(self):
        """Au début du premier tour, triez tous les joueurs en fonction de leur classement.
Divisez les joueurs en deux moitiés, une supérieure et une inférieure. Le meilleur joueur de la moitié supérieure est jumelé avec le meilleur joueur de la moitié inférieure, et ainsi de suite. Si nous avons huit joueurs triés par rang, alors le joueur 1 est jumelé avec le joueur 5, le joueur 2 est jumelé avec le joueur 6, etc.
Au prochain tour, triez tous les joueurs en fonction de leur nombre total de points. Si plusieurs joueurs ont le même nombre de points, triez-les en fonction de leur rang.
Associez le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4, et ainsi de suite. Si le joueur 1 a déjà joué contre le joueur 2, associez-le plutôt au joueur 3.
Répétez les étapes 3 et 4 jusqu'à ce que le tournoi soit terminé."""
        pass
    
    def sorted_list_of_player_for_round_1(self):
        for self.players.rank in self.players:
            sorted(self.players, reverse = True)
            print(self.players.rank)
                

class Round:
    def __init__(self, list_of_match = [], name_of_round= "", date_and_hour_start= "", date_and_hour_end= ""):
        self.list_of_match = list_of_match
        self.name_of_round = name_of_round
        self.date_and_hour_start = date_and_hour_start
        self.date_and_hour_end = date_and_hour_end
    
    def create_new_round(self):
        pass
    
    def show_winners(self):
        pass

    def get_list_of_match(self):
        pass
    
class Match:
    def __init__(self, player_1, player_1_result, player_2, player_2_result):
        self.player_1 = player_1
        self.player_1_result = player_1_result
        self.player_2 = player_2
        self.player_2_result = player_2_result

    def get_match_tuple(self):
        match_tuple = (self.player_1, self.player_1_result, self.player_2, self.player_2_result)
        return match_tuple
        
class Player:
    def __init__(self, lastname="", firstname="", date_of_birth="", sexe="", rank=""):
        self.lastname = lastname
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.sexe = sexe
        self.rank = rank
    
    def add_player_infos(self):
        self.firstname = input("Veuillez entrer le nom de famille du joueur : ")
        self.lastname = input("Veuillez entrer le prénom du joueur : ")
        self.date_of_birth = input("Veuillez la date de naissance du joueur : ")
        self.sexe = input("Veuillez entrer le sexe du joueur : ")
        self.rank = input("Veuillez entrer le classement du joueur : ")
        
    


    
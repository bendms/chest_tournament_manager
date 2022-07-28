from typing import List


from models.player import Player
from models.match import Match
from models.round import Round


class Tournament():
    def __init__(self, name="", location="", date="", nb_rounds=4, time_control="", description="", players=[], rounds=[]):
        self.name = name
        self.location = location
        self.date = date
        self.nb_rounds = nb_rounds
        self.time_control = time_control
        self.description = description
        self.players: List[Player] = []
        self.rounds: List[Round] = []
            
    def create_new_tournament(self):
        if self.name == "":
            self.name = input("Veuillez entrer le nom du tournois : ")
            print(f"Le tournois se nomme '{self.name}'")
        if self.location == "":
            self.location = input("Veuillez entrer la localisation du tournois : ")
            print(f"Le tournois se nomme '{self.location}'")
        if self.description == "":
            self.description = input("Veuillez entrer la description du tournois : ")
            print(f"Le tournois se nomme '{self.description}'")
            
    def add_player(self, player):
        print(f"Voici la liste des joueurs : ")
        for player in self.players: 
            print(f"- {player.firstname} {player.lastname} -> classement : {player.rank}")
        self.players.append(player)
    
    def sorted_list_of_player_for_round_1(self):
        return self.players.sort(key=lambda player: player.rank, reverse=True)

    def sorted_list_of_player_for_next_rounds(self):
        self.players.sort(key=lambda player: player.rank, reverse=True)
        self.players.sort(key=lambda player: player.score, reverse=True)
              
    def add_round(self, round):
        self.rounds.append(round)
    
    def create_pair_of_players(self):
        """Au début du premier tour, triez tous les joueurs en fonction de leur classement.
Divisez les joueurs en deux moitiés, une supérieure et une inférieure. Le meilleur joueur de la moitié supérieure est jumelé avec le meilleur joueur de la moitié inférieure, et ainsi de suite. Si nous avons huit joueurs triés par rang, alors le joueur 1 est jumelé avec le joueur 5, le joueur 2 est jumelé avec le joueur 6, etc.
Au prochain tour, triez tous les joueurs en fonction de leur nombre total de points. Si plusieurs joueurs ont le même nombre de points, triez-les en fonction de leur rang.
Associez le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4, et ainsi de suite. Si le joueur 1 a déjà joué contre le joueur 2, associez-le plutôt au joueur 3.
Répétez les étapes 3 et 4 jusqu'à ce que le tournoi soit terminé."""
        pass
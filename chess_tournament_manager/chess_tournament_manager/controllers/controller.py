from typing import List
import json

from models.tournament import Tournament
from models.player import Player
from models.round import Round
from models.match import Match
from views.view import ViewMenu


class Controller:
    def __init__(self, tournament=Tournament, view=ViewMenu):
        #models 
        self.tournament = tournament
        
        #views
        self.view = view
        
        
    # def launch_program(self):
    #     self.view.display_menu()
    #     self.user_response = ViewMenu.get_user_response()
    #     if self.view.user_response == "1":
    #         tournament_test = Tournament()
    #         tournament_test.create_new_tournament()
    #         nb_player = input("Choisissez le nombre de joueurs : ")
    #         nb_player = int(nb_player)
    #         for player in range(nb_player):
    #             player = Player()
    #             player.add_player_infos()
    #             tournament_test.add_player(player = player)
    #         tournament_test.sorted_list_of_player_for_round_1()


    # def get_player(self):
    #     while len(self.tournament.players) < 8:
    #         self.view = self.tournament.players.append(Player.add_player_infos())
            
            
# tournament_for_test = Tournament(name = "test")
# controller = Controller(tournament_for_test)
# controller.get_player()


    
controller = Controller()
# controller.launch_program()

################################################################################################################################################

db_tournament = ["Tournois de Paris", "Paris", "20/07/2022", 4, "Tournois organisé à Paris durant l'été"]
        

db_players = [
            ["Jean", "Paul", "12/11/1982", "Homme", 1243], 
            ["Jacques", "Blade", "12/11/1985", "Homme", 1285], 
            ["Jeanne", "Logan", "12/10/1989", "Femme", 1125], 
            ["Simon", "Smith", "05/01/1986", "Homme", 1525],
            ["Alex", "John", "04/06/1982", "Homme", 1425],
            ["Elon", "Martel", "11/02/1984", "Homme", 1486],
            ["Thierry", "Louargan", "08/03/1980", "Homme", 1653],
            ["Thibault", "Darma", "09/08/1983", "Homme", 1110]
              ]

#Initialize instance of class Tournament 
tournament_testing = Tournament(name = db_tournament[0], location = db_tournament[1], date = db_tournament[2], nb_rounds = db_tournament[3], description = db_tournament[4])

#Create instance of Player with database
for player in db_players:
    player = Player(firstname = player[0], lastname = player[1], date_of_birth = player[2], sexe = player[3], rank = player[4])
    #Add instance of Player in list of player in tournament
    tournament_testing.players.append(player)
    
#Write in JSON file (tournament informations + players)
with open("db.json", "w", encoding="UTF-8") as jf:
    # json.dump(tournament_testing.__dict__, jf)
    for player in tournament_testing.players:
        json.dump(player.__dict__, jf)
        jf.write('\n')
        
#Sorted list of player by ranking
tournament_testing.sorted_list_of_player_for_round_1()
# tournament_testing.players.sort(key=lambda player: player.rank, reverse=True)

#Create 2 lists of players
list_a =[]
list_a = tournament_testing.players[0:4]
list_b = []
list_b = tournament_testing.players[4:8]

#Create round 
# first_round = []
first_round = Round(name_of_round = "Round_1")

#For loop to create list of match
for i in range(len(list_a)):
    first_round.list_of_match.append(list_a[i])
    first_round.list_of_match.append(list_b[i])
    match = Match(player_1 = list_a[i], player_1_result = 0, player_2 = list_b[i], player_2_result = 0)
    tuple_match = match.get_match_tuple()
    print(f"Match n°", i+1, ":", tuple_match)

for match in tuple_match:
    result_match = input("Qui a gagné le match ? 1 pour : " + str(match.player_1) + "2 pouur : " + str(match.player_2))
    if result_match == 1:
        tuple_match.player_1_result += 1
    elif result_match == 2:
        tuple_match.player_2_result += 1
    
        

# print(tournament_testing.__dict__)
# print(tournament_testing.players)

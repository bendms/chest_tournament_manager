from typing import List


from models.match import Match


class Round:
    def __init__(self, list_of_matches = [], name_of_round= "", date_and_hour_start= "", date_and_hour_end= "", match=None):
        self.match = Match
        self.list_of_matches: List[Match] = []
        self.name_of_round = name_of_round
        self.date_and_hour_start = date_and_hour_start
        self.date_and_hour_end = date_and_hour_end
    
    def create_list_of_matches(self, tournament):
        list_of_players = []
        list_a =[]
        list_a = tournament.players[0:4]
        list_b = []
        list_b = tournament.players[4:8]
        for i in range(len(list_a)):
            list_of_players.append(list_a[i])
            list_of_players.append(list_b[i])
            self.match = Match(player_1 = list_a[i], player_1_result = 0, player_2 = list_b[i], player_2_result = 0)
            self.match.opponents_list_update(player_1 = list_a[i], player_1_result = 0, player_2 = list_b[i], player_2_result = 0)
            self.list_of_matches.append(self.match.get_match_tuple())
        return self.list_of_matches
    
    def update_score(self, user_response, i):
        if user_response == "1" :
            self.list_of_matches[i][0][0].update_score(point = 1)
            self.list_of_matches[i][0][1] += 1
        elif user_response == "2":
            self.match.player_2_result += 1
            self.list_of_matches[i][1][0].update_score(point = 1)
            self.list_of_matches[i][1][1] += 1

        elif user_response == "0":
            self.list_of_matches[i][0][0].update_score(point = 0.5)
            self.list_of_matches[i][0][1] += 0.5
            self.list_of_matches[i][1][0].update_score(point = 0.5)
            self.list_of_matches[i][1][1] += 0.5

        else:
            print("Veuillez entrer 0, 1 ou 2")
        # print(f"\n#### Le match a bien été mis à jour ####\n", self.match, "\n\n")
        print(f"\n#### Le match a bien été mis à jour ####\n", self.list_of_matches[i], "\n\n")
        # print(f"\n#### Le match a bien été mis à jour ####\n", self.list_of_matches[i][0], "\n\n")

              
    def create_list_of_match_for_next_round(self, tournament):
        pass
        
    def show_winners(self):
        pass

    def get_list_of_match(self):
        pass
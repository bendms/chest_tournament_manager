from typing import List


from models.match import Match


class Round:
    def __init__(self, list_of_match = [], name_of_round= "", date_and_hour_start= "", date_and_hour_end= ""):
        # self.list_of_match = List[Match] = []
        self.list_of_match = list_of_match
        self.name_of_round = name_of_round
        self.date_and_hour_start = date_and_hour_start
        self.date_and_hour_end = date_and_hour_end
    
    def create_list_of_match(self, tournament):
        list_of_players = []
        list_a =[]
        list_a = tournament.players[0:4]
        list_b = []
        list_b = tournament.players[4:8]
        for i in range(len(list_a)):
            list_of_players.append(list_a[i])
            list_of_players.append(list_b[i])
            match = Match(player_1 = list_a[i], player_1_result = 0, player_2 = list_b[i], player_2_result = 0)
            self.list_of_match.append(match)
        return self.list_of_match
    
    def show_winners(self):
        pass

    def get_list_of_match(self):
        pass
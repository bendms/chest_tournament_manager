from models.player import Player


class Match:
    def __init__(self, player_1, player_1_result, player_2, player_2_result):
        self.player_1: Player = player_1
        self.player_1_result = player_1_result
        self.player_2: Player = player_2
        self.player_2_result = player_2_result


    def __repr__(self):
        return f"Player 1 : {self.player_1}, Player_1_Score : {self.player_1_result}, Player_2 : {self.player_2}, Player_2_Score : {self.player_2_result}"
       
    
    def get_match_tuple(self):
        match_tuple = ([self.player_1, self.player_1_result], [self.player_2, self.player_2_result])    
        self.player_1.add_opponent(self.player_2.firstname)
        self.player_2.add_opponent(self.player_1.firstname)
        return match_tuple

    # def opponents_list_update(self):
    #     self.player_1.already_faced_players.append(self.player_2)
    #     self.player_2.already_faced_players.append(self.player_1)
        
    # def update_result(self, user_input):
    #     if user_input == 1:
    #         self.player_1_result += 1
    #     elif user_input == 2:
    #         self.player_2_result += 1
    #     else:
    #         self.player_1_result += 0,5
    #         self.player_2_result += 0,5
        
from models.player import Player


class Match:
    def __init__(self, player_1, player_1_result, player_2, player_2_result, match_tuple=""):
        self.player_1 = Player
        self.player_1_result = player_1_result
        self.player_2 = Player
        self.player_2_result = player_2_result
        self.match_tuple = match_tuple

    def __repr__(self):
        # return f"Player 1 : {self.player_1}, Player_1_Score : {self.player_1_result}, Player_2 : {self.player_2}, Player_2_Score : {self.player_2_result}"
        return self.match_tuple
    
    def get_match_tuple(self):
        self.match_tuple = [self.player_1, self.player_1_result], [self.player_2, self.player_2_result]
        return self.match_tuple
    
    # def update_result(self, user_input):
    #     if user_input == 1:
    #         self.player_1_result += 1
    #     elif user_input == 2:
    #         self.player_2_result += 1
    #     else:
    #         self.player_1_result += 0,5
    #         self.player_2_result += 0,5
        
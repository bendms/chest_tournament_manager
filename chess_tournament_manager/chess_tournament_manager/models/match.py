class Match:
    def __init__(self, player_1, player_1_result, player_2, player_2_result):
        self.player_1 = player_1
        self.player_1_result = player_1_result
        self.player_2 = player_2
        self.player_2_result = player_2_result

    def __repr__(self) -> str:
        return f"Player 1 : {self.player_1}, Player_1_Score : {self.player_1_result}, Player_2 : {self.player_2}, Player_2_Score : {self.player_2_result}"

    def get_match_tuple(self):
        match_tuple = [self.player_1, self.player_1_result], [self.player_2, self.player_2_result]
        return match_tuple
    

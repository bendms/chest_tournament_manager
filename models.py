class Tournament():
    def __init__(self, name, location, date, nb_rounds=4, players, time_control, description):
        self.name = name
        self.location = location
        self.date = date
        self.nb_rounds = nb_rounds
        self.players = players
        self.time_control = time_control
        self.description = description
        
    
    def create_new_tournament():
        pass
    
    def add_player():
        pass
    
    def create_pair_of_players():
        """Au début du premier tour, triez tous les joueurs en fonction de leur classement.
Divisez les joueurs en deux moitiés, une supérieure et une inférieure. Le meilleur joueur de la moitié supérieure est jumelé avec le meilleur joueur de la moitié inférieure, et ainsi de suite. Si nous avons huit joueurs triés par rang, alors le joueur 1 est jumelé avec le joueur 5, le joueur 2 est jumelé avec le joueur 6, etc.
Au prochain tour, triez tous les joueurs en fonction de leur nombre total de points. Si plusieurs joueurs ont le même nombre de points, triez-les en fonction de leur rang.
Associez le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4, et ainsi de suite. Si le joueur 1 a déjà joué contre le joueur 2, associez-le plutôt au joueur 3.
Répétez les étapes 3 et 4 jusqu'à ce que le tournoi soit terminé."""
        pass
    

class Round():
    def __init__(self, list_of_match = [], name_of_round, date_and_hour_start, date_and_hour_end):
        self.list_of_match = list_of_match
        self.name_of_round = name_of_round
        self.date_and_hour_start = date_and_hour_start
        self.date_and_hour_end = date_and_hour_end
    
    def create_new_round():
        pass
    
    def show_winners():
        pass

class Match():
    def __init__(self, pair_of_players = []):
        self.pair_of_players = pair_of_players

class Player():
    def __init__(self, lastname, firstname, date_of_birth, sexe, rank):
        self.lastname = lastname
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.sexe = sexe
        self.rank = rank
    

class View:
    pass

class ViewMenu: 
    def __init__(self, player="", user_response=""):
        self.user_response = user_response    
        self.player = player
    
    def display_menu():
        print("Menu : ")
        print("1. Créer un nouveau tournoi")
        print("2. Ajouter des joueurs")
        print("3. Générer un rapport")
            
    
    def get_user_response(self):
        self.user_response = input("Entrez un chiffre pour naviguer dans le menu : ")
        return self.user_response
    
    
    def get_result_for_round(self):
        self.user_response = input("Veuillez indiquer quel joueur a gagné le match. \nTapez 1 pour joueur 1. \nTapez 2 pour joueur 2. \nTapez 0 en cas d'égalité.\n")
        return self.user_response


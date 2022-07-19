class View:
    pass

class ViewMenu: 
    def __init__(self, player="", user_response=""):
        self.user_response = user_response    
        self.player = player
        self.user_response = user_response
    
    def display_menu():
        print("Menu : ")
        print("1. Créer un nouveau tournoi")
        print("2. Ajouter des joueurs")
        print("3. Générer un rapport")
            
    
    def get_user_response(self):
        self.user_response = input("Entrez un chiffre pour naviguer dans le menu : ")
        return self.user_response
            

    


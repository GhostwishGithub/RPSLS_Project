class Game():
    def __init__(self):
        pass
    def the_welcome(self):
        print("Welcome to the game!")
        print("""
        The rules are 'simple'
        Rock crushes Scissors
        Scissors cuts Paper 
        Paper covers Rock
        Rock crushes Lizard
        Lizard poisons Spock
        Spock smashes Scissors
        Scissors decapitates Lizard
        Lizard eats Paper
        Paper disproves Spock
        Spock vaporizes Rock
        Got it? Good.
        """)

    def run_game(self, round):
        round = 0
        user_choice = input("Would you like to play against the AI? y/n:")
        if user_choice == 'y':
            pass #this is where it will go into singleplayer
        elif user_choice == 'n':
            pass #this is where it will go into multiplayer
        else:
            print("Uh, care to try again?")
            #maybe loop back into the greeting from here?
        



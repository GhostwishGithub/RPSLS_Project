class Game():
    def __init__(self, gestures):
        gestures = gestures['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

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



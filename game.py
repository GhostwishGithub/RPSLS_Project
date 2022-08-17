from human import Human
from ai import AI

class Game:
    def __init__(self):
        self.player_one = Human('')
        self.player_two = Human('')
        self.player_three = AI()
        self.wins = 0

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

    def run_game(self):
        print(self.the_welcome)
        user_choice = input("Would you like to play against the AI? y/n:")
        if user_choice == 'y':
            self.player_two = self.player_three
            self.player_one.enter_name()
        elif user_choice == 'n':
            print("Okay! Two player it is!")
            self.player_one.enter_name()
            self.player_two.enter_name()
        else:
            print("Uh, care to try again?")
            self.run_game
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()
        while self.player_one.wins <= 2 and self.player_two.wins <= 2:
            self.battle_phase() #We are right here! Breaking for break time. Need to come up with a way to record wins inside of battle_phase. 
        #Maybe define it as Game variable?
        self.display_winner()
        

    def display_winner(self):
        if (self.player_one.player_one == 2):
            print(f'{self.player_one.name} wins the game!')
        elif (self.player_two.player_two == 2):
            print(f'{self.player_two.name} wins the game!')
        
    def battle_phase(self):
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print("Son of a sock, it's a tie!")
        if self.player_one.chosen_gesture == 'rock':
            if self.player_two.chosen_gesture == 'paper':
                print("Paper beats rock! Player 2 wins!")
                #count up player 2's wins
                self.wins.player_two += 1
            elif self.player_two.chosen_gesture == 'lizard':
                print("Rock crushes lizard! Player 1 wins!")
                #count up player 1's wins
                self.wins.player_one += 1
            elif self.player_two.chosen_gesture == 'spock':
                print("Spock vaporizes rock! Player 2 wins!")
                #count up player 2's wins
                self.wins.player_two += 1
        if self.player_one.chosen_gesture == 'scissors':
            if self.player_two.chosen_gesture == 'paper':
                print("Scissors cut paper! Player 1 wins!")
                #count up player 1's wins
                self.wins.player_one += 1
            elif self.player_two.chosen_gesture == 'lizard':
                print("Scissors decapitates lizard! Player 1 wins!")
                #count up player 1's wins
                self.wins.player_one += 1
            elif self.player_two.chosen_gesture == 'spock':
                print("Spock SNASH scissors! Player 2 wins!")
                #count up player 2's wins
                self.wins.player_two += 1
            elif self.player_two.chosen_gesture == 'rock':
                print("Rock SMASH scissors! Player 2 wins!")
                #count up player 2's wins
                self.wins.player_two += 1
        if self.player_one.chosen_gesture == 'paper':
            if self.player_two.chosen_gesture == 'scissors':
                print("Scissors cut paper! Player 2 wins!")
                #count up player 2's wins
                self.wins.player_two += 1
            elif self.player_two.chosen_gesture == 'lizard':
                print("Lizard eats paper! Burp! Player 2 wins!")
                #count up player 2's wins
                self.wins.player_two += 1
            elif self.player_two.chosen_gesture == 'spock':
                print("Paper disproves Spock! Take that nerd! Player 1 wins!")
                #count up player 1's wins
                self.wins.player_one += 1
            elif self.player_two.chosen_gesture == 'rock':
                print("Paper covers Rock! Player 1 wins!")
                #count up player 1's wins
                self.wins.player_one += 1
        if self.player_one.chosen_gesture == 'lizard':
            if self.player_two.chosen_gesture == 'scissors':
                print("Scissors decapitate lizard! Player 2 wins!")
                #count up player 2's wins
                self.wins.player_two += 1
            elif self.player_two.chosen_gesture == 'paper':
                print("Lizard eats paper! Burp! Player 1 wins!")
                #count up player 1's wins
                self.wins.player_one += 1
            elif self.player_two.chosen_gesture == 'spock':
                print("Lizard poisons Spock! Player 1 wins!")
                #count up player 1's wins
                self.wins.player_one += 1
            elif self.player_two.chosen_gesture == 'rock':
                print("Rock crushes lizard! Player 2 wins!")
                #count up player 2's wins
                self.wins.player_two += 1
        if self.player_one.chosen_gesture == 'Spock':
            if self.player_two.chosen_gesture == 'scissors':
                print("Spock SNASH scissors! Player 1 wins!")
                #count up player 1's wins
                self.wins.player_one += 1
            elif self.player_two.chosen_gesture == 'paper':
                print("Paper disproves Spock! Take that nerd! Player 2 wins!")
                #count up player 2's wins
                self.wins.player_two += 1
            elif self.player_two.chosen_gesture == 'lizard':
                print("Lizard poisons Spock! Player 2 wins!")
                #count up player 2's wins
                self.wins.player_two += 1
            elif self.player_two.chosen_gesture == 'rock':
                print("Spock vaporizes Rock! Player 1 wins!")
                #count up player 1's wins
                self.wins.player_one += 1
        
        

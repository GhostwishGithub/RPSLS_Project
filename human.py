from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def enter_name(self):
        self.name = input("Please enter your name!")

    def choose_gesture(self):
        self.choose_gesture = self.gestures[0:4]
        user_input = input("pick a gesture: rock, paper, scissors, lizard, spock. Case sensitive! No bananas! ")
        
        if user_input == self.gestures[0]:
            print('You picked rock!')
            self.chosen_gesture = self.gestures[0]
       
        elif user_input == self.gestures[1]:
            print('You chose paper!')
            self.choose_gesture = self.gestures[1]
        
        elif user_input == self.gestures[2]:
            print('You chose scissors!')
            self.choose_gesture = self.gestures[2]
       
        elif user_input == self.gestures[3]:
            print('You chose lizard!')
            self.chosen_gesture = self.gestures[3]
       
        elif user_input== self.gestures[4]:
            print('You chose spock!')
            self.chosen_gesture = self.gestures[4]
        
        else:
            print('not a valid option')
            self.choose_gesture()
from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = input('please enter your name ')

    def choose_gesture(self):
        self.choose_gesture = self.gesture[0:4]
        user_input = input('pick a gesture ')
        
        if user_input == self.gesture[0]:
            print('You picked rock!')
            self.chosen_gesture = self.gesture[0]
       
        elif user_input == self.gesture[1]:
            print('You chose paper!')
            self.choose_gesture = self.gesture[1]
        
        elif user_input == self.gesture[2]:
            print('You chose scissors!')
            self.choose_gesture = self.gesture[2]
       
        elif user_input == self.gesture[3]:
            print('You chose lizard!')
            self.chosen_gesture = self.gesture[3]
       
        elif user_input== self.gesture[4]:
            print('You chose spock!')
            self.chosen_gesture = self.gesture[4]
        
        else:
            print('not a valid option')
from player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gestures)
        print(f"The Killatron 9000 has chosen {self.chosen_gesture}!!")
        return self.chosen_gesture
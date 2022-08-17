from gesture import Gesture

class Player(Gesture):
    
    def __init__(self):
        super().__init__()
        self.wins = 0
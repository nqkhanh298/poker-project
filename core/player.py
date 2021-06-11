from random import sample
from core.card import Card

# chip = Chip()
card = Card()

class Player:
    stt = 0    
    def __init__(self):
        self.id = Player.stt
        self.player_card = []
        self.player_chip = 4000
        self.score = 0
        Player.stt +=1

        
    def bet(self, number, board):
        self.player_chip -= number
        board.chip_on_table += number

    def check():
        pass

    def fold(self, board):
        board.player_on_table.remove(self)
        
    

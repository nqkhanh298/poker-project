from core.card import Card
from core.board import Board

# chip = Chip()
card = Card()
board = Board()

class Player:
    stt = 0    
    def __init__(self):
        self.id = Player.stt
        self.player_card = []
        self.player_chip = 4000
        self.score = 0
        Player.stt +=1
    
    def get_player(self):
        player_data = {
            'id': self.id,
            'player_card': self.player_card,
            'player_chip': self.player_chip,
            'score': self.score,
        }
        return player_data
    
    def set_card(self, card):
        self.player_card = card

    def set_chip(self, chip):
        self.player_chip = chip
    
    def set_card(self, card):
        self.card = card

    def bet(self, number):
        self.player_chip -= number
        board.set_chip(number)

    def check():
        pass

    def fold(self):
        board.eliminate_player(self)
        
    

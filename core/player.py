from random import sample
from core.card import Card

# chip = Chip()
card = Card()

class Player:
    player_card = []
    player_chip = 0
    score = 0

    @staticmethod
    def bet(player, number, board):
        player.player_chip -= number
        board.chip_on_table += number

    @staticmethod
    def check():
        pass

    @staticmethod
    def fold(player, board):
        board.player_on_table.remove(player)
        
    

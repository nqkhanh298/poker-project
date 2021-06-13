import sys
from core import player
sys.path.append("..") # Adds higher directory to python modules path.
from core.player import Player

player_1 = Player('Khanh')

def action(board):
    return player1_action(player_1, board)

def player1_action(player_1, board):
    player_1.bet(1000, board)
import sys
from core import player
sys.path.append("..") # Adds higher directory to python modules path.
from core.player import Player

player_2 = Player('Vang')

def action(board):
    return player2_action(player_2, board)

def player2_action(player_2, board):
    player_2.bet(1000, board)
import sys
from core import player
sys.path.append("..") # Adds higher directory to python modules path.
from core.player import Player
player_1 = Player("Khanh")

def action(board):
    return player1_action(board)

def player1_action(board):
    return player_1.bet(500,board)

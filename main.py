# from basic import all_players_action
from core.player import Player
from core.board import Board
from core.card import Card
from player import player1 as p1
from player import player2 as p2
from random import randint
import math

card = Card()
board = Board()

def turn(button):
    i = button
    t = True
    while (i - button) < button or board.player_on_table[(i+1) % len(board.player_on_table)].checkData():
        i += 1
        if board.player_on_table[i % len(board.player_on_table)].id == 0:
            print("1")
            p1.action(board)
        elif board.player_on_table[i % len(board.player_on_table)].id == 1:
            print("2")
            p2.action(board)
    # print("Player:", Player.chip_basic)
    Player.reset(board.player_on_table)
    # print("Player:", Player.chip_basic)


def chiabai(number):
    board.deal_card(number, card)
    board.show_board()
    board.set_score_all_players(card)
board.player_on_table = [p1.player_1, p2.player_2]

# Start game
print("""
--------------------------------
Welcome to Poker Game !
Let's get started ...
--------------------------------
Here is all of your cards: 
""")

round = 1
button_position = randint(0, len(board.player_on_table) - 1)
while True:
    # Start game
    print('Round:', round)
    board.init_board(card, [p1.player_1, p2.player_2], button_position)
    for p in board.player_on_table:
        if p.player_chip > 0:
            p.set_card(card.get_card())
        else:
            board.player_on_table.remove(p)

    if (len(board.player_on_table) > 1):
        for i in range(len(board.player_on_table)):
            print("Player", i + 1, ":", *board.player_on_table[i].player_card, '-', board.player_on_table[i].player_chip)

        # Pre flop
        turn(button_position+len(board.player_on_table))
        # Flop
        chiabai(3)
        turn(button_position)
        # Turn
        chiabai(1)
        turn(button_position)
        # River
        chiabai(1)
        turn(button_position)
                
        winner = []
        winner.append(board.player_on_table[0])
        max_score = board.player_on_table[0].score
        for p in board.player_on_table:
            if p.score > max_score:
                winner.clear()
                winner.append(p)
                max_score = p.score
            elif p.score == max_score:
                winner.append(p)
        for p in winner:
            p.player_chip += math.floor(board.chip_on_table / len(winner))
        round += 1
        if button_position == (len(board.player_on_table) - 1):
            button_position = 0
        else:
            button_position += 1
    else:
        break

print(board.player_on_table[0].name, 'is the winner')

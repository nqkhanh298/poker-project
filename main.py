# from basic import all_players_action
from core.board import Board
from core.card import Card
from player import player1 as p1
from player import player2 as p2
from random import randint
import math

# player_number = int(input("Enter number of players: "))
# chip_total = int(input("Enter amount of chips: "))

card = Card()
board = Board()

player_1 = p1.player_1
player_2 = p2.player_2

board.player_on_table = [player_1, player_2]

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
    board.init_board(card, [player_1, player_2], button_position)
    for p in board.player_on_table:
        if p.player_chip > 0:
            p.set_card(card.get_card())
        else:
            board.player_on_table.remove(p)

    if (len(board.player_on_table) > 1):
        for i in range(len(board.player_on_table)):
            print("Player", i + 1, ":", *board.player_on_table[i].player_card, '-', board.player_on_table[i].player_chip)

        print("--------------------------------")
        # Pre flop
        board.show_board()
        board.set_score_all_players(card)
        p1.action(board)
        p2.action(board)
        print("--------------------------------")
        # Flop
        board.deal_card(3, card)
        board.show_board()
        board.set_score_all_players(card)
        print("--------------------------------")
        # Turn
        board.deal_card(1, card)
        board.show_board()
        board.set_score_all_players(card)
        print("--------------------------------")
        # River
        board.deal_card(1, card)
        board.show_board()
        board.set_score_all_players(card)
        print("--------------------------------")
        
        # Check winner
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

from core.board import Board
from core.card import Card
from core.player import Player
from player.player1 import Player1 as p1
from player.player2 import Player2 as p2

# player_number = int(input("Enter number of players: "))
# chip_total = int(input("Enter amount of chips: "))

card = Card()
board = Board(2, 1000)
player = Player()
# chip = Chip()

card.generate_card()
board.get_list_player_card(2)
board.player_on_table

p1.player_card = board.list_player_card[0]
p2.player_card = board.list_player_card[1]
p1.player_chip = 1000 / 2
p2.player_chip = 1000 / 2

# Start game
print("""
--------------------------------
Welcome to Poker Game !
Let's get started ...
--------------------------------
Here is all of your cards: 
""")

# Deal card to players
for i in range(2):
    print("Player", i + 1, ":", *board.list_player_card[i])

# Show cards on table
print("--------------------------------")
# Pre flop
print("Actions: ")
board.set_score(p1)
board.set_score(p2)
print(p1.score)
print(p2.score)
print("p1 chip:", p1.player_chip)
p1.bet(p1, 300, board)
print("chip on table: ", board.chip_on_table)
print("p1 chip:", p1.player_chip)
print("--------------------------------")
# Flop
board.deal_card(3)
print("Actions: ")
board.set_score(p1)
board.set_score(p2)
print(p1.score)
print(p2.score)
print("--------------------------------")
# Turn
board.deal_card(1)
print("Actions: ")
board.set_score(p1)
board.set_score(p2)
print(p1.score)
print(p2.score)
print("--------------------------------")
# River
board.deal_card(1)
print("Actions: ")
board.set_score(p1)
board.set_score(p2)
print(p1.score)
print(p2.score)

print("--------------------------------")



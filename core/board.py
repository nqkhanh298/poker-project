from core.card import Card
from random import sample

card = Card()

class Board:
    card_on_table = []
    list_player_chip = []

    def __init__(self):
        self.chip_on_table = 0
        self.player_on_table = []

    def deal_card(self, number):
        new_card = sample(card.card_deck, number)
        for item in new_card:
            self.card_on_table.append(item)
            card.card_deck.remove(item)
        print("Board:", *self.card_on_table)

    def set_score(self, player):
        player.score = 0
        total_card = player.player_card + self.card_on_table
        if card.check_straight_flush(total_card): player.score = card.check_straight_flush(total_card)
        elif card.check_quad(total_card): player.score = card.check_quad(total_card)
        elif card.check_full_house(total_card): player.score = card.check_full_house(total_card)
        elif card.check_flush(total_card): player.score = card.check_flush(total_card)
        elif card.check_straight(total_card): player.score = card.check_straight(total_card)
        elif card.check_set(total_card): player.score = card.check_set(total_card)
        elif card.check_two_pair(total_card): player.score = card.check_two_pair(total_card)
        elif card.check_pair(total_card): player.score = card.check_pair(total_card)
        else: player.score = card.check_high_card(total_card)
    
    def set_chip(self, chip):
        self.chip_on_table += chip
    
    def eliminate_player(self, player):
        self.player_on_table.remove(player)

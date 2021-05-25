from core.card import Card
from random import sample

card = Card()


class Board:
    card_on_table = []
    player_on_table = []
    chip_on_table = 0
    list_player_card = []
    list_player_chip = []

    def __init__(self, chip_total, player_number):
        self.chip_total = chip_total
        self.player_number = player_number

    def get_list_player_card(self, player_number):
        for _ in range(player_number):
            player_card = sample(card.card_deck, 2)
            self.list_player_card.append(player_card)
            for item in player_card:
                card.card_deck.remove(item)

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

from random import sample, randint

class Board:
    card_on_table = []
    list_player_chip = []

    def __init__(self):
        self.chip_on_table = 0
        self.player_on_table = []
        self.blind = 10

    def init_board(self, card, list_player, temp):
        self.chip_on_table = 0
        self.card_on_table = []
        self.player_on_table = list_player
        self.set_blind(list_player, temp)
        for p in list_player:
            p.stt = ''
        card.card_deck = []
        for i in range(1, 14):
            for j in card.list_suit:
                c = str(i) + j
                card.card_deck.append(c)

    def set_blind(self, list_player, temp):
        if temp < (len(list_player) - 2):
            list_player[temp + 1].player_chip -= self.blind
            list_player[temp + 2].player_chip -= (self.blind * 2)
        elif temp == (len(list_player) - 2):
            list_player[temp + 1].player_chip -= self.blind
            list_player[0].player_chip -= (self.blind * 2)
        elif temp == (len(list_player) - 1):
            list_player[0].player_chip -= self.blind
            list_player[1].player_chip -= (self.blind * 2) 

    def deal_card(self, number, card):
        new_card = sample(card.card_deck, number)
        for item in new_card:
            self.card_on_table.append(item)
            card.card_deck.remove(item)
    
    def show_board(self):
        print("Board:", *self.card_on_table)
        print("Pot:", self.chip_on_table)

    def set_score_all_players(self, card):
        for p in self.player_on_table:
            self.set_score(p, card)
            print('score:', p.score)

    def set_score(self, player, card):
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
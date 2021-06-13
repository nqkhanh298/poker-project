class Player:
    def __init__(self, name):
        self.name = name
        self.player_card = []
        self.player_chip = 4000
        self.score = 0
        self.stt = ''
        self.rules = {
            'canCall': True,
            'canCheck': True,
            'canBet': True
        }

    def set_card(self, card):
        self.player_card = card

    def set_chip(self, chip):
        self.player_chip += chip

    def bet(self, number, board):
        if self.rules['canBet']:
            self.set_chip(-number)
            self.stt = 'bet'
            board.set_chip(number)

    def check(self):
        if self.rules['canCheck']:
            self.stt = 'check'
            pass

    def fold(self, board):
        self.stt = 'fold'
        board.eliminate_player(self)        
    

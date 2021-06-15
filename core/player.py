import player


class Player:
    chip_basic = 0
    index = 0
    def __init__(self, name):
        self.name = name
        self.player_card = []
        self.player_chip = 4000
        self.chip_basic_mine = 0
        self.score = 0
        self.stt = ''
        self.id = Player.index
        Player.index+=1

    def checkData(self):
        return self.chip_basic_mine != Player.chip_basic

    def set_card(self, card):
        self.player_card = card

    def set_chip(self, chip):
        self.player_chip += chip

    def call(self,board):
        if self.checkCall():
            self.set_chip(-1*Player.chip_basic)
            self.chip_basic_mine = Player.chip_basic
            board.set_chip(Player.chip_basic)
            self.stt = 'call'
            print("chip sau call ca nhan: ", self.chip_basic_mine)

    def checkCall(self):
        if self.chip_basic_mine > Player.chip_basic:
            return False
        if self.player_chip < Player.chip_basic:
            return False
        return True

    def bet(self, number, board):
        if self.checkBet(number,board):
            self.set_chip(-number)
            self.chip_basic_mine = number
            self.stt = 'bet'
            board.set_chip(number)
            Player.chip_basic = number
    
    def checkBet(self,number,board):
        if number < 2*Player.chip_basic:
            return False
        if number < board.blind:
            return False
        if number > self.player_chip:
            return False
        return True

    def check(self):
        if self.checkCheck():
            self.stt = 'check'
            pass
    def checkCheck(self):
        if self.chip_basic_mine < Player.chip_basic:
            return False
        return True

    def fold(self, board):
        self.chip_basic = 0
        self.stt = 'fold'
        board.eliminate_player(self)  

    @staticmethod
    def reset(arr):
        Player.chip_basic = 0
        for i in arr:
            i.chip_basic_mine = 0

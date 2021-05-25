class Chip:
    chip_on_table = 0

    def __init__(self):
        self.chip_amount = 0
        self.list_chip_player = []

    def get_list_player_chip(self, player_number, chip_amount):
        self.chip_amount = chip_amount
        for i in range(player_number):
            self.list_chip_player.append(round(self.chip_amount/player_number))
    
    def show_pot(self):
        print("Pot:", self.chip_on_table)
    
    @classmethod
    def set_chip_on_table(cls, chip):
        cls.chip_on_table += chip
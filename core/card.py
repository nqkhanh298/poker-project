import basic as b

class Card():
    card_deck = []
    list_suit = ['H', 'D', 'S', 'C']  # H:Heart, D:Diamond, S:Spade, C:Club

    def generate_card(self):
        for i in range(1, 14):
            for j in self.list_suit:
                card = str(i) + j
                self.card_deck.append(card)

    @staticmethod
    def check_high_card(list_card):
        temp = b.get_list_card_number(list_card)
        for i in range(len(temp)):
            temp[i] = int(temp[i])
        if (temp.count(1) == 1): 
            return 13
        return int(max(temp)) - 1

    @staticmethod
    def check_pair(list_card):
        temp = b.get_list_card_number(list_card)
        list_number =  b.get_list_number(temp)
        if(list_number.count(2) == 2):
            for number in temp:
                if(temp.count(number) == 2):
                    if(int(number) == 1): 
                        return 26
                    else: 
                        return (int(number) + 12)
        return 0

    @staticmethod
    def check_two_pair(list_card):
        temp = b.get_list_card_number(list_card)
        list_number =  b.get_list_number(temp)
        list_score = []
        if(list_number.count(2) >= 4):
            for number in temp:
                if(temp.count(number) == 2):
                    if(int(number) == 1): 
                        list_score.append(39)
                    else: list_score.append(int(number) + 25)
        if(list_score): 
            return max(list_score)
        return 0
    
    @staticmethod
    def check_set(list_card):
        temp = b.get_list_card_number(list_card)
        list_number =  b.get_list_number(temp)
        if(list_number.count(3) == 3 and list_number.count(2) == 0):
            for number in temp:
                if(temp.count(number) == 3):
                    if(int(number) == 1): 
                        return 52
                    else: 
                        return (int(number) + 38)
        return 0

    @staticmethod
    def check_quad(list_card):
        temp = b.get_list_card_number(list_card)
        list_number =  b.get_list_number(temp)
        if(list_number.count(4) == 4):
            for number in temp:
                if(temp.count(number) == 4):
                    if(int(number) == 1): 
                        return 102
                    else: 
                        return (int(number) + 88)
        return 0
    
    @staticmethod
    def check_full_house(list_card):
        temp = b.get_list_card_number(list_card)
        list_number =  b.get_list_number(temp)
        if(list_number.count(3) == 3 and list_number.count(2) == 2):
            for number in temp:
                if(temp.count(number) == 3):
                    if(int(number) == 1): 
                        return 89
                    else: 
                        return (int(number) + 75)
        return 0
    
    @staticmethod
    def check_flush(list_card):
        temp1 = b.get_list_card_suit(list_card)
        temp2 = b.get_list_card_number(list_card)
        list_score = []
        for suit in ['H', 'D', 'S', 'C']:
            if (temp1.count(suit) >= 5):
                for i in range(len(list_card)):
                    if list_card[i][-1] == suit:
                        if temp2[i] == 1: list_score.append(76)
                        else: list_score.append(int(temp2[i]) + 62)
        if(list_score):
            return max(list_score)
        return 0

    @staticmethod
    def check_straight(list_card):
        temp = b.get_list_card_number(list_card)
        for i in range(len(temp)):
            temp[i] = int(temp[i])
        list_sorted = sorted(temp)
        if(len(list_sorted) >= 5):
            for i in range(len(list_sorted) - 4):
                if(list_sorted[i] == list_sorted[i + 4] - 4):
                    return list_sorted[i] + 52
                elif (list_sorted[0]== list_sorted[i + 1] - 9 == list_sorted[i + 4] - 12):
                    return 63
        return 0
    
    @staticmethod
    def check_straight_flush(list_card):
        temp1 = b.get_list_card_suit(list_card)
        temp = b.get_list_card_number(list_card)
        for suit in ['H', 'D', 'S', 'C']:
            if (temp1.count(suit) >= 5):
                for i in range(len(temp)):
                    temp[i] = int(temp[i])
                list_sorted = sorted(temp)
                if(len(list_sorted) >= 5):
                    for i in range(len(list_sorted) - 4):
                        if(list_sorted[i] == list_sorted[i + 4] - 4):
                            return list_sorted[i] + 102
                        elif (list_sorted[0]== list_sorted[i + 1] - 9 == list_sorted[i + 4] - 12):
                            return 113
        return 0


    
   
    

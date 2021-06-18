import basic as b
from random import sample

class Card():
    card_deck = []
    list_suit = ['H', 'D', 'S', 'C']  # H:Heart, D:Diamond, S:Spade, C:Club

    def get_card(self):
        player_card = sample(self.card_deck, 2)
        for item in player_card:
            self.card_deck.remove(item)
        return player_card

    def check_high_card(self, list_card, j=5):
        score = 0
        temp = b.get_list_card_number(list_card)
        temp = sorted(temp, reverse=True)
        if(temp.count(1) == 1):
            score += 14
            for i in range(4):
                temp[i] = int(temp[i])
                score += temp[i]
        else:
            for i in range(j):
                temp[i] = int(temp[i])
                score += temp[i]
        return score

    def check_pair(self, list_card):
        score = 0
        c = 2
        list_index = []
        temp = b.get_list_card_number(list_card)
        list_number =  b.get_list_number(temp)
        if(list_number.count(2) == 2):
            for i in range(len(temp)):
                if(temp.count(temp[i]) == 2):
                    if(int(temp[i]) == 1): 
                        score += 88
                    else: 
                        score += (c*(int(temp[i]) +28))
                    list_index.append(list_card[i])
            for index in list_index:
                list_card.remove(index)
            if (len(list_card) > 2):
                score += self.check_high_card(list_card, len(list_card) - 2)
        print('pair score:', score)
        return score

    def check_two_pair(self, list_card):
        score = 0
        c = 3
        temp = b.get_list_card_number(list_card)
        list_number =  b.get_list_number(temp)
        list_index = []
        if(list_number.count(2) >= 4):
            for i in range(len(temp)):
                number = temp[i]
                if(temp.count(number) == 2):
                    if(int(number) == 1): 
                        score += 161
                    else:
                        score += (c*(int(number)+40)-1)
                    list_index.append(list_card[i])
            for index in list_index:
                list_card.remove(index)
            if (len(list_card) > 4):
                score += self.check_high_card(list_card, len(list_card) - 4)
        return score
    
    def check_set(self, list_card):
        temp = b.get_list_card_number(list_card)
        list_number =  b.get_list_number(temp)
        list_index = []
        score = 0
        c = 4
        if(list_number.count(3) == 3 and list_number.count(2) == 0):
            for i in range(len(temp)):
                number = temp[i]
                if(temp.count(number) == 3):
                    if(int(number) == 1): 
                        score += 380
                    else: 
                        score += (c*(int(number)+81))
                list_index.append(list_card[i])
            for index in list_index:
                list_card.remove(index)
            if (len(list_card) > 2):
                score += self.check_high_card(list_card, len(list_card) - 2)
        return score

    def check_quad(self, list_card):
        temp = b.get_list_card_number(list_card)
        list_number =  b.get_list_number(temp)
        score = 0
        c = 7
        list_index = []
        if(list_number.count(4) == 4):
            for i in range(len(temp)):
                number = temp[i]
                if(temp.count(number) == 4):
                    if(int(number) == 1): 
                        score += 2214
                    else: 
                        score += (c*(int(number)+302)+2)
                list_index.append(list_card[i])
            for index in list_index:
                list_card.remove(index)
            if (len(list_card) > 1):
                score += self.check_high_card(list_card, len(list_card) - 1)
        return score
    
    def check_full_house(self, list_card):
        temp = b.get_list_card_number(list_card)
        list_number =  b.get_list_number(temp)
        score = 0
        c = 15
        if(list_number.count(3) == 3 and list_number.count(2) == 2):
            for number in temp:
                if(temp.count(number) == 3):
                    if(int(number) == 1): 
                        score += 2310
                    else: 
                        score += ((int(number) + 140) * c)
                if(temp.count(number) == 2):
                    if(int(number) == 1): 
                        score += 14
                    else: 
                        score += int(number)
        return score
    
    def check_flush(self, list_card):
        temp1 = b.get_list_card_suit(list_card)
        temp2 = b.get_list_card_number(list_card)
        list_remove = []
        score = 0
        c = 6
        for suit in ['H', 'D', 'S', 'C']:
            if (temp1.count(suit) >= 5):
                for i in range(len(temp1)):
                    if (temp1[i] != suit):
                        index = temp2[i]
                        list_remove.append(index)
                for item in list_remove:
                    temp2.remove(item)
                temp2 = sorted(temp2, reverse=True)
                if(temp2.count(1) == 1):
                    score += 539
                    for i in range(4):
                        temp2[i] = int(temp2[i])
                        score += ((temp2[i]+76)*6 -1)
                else:
                    for i in range(5):
                        temp2[i] = int(temp2[i])
                        score += ((temp2[i]+76)*6 -1)
        return score

    def check_straight(self, list_card):
        score = 0
        c = 5
        temp = b.get_list_card_number(list_card)
        for i in range(len(temp)):
            temp[i] = int(temp[i])
        list_sorted = sorted(temp)
        if(len(list_sorted) >= 5):
            for i in range(len(list_sorted) - 4):
                if(list_sorted[i] == list_sorted[i + 4] - 4):
                    score += (c*(list_sorted[i] + 79) + 1)
                elif (list_sorted[0]== list_sorted[i + 1] - 9 == list_sorted[i + 4] - 12):
                    score += 446
        return score
    
    def check_straight_flush(self, list_card):
        temp1 = b.get_list_card_suit(list_card)
        temp = b.get_list_card_number(list_card)
        score = 0
        c = 9
        for suit in ['H', 'D', 'S', 'C']:
            if (temp1.count(suit) >= 5):
                for i in range(len(temp)):
                    temp[i] = int(temp[i])
                list_sorted = sorted(temp)
                if(len(list_sorted) >= 5):
                    for i in range(len(list_sorted) - 4):
                        if(list_sorted[i] == list_sorted[i + 4] - 4):
                            score += (c*(list_sorted[i] + 268) + 4)
                        elif (list_sorted[0]== list_sorted[i + 1] - 9 == list_sorted[i + 4] - 12):
                            score += 2506
        return score


    
   
    

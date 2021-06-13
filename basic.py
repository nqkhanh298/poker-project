def get_list_card_number(list_card):
    temp = []
    for card in list_card:
        temp.append(card[:-1])
    return temp

def get_list_card_suit(list_card):
    temp = []
    for card in list_card:
        temp.append(card[-1])
    return temp

def get_list_number(list):
    temp = []
    for number in list:
        temp.append(list.count(number))
    return temp

import copy
import random

card_order = {1: "clovers", 2: "spades", 3: "hearts", 4: "diamonds"}
cards_list = {"clovers": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
              "hearts": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
              "diamonds": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
              "spades": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]}
player_cards = [[], []]
dealer_cards = [[], []]


def copy_shuffle_cards():
    # copy original card list
    cards_copy = copy.deepcopy(cards_list)
    # shuffle copy
    for key in card_order:
        symbol = card_order[key]
        random.shuffle(cards_copy[symbol])
    return cards_copy


def draw_cards(hand, draws):
    for index in range(0, draws):
        symbol = str(card_order[random.randint(1, 4)])
        hand[0].append(game_cards[symbol].pop())
        hand[1].append(symbol[0].upper())


# print card total value
def display_cards_value(hand, hid_dealer_card):
    value = 0
    for card in hand[0]:
        if isinstance(card, str):
            value += 10
        else:
            value += int(card)
        if hid_dealer_card:
            break
    #     if value is 9 or lower add a space to center number
    print(f"       {value if value >= 10 else f' {value}'}")


# print cards
def display_cards(hand, hid_dealer_card=False):
    card_rows = 5
    number_of_cards = 1
    if not hid_dealer_card:
        number_of_cards = len(hand[0])
    for row in range(card_rows):
        display = ""
        for card_num in range(number_of_cards):
            if row == 1:
                display += f"|{hand[0][card_num]}     | "
            elif row == 2:
                display += f"|{hand[1][card_num]}    {hand[1][card_num]}| "
            elif row == 3:
                display += f"|     {hand[0][card_num]}| "
            else:
                display += "-------- "
        print(display)
    display_cards_value(hand, hid_dealer_card)


game_cards = copy_shuffle_cards()
draw_cards(player_cards, 2)
display_cards(player_cards)
draw_cards(dealer_cards, 2)
display_cards(dealer_cards, True)
# display_cards(dealer_cards)
draw_cards(player_cards, 1)
display_cards(player_cards)

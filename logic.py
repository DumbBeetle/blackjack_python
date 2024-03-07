import copy
import random
from constants import (CARD_ROWS, CARDS_LIST, CARDS_SYMBOLS, )

deck = {}
money = 500
dealer_hand = {
    "values": [[]],
    "symbols": [[]],
}
user_hand = {
    "values": [[]],
    "symbols": [[]],
}
number_of_hands = 1
user_current_hand_index = 0


def set_default_values():
    global deck
    global dealer_hand
    global user_hand
    global number_of_hands
    global user_current_hand_index

    deck = copy.deepcopy(CARDS_LIST)
    dealer_hand = {
        "values": [[]],
        "symbols": [[]],
    }
    user_hand = {
        "values": [[]],
        "symbols": [[]],
    }
    number_of_hands = 1
    user_current_hand_index = 0


def get_players():
    global user_hand
    global dealer_hand
    return user_hand, dealer_hand


def shuffle_deck():
    global deck
    for key in CARDS_SYMBOLS:
        symbol = CARDS_SYMBOLS[key]
        random.shuffle(deck[symbol])


def add_hand():
    global user_hand
    user_hand["values"].append([])
    user_hand["symbols"].append([])


def draw_card(player_hand, hand_index=0):
    symbol = str(CARDS_SYMBOLS[random.randint(1, 4)])
    value = deck[symbol].pop()
    player_hand["values"][hand_index].append(value)
    player_hand["symbols"][hand_index].append(symbol[0].upper())


def split_hand(hand_index):
    global number_of_hands

    number_of_hands += 1
    add_hand()
    value = user_hand["values"][hand_index].pop()
    symbol = user_hand["symbols"][hand_index].pop()
    user_hand["values"][-1].append(value)
    user_hand["symbols"][-1].append(symbol)


def first_draw():
    draw_card(user_hand)
    draw_card(dealer_hand)
    draw_card(user_hand)
    draw_card(dealer_hand)


def get_hand_value(player_cards, number_of_cards):
    value = 0
    spaces = ""
    has_ace = False
    for card in range(number_of_cards):
        spaces += "    "
        if isinstance(player_cards[card], str):
            if player_cards[card] == "A":
                value += 11
                has_ace = True
            else:
                value += 10
        else:
            value += int(player_cards[card])
    if has_ace and value > 21:
        value -= 10
    if value > 21:
        value = "Bust"
    return spaces, value


def display_hand(player, hide_dealers_hand, hand_index=0, ):
    cards_to_display = 1
    if not hide_dealers_hand:
        cards_to_display = len(player["values"][hand_index])

    cards = player["values"][hand_index]
    symbols = player["symbols"][hand_index]
    for row in range(CARD_ROWS):
        display = ""
        for card_index in range(cards_to_display):
            card_value = cards[card_index]
            card_symbol = symbols[card_index]
            if row == 1:
                display += f"|{card_value if card_value == 10 else f'{card_value} '}    | "
            elif row == 2:
                display += f"|{card_symbol}    {card_symbol}| "
            elif row == 3:
                display += f"|    {card_value if card_value == 10 else f' {card_value}'}| "
            else:
                display += "-------- "
        print(display)

    spaces, value = get_hand_value(cards, cards_to_display)
    print(f"{spaces}{value}")


def display_players(hide_dealers_hand=False):
    print("Dealer")
    display_hand(dealer_hand, hide_dealers_hand, 0)
    print("Player")
    for hand_index in range(number_of_hands):
        display_hand(user_hand, False, hand_index)


def player_choice():
    global number_of_hands
    global user_current_hand_index
    while user_current_hand_index < number_of_hands:
        cards_number = len(user_hand['values'][user_current_hand_index])
        if cards_number == 1:
            draw_card(user_hand, user_current_hand_index)
            display_hand(user_hand, False, user_current_hand_index)
            cards_number = 2
        can_double = cards_number == 2
        # can_split = check_split(hand_index)
        can_split = True

        while True:
            choice = input(
                f"Would you like to Hit{', Double' if can_double else ''} {', Split' if can_split else ''} or Stand \n").lower()
            if choice == "hit":
                draw_card(user_hand, user_current_hand_index)
                cards_number += 1
                _, value = get_hand_value(user_hand["values"][user_current_hand_index], cards_number)
                if value == "Bust":
                    display_players()
                    break
            elif choice == "double" and can_double:
                draw_card(user_hand)
            elif choice == "split" and can_split:
                split_hand(user_current_hand_index)
                draw_card(user_hand, user_current_hand_index)
            elif choice == "stand":
                display_players()
                break
            else:
                continue
            display_hand(user_hand, False, user_current_hand_index)
        user_current_hand_index += 1


def check_split(hand_index):
    number_of_cards = len(user_hand["values"][hand_index])
    first_turn = number_of_cards == 2
    if first_turn:
        symbol1 = user_hand["symbols"][hand_index][0]
        symbol2 = user_hand["symbols"][hand_index][1]
        if symbol1 == symbol2:
            return True
    return False


def check_winner():
    dealer_cards = dealer_hand["values"][0]
    _, dealer_hand_value = get_hand_value(dealer_cards, len(dealer_cards))
    print(f"dealer's value = {dealer_hand_value}")

    for hand_index in range(number_of_hands):
        user_cards = user_hand["values"][0]
        _, user_hand_values = get_hand_value(user_cards, len(user_cards))
        print(f"user's value = {user_hand_values}")
        if user_hand_values == "Bust" or dealer_hand_value >= user_hand_values:
            print(f"Hand {hand_index} Lost")
        else:
            print(f"Hand {hand_index} Won")

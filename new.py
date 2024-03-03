import copy
import random

card_symbols = {1: "clovers", 2: "spades", 3: "hearts", 4: "diamonds"}
card_list = {"clovers": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
             "hearts": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
             "diamonds": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
             "spades": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]}
player_list = {
    "user": {
        "hand": [],
        "money": 500,
    },
    "dealer": {
        "hand": [],
        "values": [],
    },
}
player_options = ["Hit", "Stand", "Double" "Split"]


# return a copy of the original card list
def copy_shuffle_cards():
    # copy original card list
    cards_copy = copy.deepcopy(card_list)
    # shuffle copy
    for key in card_symbols:
        symbol = card_symbols[key]
        random.shuffle(cards_copy[symbol])
    return cards_copy


# will be used as a copy of card_list
cards_deck = copy_shuffle_cards()


# only used for first turn or when splitting hand
def add_hand(player):
    player["hand"].append({"cards": [], "symbols": []})


# will draw hands to a specific given list. example: hands["player"]["cards"][0]
# TODO: find way to use when hand is splitted
def draw_cards(player):
    symbol = str(card_symbols[random.randint(1, 4)])
    card = cards_deck[symbol].pop()
    print(card)
    player["hand"][0]["cards"].append(card)
    player["hand"][0]["symbols"].append(symbol[0].upper())


def first_draw():
    for _ in range(2):
        for player in player_list:
            draw_cards(player_list[player])


# print card total value
def display_hand_value(player_cards, number_of_cards):
    value = 0
    for card in range(number_of_cards):
        if isinstance(player_cards[card], str):
            if player_cards[card] == "A":
                value += 11
            else:
                value += 10
        else:
            value += int(player_cards[card])
    #     if value is 9 or lower add a space to center number
    print(f"       {value if value >= 10 else f' {value}'}")


# print cards
def display_hand(player_hand, hide_dealers_hand):
    """
    :param player_hand: whose hand is to be displayed
    :param hide_dealers_hand: used to only display the first card of the dealer

    card_rows : the number of rows in a card.
    number_of_cards : number of cards to display.

    will run a loop to display all the cards together row by row based on number_of_cards
    """
    card_rows = 5
    cards_to_display = 1
    if not hide_dealers_hand:
        cards_to_display = len(player_hand)
        print(f"Number of Cards = {cards_to_display}")
    cards = player_hand["cards"]
    symbols = player_hand["symbols"]
    for row in range(card_rows):
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

    display_hand_value(cards, cards_to_display)


def display_player_cards(player_name, hide_dealers_hand=False):
    player = player_list[player_name]
    print(f"       {player_name}")
    number_of_hands = len(player["hand"])
    for hand_index in range(number_of_hands):
        player_hand = player["hand"][hand_index]
        display_hand(player_hand, hide_dealers_hand)

import copy
import random
from typing import Final
import os

card_symbols = {1: "clovers", 2: "spades", 3: "hearts", 4: "diamonds"}
card_list = {"clovers": ["""--------
|1     |
|C    C|
|     1|
--------""", """--------
|2     |
|C    C|
|     2|
--------""", """--------
|3     |
|C    C|
|     3|
--------""", """--------
|4     |
|C    C|
|     4|
--------""", """--------
|5     |
|C    C|
|     5|
--------""", """--------
|6     |
|C    C|
|     6|
--------""", """--------
|7     |
|C    C|
|     7|
--------""", """--------
|8     |
|C    C|
|     8|
--------""", """--------
|9     |
|C    C|
|     9|
--------""", """--------
|10    |
|C    C|
|    10|
--------""", """--------
|J     |
|C    C|
|     J|
--------""", """--------
|Q     |
|C    C|
|     Q|
--------""", """--------
|K     |
|C    C|
|     K|
--------""", """--------
|A     |
|C    C|
|     A|
--------"""],
             "hearts": ["""--------
|1     |
|H    H|
|     1|
--------""", """--------
|2     |
|H    H|
|     2|
--------""", """--------
|3     |
|H    H|
|     3|
--------""", """--------
|4     |
|H    H|
|     4|
--------""", """--------
|5     |
|H    H|
|     5|
--------""", """--------
|6     |
|H    H|
|     6|
--------""", """--------
|7     |
|H    H|
|     7|
--------""", """--------
|8     |
|H    H|
|     8|
--------""", """--------
|9     |
|H    H|
|     9|
--------""", """--------
|10    |
|H    H|
|    10|
--------""", """--------
|J     |
|H    H|
|     J|
--------""", """--------
|Q     |
|H    H|
|     Q|
--------""", """--------
|K     |
|H    H|
|     K|
--------""", """--------
|A     |
|H    H|
|     A|
--------"""],
             "diamonds": ["""--------
|1     |
|D    D|
|     1|
--------""", """--------
|2     |
|D    D|
|     2|
--------""", """--------
|3     |
|D    D|
|     3|
--------""", """--------
|4     |
|D    D|
|     4|
--------""", """--------
|5     |
|D    D|
|     5|
--------""", """--------
|6     |
|D    D|
|     6|
--------""", """--------
|7     |
|D    D|
|     7|
--------""", """--------
|8     |
|D    D|
|     8|
--------""", """--------
|9     |
|D    D|
|     9|
--------""", """--------
|10    |
|D    D|
|    10|
--------""", """--------
|J     |
|D    D|
|     J|
--------""", """--------
|Q     |
|D    D|
|     Q|
--------""", """--------
|K     |
|D    D|
|     K|
--------""", """--------
|A     |
|D    D|
|     A|
--------"""],
             "spades": ["""--------
|1     |
|S    S|
|     1|
--------""", """--------
|2     |
|S    S|
|     2|
--------""", """--------
|3     |
|S    S|
|     3|
--------""", """--------
|4     |
|S    S|
|     4|
--------""", """--------
|5     |
|S    S|
|     5|
--------""", """--------
|6     |
|S    S|
|     6|
--------""", """--------
|7     |
|S    S|
|     7|
--------""", """--------
|8     |
|S    S|
|     8|
--------""", """--------
|9     |
|S    S|
|     9|
--------""", """--------
|10    |
|S    S|
|    10|
--------""", """--------
|J     |
|S    S|
|     J|
--------""", """--------
|Q     |
|S    S|
|     Q|
--------""", """--------
|K     |
|S    S|
|     K|
--------""", """--------
|A     |
|S    S|
|     A|
--------"""], }
hands = {
    "player": {
        "cards": [],
        "values": [],
        "money": 500,
    },
    "dealer": {
        "cards": [],
        "values": [],
    },
}
# index of value in card string
CARD_VALUE_INDEX: Final = 10


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


# will draw hands to a specific given list. example: hands["player"]["cards"][0]
def draw_cards(hand, is_dealer=False, hand_index=0):
    symbol = str(card_symbols[random.randint(1, 4)])
    card = cards_deck[symbol].pop()
    print(card)
    if is_dealer:
        hand.append(card)
    else:
        hand[hand_index].append(card)


# only used for first turn or when splitting hand
def add_hand():
    hand = hands["player"]
    hand["cards"].append([])
    hand["values"].append([])


def first_draw():
    for index in range(2):
        for hand in hands:
            if hand == "player":
                draw_cards(hands[hand]["cards"])
            else:
                draw_cards(hands[hand]["cards"], True)


#
card_image = card_list["clovers"].pop(10)
print(card_image)
try:
    print(f"card = {int(card_image[CARD_VALUE_INDEX])}")
except ValueError:
    print("card = 10")

from new import (card_symbols, card_list, add_hand, draw_cards, player_list, first_draw, display_player_cards,
                 get_hand_value)


def game_loop():
    while True:
        print("Blackjack")
        # TODO: add bet
        add_hand(player_list["user"])
        add_hand(player_list["dealer"])
        first_draw()
        display_player_cards("dealer", True)
        display_player_cards("user")

        while True:
            user_choice = input("Hit or Stand \n").lower()
            if user_choice == "hit":
                draw_cards(player_list["user"])
                display_player_cards("user")

            break

        break


game_loop()

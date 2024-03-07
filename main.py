import logic
import keyboard


def game_loop():
    while True:
        logic.set_default_values()
        logic.shuffle_deck()
        logic.first_draw()
        logic.display_players(True)
        logic.player_choice()
        logic.check_winner()
        break


game_loop()

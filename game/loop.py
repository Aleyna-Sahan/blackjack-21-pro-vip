import sys

import pygame

import display
from game import state
from game.events import handle_keydown, handle_mouse_down
from game.render import draw_final_score, draw_menu, draw_table
from ui.drawing import draw_table_background


def run_game():
    while True:
        draw_table_background(display.screen)
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                handle_mouse_down(mouse_pos)
            handle_keydown(event)

        if state.game_state == "DEALER_TURN":
            state.run_dealer_turn()

        if state.game_state == "MENU":
            draw_menu(display.screen, mouse_pos)
        elif state.game_state == "FINAL_SCORE":
            draw_final_score(display.screen, mouse_pos)
        else:
            draw_table(display.screen, mouse_pos)

        pygame.display.flip()
        display.clock.tick(30)

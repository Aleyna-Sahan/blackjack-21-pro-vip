import pygame

from constants import (
    btn_10_tur,
    btn_5_tur,
    btn_bet_minus,
    btn_bet_plus,
    btn_deal,
    btn_double,
    btn_hit,
    btn_main_menu,
    btn_next_round,
    btn_sinirsiz,
    btn_stand,
    input_box,
)
from oyuncu_sistemi import MIN_BET, calculate_hand, can_afford_bet, max_bet_for
from game import state


def handle_mouse_down(mouse_pos):
    gs = state.game_state
    if gs == "MENU":
        state.active_input = input_box.collidepoint(mouse_pos)
        if btn_5_tur.collidepoint(mouse_pos):
            state.start_new_game(5)
        elif btn_10_tur.collidepoint(mouse_pos):
            state.start_new_game(10)
        elif btn_sinirsiz.collidepoint(mouse_pos):
            state.start_new_game(0)

    elif gs == "BETTING":
        cap = max_bet_for(state.oyuncu.balance)
        if btn_bet_plus.collidepoint(mouse_pos) and state.can_bet(state.oyuncu.balance):
            if (state.oyuncu.bet + MIN_BET) <= cap:
                state.oyuncu.bet += MIN_BET
        elif btn_bet_minus.collidepoint(mouse_pos) and state.oyuncu.bet > MIN_BET:
            state.oyuncu.bet -= MIN_BET
        elif (
            btn_deal.collidepoint(mouse_pos)
            and state.can_bet(state.oyuncu.balance)
            and state.oyuncu.bet >= MIN_BET
            and can_afford_bet(state.oyuncu.balance, state.oyuncu.bet)
        ):
            if state.deal_initial_cards():
                state.oyuncu.status = "Oynuyor"
                state.game_state = "PLAYING"
                state.message = "Kartlarınızı oynayın!"

    elif gs == "PLAYING":
        if btn_hit.collidepoint(mouse_pos):
            state.oyuncu.hand.append(state.deck.deal())
            if calculate_hand(state.oyuncu.hand) > 21:
                state.oyuncu.status = "Battı"
                state.game_state = "DEALER_TURN"
        elif btn_stand.collidepoint(mouse_pos):
            state.oyuncu.status = "Kaldı"
            state.game_state = "DEALER_TURN"
        elif btn_double.collidepoint(mouse_pos) and len(state.oyuncu.hand) == 2:
            if can_afford_bet(state.oyuncu.balance, state.oyuncu.bet):
                state.oyuncu.balance -= state.oyuncu.bet
                state.oyuncu.bet *= 2
                state.oyuncu.hand.append(state.deck.deal())
                state.oyuncu.status = (
                    "Battı" if calculate_hand(state.oyuncu.hand) > 21 else "Kaldı (X2)"
                )
                state.game_state = "DEALER_TURN"

    elif gs == "GAME_OVER":
        if btn_next_round.collidepoint(mouse_pos):
            if state.total_rounds > 0 and state.current_round >= state.total_rounds:
                state.game_state = "FINAL_SCORE"
            else:
                state.current_round += 1
                state.game_state = "BETTING"
                state.prepare_betting_round()

    elif gs == "FINAL_SCORE":
        if btn_main_menu.collidepoint(mouse_pos):
            state.game_state = "MENU"
            state.player_name = ""
            state.active_input = False


def handle_keydown(event):
    if event.type != pygame.KEYDOWN or state.game_state != "MENU" or not state.active_input:
        return
    if event.key == pygame.K_BACKSPACE:
        state.player_name = state.player_name[:-1]
    elif len(state.player_name) < 12 and event.unicode.isprintable():
        state.player_name += event.unicode

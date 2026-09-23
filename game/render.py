import pygame

from constants import (
    BLACK,
    BTN_GOLD,
    BTN_GOLD_HOVER,
    BTN_HOVER,
    BTN_NORMAL,
    GOLD,
    INPUT_BOX_COLOR,
    INPUT_TEXT_COLOR,
    MESSAGE_Y,
    PLACEHOLDER_TEXT,
    SCREEN_WIDTH,
    bet_amount_rect,
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
from game import state
import display
from ui.buttons import draw_bottom_bar
from ui.drawing import draw_button, draw_table_background
from ui.layout import draw_layout


def draw_menu(surface, mouse_pos):
    baslik = display.big_font.render("VIP BLACKJACK 21", True, GOLD)
    surface.blit(baslik, (SCREEN_WIDTH // 2 - baslik.get_width() // 2, 110))
    pygame.draw.rect(
        surface,
        (70, 70, 70) if state.active_input else INPUT_BOX_COLOR,
        input_box,
        border_radius=10,
    )
    pygame.draw.rect(surface, GOLD if state.active_input else BLACK, input_box, 3, border_radius=10)
    isim = PLACEHOLDER_TEXT if state.player_name == "" else state.player_name
    isim_color = (120, 120, 120) if state.player_name == "" else INPUT_TEXT_COLOR
    isim_text = display.title_font.render(isim, True, isim_color)
    surface.blit(
        isim_text,
        (input_box.x + (input_box.width - isim_text.get_width()) // 2, input_box.y + 7),
    )
    draw_button(surface, btn_5_tur, "5 Tur", BTN_NORMAL, BTN_HOVER, mouse_pos)
    draw_button(surface, btn_10_tur, "10 Tur", BTN_NORMAL, BTN_HOVER, mouse_pos)
    draw_button(surface, btn_sinirsiz, "Sınırsız", BTN_NORMAL, BTN_HOVER, mouse_pos)


def draw_final_score(surface, mouse_pos):
    surface.blit(display.title_font.render("Final Skorlar", True, GOLD), (SCREEN_WIDTH // 2 - 120, 100))
    sirali = sorted(state.all_players, key=lambda x: x.balance, reverse=True)
    for index, p in enumerate(sirali):
        renk = GOLD if p.name == state.oyuncu.name else (248, 248, 245)
        skor_text = display.title_font.render(
            f"{index + 1}. {p.name} - Bakiye: {p.balance} TL", True, renk
        )
        surface.blit(skor_text, (SCREEN_WIDTH // 2 - 200, 180 + index * 65))
    draw_button(surface, btn_main_menu, "Ana Menü", BTN_GOLD, BTN_GOLD_HOVER, mouse_pos, accent=True)


def draw_table(surface, mouse_pos):
    msg = display.title_font.render(state.message, True, GOLD)
    surface.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, MESSAGE_Y))
    draw_layout(surface, state.oyuncu, state.kasa, state.bots, state.game_state)
    draw_bottom_bar(surface, state.oyuncu, show_bet_info=(state.game_state == "BETTING"))

    gs = state.game_state
    if gs == "BETTING":
        draw_button(surface, btn_bet_minus, "-", BTN_NORMAL, BTN_HOVER, mouse_pos)
        draw_button(surface, btn_bet_plus, "+", BTN_NORMAL, BTN_HOVER, mouse_pos)
        draw_button(surface, btn_deal, "Dağıt", BTN_GOLD, BTN_GOLD_HOVER, mouse_pos, accent=True)
        bet_txt = display.title_font.render(f"{state.oyuncu.bet} TL", True, GOLD)
        surface.blit(
            bet_txt,
            (
                bet_amount_rect.centerx - bet_txt.get_width() // 2,
                bet_amount_rect.centery - bet_txt.get_height() // 2,
            ),
        )
    elif gs == "PLAYING":
        draw_button(surface, btn_hit, "İste", BTN_NORMAL, BTN_HOVER, mouse_pos)
        draw_button(surface, btn_stand, "Kal", BTN_NORMAL, BTN_HOVER, mouse_pos)
        if len(state.oyuncu.hand) == 2:
            draw_button(surface, btn_double, "Double", BTN_GOLD, BTN_GOLD_HOVER, mouse_pos, accent=True)
    elif gs == "GAME_OVER":
        draw_button(surface, btn_next_round, "Devam", BTN_GOLD, BTN_GOLD_HOVER, mouse_pos, accent=True)

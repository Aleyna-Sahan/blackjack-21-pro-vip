import pygame

from constants import BOTTOM_BAR_H, BOTTOM_BAR_Y, GOLD_DIM, SCREEN_WIDTH, TABLE_BORDER
from oyuncu_sistemi import max_bet_for
import display


def draw_bottom_bar(surface, oyuncu=None, show_bet_info=False):
    bar = pygame.Rect(36, BOTTOM_BAR_Y - 8, SCREEN_WIDTH - 72, BOTTOM_BAR_H + 4)
    pygame.draw.rect(surface, (8, 38, 18), bar.move(0, 3), border_radius=12)
    pygame.draw.rect(surface, (14, 62, 28), bar, border_radius=12)
    pygame.draw.rect(surface, GOLD_DIM, bar, 1, border_radius=12)
    pygame.draw.rect(surface, TABLE_BORDER, bar, 2, border_radius=12)
    if show_bet_info and oyuncu is not None:
        cap = max_bet_for(oyuncu.balance)
        info = f"Bakiye: {oyuncu.balance} TL  ·  Max bahis: {cap} TL"
        info_surf = display.small_font.render(info, True, GOLD_DIM)
        surface.blit(info_surf, (bar.x + 14, bar.y + bar.height - 18))

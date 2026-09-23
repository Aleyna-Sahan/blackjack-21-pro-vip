import pygame

from constants import MARGIN_X, SCREEN_WIDTH


def clamp_x(left, width):
    return max(MARGIN_X, min(left, SCREEN_WIDTH - MARGIN_X - width))


def blit_centered_clamped(surface, surf, center_x, y):
    x = clamp_x(center_x - surf.get_width() // 2, surf.get_width())
    surface.blit(surf, (x, y))
    return pygame.Rect(x, y, surf.get_width(), surf.get_height())

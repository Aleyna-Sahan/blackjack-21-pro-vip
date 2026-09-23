import pygame

from constants import CAPTION, SCREEN_HEIGHT, SCREEN_WIDTH

screen = None
clock = None
font = None
title_font = None
big_font = None
small_font = None
rank_font = None
label_font = None


def init_display():
    global screen, clock, font, title_font, big_font, small_font, rank_font, label_font
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Segoe UI", 20, bold=True)
    title_font = pygame.font.SysFont("Segoe UI", 28, bold=True)
    big_font = pygame.font.SysFont("Segoe UI", 45, bold=True)
    small_font = pygame.font.SysFont("Segoe UI", 14, bold=True)
    rank_font = pygame.font.SysFont("Segoe UI", 24, bold=True)
    label_font = pygame.font.SysFont("Segoe UI", 17, bold=True)

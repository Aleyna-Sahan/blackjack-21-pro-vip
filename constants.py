import pygame

TABLE_GREEN = (12, 58, 24)
TABLE_GREEN_LIGHT = (22, 88, 38)
TABLE_BORDER = (90, 55, 25)
WHITE = (248, 248, 245)
BLACK = (12, 12, 14)
RED = (210, 35, 45)
GOLD = (255, 210, 70)
GOLD_DIM = (200, 165, 50)
SHADOW = (5, 18, 8)
BTN_NORMAL = (218, 218, 225)
BTN_HOVER = (255, 255, 255)
BTN_GOLD = (235, 195, 55)
BTN_GOLD_HOVER = (255, 228, 110)
BTN_TEXT = (28, 28, 32)
INPUT_BOX_COLOR = (32, 38, 42)
INPUT_TEXT_COLOR = (210, 255, 210)
STATUS_WIN = (55, 175, 95)
STATUS_LOSE = (210, 55, 55)
STATUS_PUSH = (95, 145, 220)
STATUS_BJ = (255, 200, 50)

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700

CARD_W, CARD_H = 70, 100
MARGIN_X = 28
MESSAGE_Y = 20
MESSAGE_CLEARANCE = 54
DEALER_Y = 108
LABEL_GAP = 14
INFO_LINE_GAP = 4
INFO_CARD_GAP = 12
SCORE_GAP = 12
BADGE_PAD = 8
CHIP_ABOVE_GAP = 10
CHIP_RADIUS = 13
BOTTOM_BAR_Y = 628
BOTTOM_BAR_H = 52
BET_CTRL_GAP = 14
BET_SLOT_W = 96
BET_CLUSTER_X = 402
TABLE_CX = SCREEN_WIDTH // 2
TABLE_CY = 318
ARC_RX = 298
ARC_RY = 162
SEAT_ANGLES = [3.14, 2.22, 1.48, 0.20]
SEAT_CARD_NUDGE = [-14, -6, 0, 14]

PLAY_GAP = 14
CAPTION = "Blackjack 21 Pro - VIP Edition"
PLACEHOLDER_TEXT = "İsminizi Girin..."

input_box = pygame.Rect(SCREEN_WIDTH // 2 - 150, 200, 300, 40)
btn_5_tur = pygame.Rect(SCREEN_WIDTH // 2 - 120, 280, 100, 40)
btn_10_tur = pygame.Rect(SCREEN_WIDTH // 2 - 10, 280, 100, 40)
btn_sinirsiz = pygame.Rect(SCREEN_WIDTH // 2 + 100, 280, 120, 40)
btn_bet_minus = pygame.Rect(BET_CLUSTER_X, BOTTOM_BAR_Y + 4, 50, 40)
btn_bet_plus = pygame.Rect(
    BET_CLUSTER_X + 50 + BET_CTRL_GAP + BET_SLOT_W + BET_CTRL_GAP,
    BOTTOM_BAR_Y + 4,
    50,
    40,
)
btn_deal = pygame.Rect(btn_bet_plus.right + BET_CTRL_GAP, BOTTOM_BAR_Y, 110, 45)
bet_amount_rect = pygame.Rect(
    btn_bet_minus.right + BET_CTRL_GAP,
    BOTTOM_BAR_Y + 4,
    btn_bet_plus.left - btn_bet_minus.right - 2 * BET_CTRL_GAP,
    40,
)
btn_hit = pygame.Rect(BET_CLUSTER_X, BOTTOM_BAR_Y, 85, 45)
btn_stand = pygame.Rect(btn_hit.right + PLAY_GAP, BOTTOM_BAR_Y, 85, 45)
btn_double = pygame.Rect(btn_stand.right + PLAY_GAP, BOTTOM_BAR_Y, 95, 45)
btn_next_round = pygame.Rect(SCREEN_WIDTH // 2 - 65, BOTTOM_BAR_Y, 130, 45)
btn_main_menu = pygame.Rect(SCREEN_WIDTH // 2 - 80, 520, 160, 45)

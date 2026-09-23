import pygame

from constants import (
    BLACK,
    BTN_TEXT,
    CARD_H,
    CARD_W,
    GOLD,
    GOLD_DIM,
    RED,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SHADOW,
    STATUS_BJ,
    STATUS_LOSE,
    STATUS_PUSH,
    STATUS_WIN,
    TABLE_BORDER,
    TABLE_GREEN,
    TABLE_GREEN_LIGHT,
    WHITE,
)
import display


def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))


def draw_card(surface, card, x, y, face_up=True):
    rect = pygame.Rect(x, y, CARD_W, CARD_H)
    pygame.draw.rect(surface, SHADOW, pygame.Rect(x + 4, y + 6, CARD_W, CARD_H), border_radius=9)
    pygame.draw.rect(surface, (30, 30, 35), pygame.Rect(x + 2, y + 3, CARD_W, CARD_H), border_radius=9)
    if face_up:
        pygame.draw.rect(surface, WHITE, rect, border_radius=9)
        pygame.draw.rect(surface, (180, 180, 185), rect, 1, border_radius=9)
        color = RED if card.suit in ["♦", "♥"] else BLACK
        rank = str(card.value)
        suit = card.suit
        surface.blit(display.small_font.render(rank, True, color), (x + 7, y + 6))
        surface.blit(display.small_font.render(suit, True, color), (x + 7, y + 22))
        big = display.rank_font.render(rank, True, color)
        surface.blit(big, (x + CARD_W // 2 - big.get_width() // 2, y + CARD_H // 2 - 14))
        surface.blit(display.small_font.render(suit, True, color), (x + CARD_W // 2 - 6, y + CARD_H // 2 + 8))
        br = display.small_font.render(rank, True, color)
        bs = display.small_font.render(suit, True, color)
        surface.blit(br, (x + CARD_W - br.get_width() - 7, y + CARD_H - br.get_height() - 20))
        surface.blit(bs, (x + CARD_W - bs.get_width() - 7, y + CARD_H - bs.get_height() - 6))
    else:
        pygame.draw.rect(surface, (165, 25, 35), rect, border_radius=9)
        pygame.draw.rect(surface, WHITE, rect, 2, border_radius=9)
        inner = pygame.Rect(x + 10, y + 10, CARD_W - 20, CARD_H - 20)
        pygame.draw.rect(surface, (120, 18, 28), inner, border_radius=6)
        pygame.draw.rect(surface, GOLD_DIM, inner, 2, border_radius=6)
        cross = display.rank_font.render("♠", True, GOLD)
        surface.blit(cross, (x + CARD_W // 2 - cross.get_width() // 2, y + CARD_H // 2 - 14))


def draw_table_background(surface):
    for y in range(SCREEN_HEIGHT):
        t = y / SCREEN_HEIGHT
        pygame.draw.line(
            surface, lerp_color((6, 32, 14), TABLE_GREEN_LIGHT, t), (0, y), (SCREEN_WIDTH, y)
        )
    felt = pygame.Rect(48, 62, SCREEN_WIDTH - 96, SCREEN_HEIGHT - 135)
    pygame.draw.ellipse(surface, (10, 52, 22), felt)
    pygame.draw.ellipse(surface, (18, 78, 32), felt.inflate(-6, -6))
    pygame.draw.ellipse(surface, TABLE_BORDER, felt, 4)
    pygame.draw.ellipse(surface, GOLD_DIM, felt.inflate(-12, -12), 1)
    vignette = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    for edge in range(80):
        alpha = int(55 * (edge / 80) ** 1.4)
        pygame.draw.rect(vignette, (0, 0, 0, alpha), (edge, 0, 1, SCREEN_HEIGHT))
        pygame.draw.rect(vignette, (0, 0, 0, alpha), (SCREEN_WIDTH - 1 - edge, 0, 1, SCREEN_HEIGHT))
        pygame.draw.rect(vignette, (0, 0, 0, alpha), (0, edge, SCREEN_WIDTH, 1))
        pygame.draw.rect(vignette, (0, 0, 0, alpha), (0, SCREEN_HEIGHT - 1 - edge, SCREEN_WIDTH, 1))
    surface.blit(vignette, (0, 0))
    pygame.draw.rect(surface, TABLE_BORDER, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 18, border_radius=14)
    pygame.draw.rect(surface, GOLD_DIM, (12, 12, SCREEN_WIDTH - 24, SCREEN_HEIGHT - 24), 2, border_radius=12)


def draw_button(surface, rect, text, normal_color, hover_color, mouse_pos, accent=False):
    hovered = rect.collidepoint(mouse_pos)
    base = hover_color if hovered else normal_color
    top = lerp_color(base, WHITE, 0.22 if hovered else 0.12)
    bot = lerp_color(base, BLACK, 0.08)
    pygame.draw.rect(surface, bot, rect.move(0, 2), border_radius=10)
    pygame.draw.rect(surface, top, rect, border_radius=10)
    border_c = GOLD if accent else (50, 50, 55)
    pygame.draw.rect(surface, border_c, rect, 2, border_radius=10)
    txt = display.font.render(text, True, BTN_TEXT)
    surface.blit(
        txt,
        (rect.x + (rect.width - txt.get_width()) // 2, rect.y + (rect.height - txt.get_height()) // 2),
    )


def status_badge_color(status):
    if "Blackjack" in status:
        return STATUS_BJ
    if status.startswith("Battı") or status == "Kaybetti":
        return STATUS_LOSE
    if "Berabere" in status or "Kazandı" in status:
        return STATUS_WIN if "Kazandı" in status else STATUS_PUSH
    return (70, 75, 85)


def draw_status_badge(surface, text, center_x, y, left_aligned=False):
    from ui.helpers import clamp_x

    if not text or text in ("Bekliyor", "Oynuyor", "Kaldı", "Kaldı (X2)"):
        return
    surf = display.small_font.render(text, True, WHITE)
    pad_x, pad_y = 10, 4
    w, h = surf.get_width() + pad_x * 2, surf.get_height() + pad_y * 2
    if left_aligned:
        rect = pygame.Rect(center_x, y, w, h)
        rect.x = clamp_x(rect.x, w)
    else:
        rect = pygame.Rect(center_x - w // 2, y, w, h)
    pygame.draw.rect(surface, status_badge_color(text), rect, border_radius=8)
    pygame.draw.rect(surface, WHITE, rect, 1, border_radius=8)
    surface.blit(surf, (rect.x + pad_x, rect.y + pad_y))


def draw_chip_bet(surface, amount, center_x, card_top):
    from constants import CHIP_ABOVE_GAP, CHIP_RADIUS

    if amount <= 0:
        return
    chip_y = card_top - CHIP_ABOVE_GAP - CHIP_RADIUS
    pygame.draw.circle(surface, (205, 42, 48), (center_x, chip_y), CHIP_RADIUS)
    pygame.draw.circle(surface, WHITE, (center_x, chip_y), CHIP_RADIUS, 2)
    pygame.draw.circle(surface, GOLD_DIM, (center_x, chip_y), 7, 1)
    txt = display.small_font.render(str(amount), True, WHITE)
    surface.blit(txt, (center_x - txt.get_width() // 2, chip_y - txt.get_height() // 2))

import math

from constants import (
    ARC_RX,
    ARC_RY,
    BADGE_PAD,
    CARD_H,
    CARD_W,
    DEALER_Y,
    GOLD,
    INFO_CARD_GAP,
    INFO_LINE_GAP,
    LABEL_GAP,
    MESSAGE_CLEARANCE,
    SCORE_GAP,
    SCREEN_WIDTH,
    SEAT_ANGLES,
    SEAT_CARD_NUDGE,
    TABLE_CX,
    TABLE_CY,
)
from oyuncu_sistemi import calculate_hand
import display
from ui.drawing import draw_card, draw_chip_bet, draw_status_badge
from ui.helpers import blit_centered_clamped


def seat_position(seat_index, total_seats=4):
    if seat_index < len(SEAT_ANGLES):
        angle = SEAT_ANGLES[seat_index]
    else:
        t = seat_index / max(total_seats - 1, 1)
        angle = math.pi * (1.02 - t * 0.52)
    cx = TABLE_CX
    cy = TABLE_CY
    x = cx + int(math.cos(angle) * ARC_RX)
    y = cy + int(math.sin(angle) * ARC_RY)
    return x, y


def card_spread(hand_len, seat_index=None):
    if hand_len <= 1:
        return 0
    base = min(36, max(26, 130 // hand_len))
    if seat_index in (0, 3):
        return min(base, 28)
    return base


def fan_bounds(center_x, card_y, hand_len, seat_index=None):
    spread = card_spread(hand_len, seat_index)
    fan_w = CARD_W + spread * max(hand_len - 1, 0)
    start_x = center_x - fan_w // 2
    import pygame

    card_rect = pygame.Rect(start_x, card_y, fan_w, CARD_H)
    return spread, start_x, card_rect


def player_info_surfaces(player, is_human):
    from constants import GOLD, GOLD_DIM, WHITE

    name_color = GOLD if is_human else WHITE
    return [
        display.label_font.render(player.name, True, name_color),
        display.label_font.render(f"{player.balance} TL", True, (200, 205, 210)),
        display.label_font.render(f"Bahis: {player.bet}", True, GOLD_DIM),
    ]


def info_block_height(surfaces):
    if not surfaces:
        return 0
    return sum(s.get_height() for s in surfaces) + INFO_LINE_GAP * (len(surfaces) - 1)


def draw_player_info_block(surface, player, center_x, card_top, is_human=False):
    from constants import CHIP_ABOVE_GAP, CHIP_RADIUS

    surfaces = player_info_surfaces(player, is_human)
    block_h = info_block_height(surfaces)
    anchor_bottom = card_top - INFO_CARD_GAP
    if player.bet > 0:
        chip_top = card_top - CHIP_ABOVE_GAP - CHIP_RADIUS * 2
        anchor_bottom = min(anchor_bottom, chip_top - INFO_CARD_GAP)
    y = max(anchor_bottom - block_h, MESSAGE_CLEARANCE)
    for surf in surfaces:
        blit_centered_clamped(surface, surf, center_x, y)
        y += surf.get_height() + INFO_LINE_GAP


def draw_player_seat_cards(surface, player, center_x, card_y, seat_index=None):
    from constants import MARGIN_X

    n = len(player.hand)
    spread, start_x, card_rect = fan_bounds(center_x, card_y, max(n, 1), seat_index)
    card_top = card_rect.top
    card_bottom = card_rect.bottom

    if player.bet > 0:
        draw_chip_bet(surface, player.bet, center_x, card_top)

    for i, card in enumerate(player.hand):
        draw_card(surface, card, start_x + i * spread, card_y)

    if player.hand:
        score = calculate_hand(player.hand)
        score_surf = display.label_font.render(f"Skor {score}", True, (200, 205, 210))
        score_y = card_bottom + SCORE_GAP
        score_rect = blit_centered_clamped(surface, score_surf, center_x, score_y)
        if player.status not in ("Bekliyor", "Oynuyor", "Kaldı", "Kaldı (X2)"):
            badge_surf = display.small_font.render(player.status, True, (248, 248, 245))
            badge_w = badge_surf.get_width() + 20
            inline_x = score_rect.right + BADGE_PAD
            if inline_x + badge_w <= SCREEN_WIDTH - MARGIN_X:
                draw_status_badge(
                    surface, player.status, inline_x, score_rect.top, left_aligned=True
                )
            else:
                draw_status_badge(surface, player.status, center_x, score_rect.bottom + BADGE_PAD)


def draw_layout(surface, oyuncu, kasa, bots, game_state):
    show_hole = game_state == "GAME_OVER"

    dealer_cx = SCREEN_WIDTH // 2
    kasa_y = DEALER_Y
    n_d = len(kasa.hand)
    d_spread, kasa_x, dealer_card_rect = fan_bounds(dealer_cx, kasa_y, max(n_d, 1))
    kasa_label = display.title_font.render("KASA", True, GOLD)
    sub = display.small_font.render("Kurpiyer", True, (180, 185, 190))
    sub_gap = 6
    label_block_h = kasa_label.get_height() + sub_gap + sub.get_height()
    label_top = dealer_card_rect.top - LABEL_GAP - label_block_h
    label_top = max(label_top, MESSAGE_CLEARANCE)
    blit_centered_clamped(surface, kasa_label, dealer_cx, label_top)
    blit_centered_clamped(surface, sub, dealer_cx, label_top + kasa_label.get_height() + sub_gap)
    for i, card in enumerate(kasa.hand):
        face = show_hole or i > 0
        draw_card(surface, card, kasa_x + i * (d_spread or 0), kasa_y, face_up=face)
    if kasa.hand:
        d_score = calculate_hand(kasa.hand) if show_hole else "?"
        score_surf = display.font.render(f"Skor: {d_score}", True, (248, 248, 245))
        blit_centered_clamped(surface, score_surf, dealer_cx, dealer_card_rect.bottom + SCORE_GAP)

    seats = [bots[0], bots[1], oyuncu, bots[2]]
    seat_layout = []
    for idx, player in enumerate(seats):
        center_x, card_y = seat_position(idx, len(seats))
        if idx < len(SEAT_CARD_NUDGE):
            center_x += SEAT_CARD_NUDGE[idx]
        seat_layout.append((idx, player, center_x, card_y, player is oyuncu))

    for idx, player, center_x, card_y, _ in seat_layout:
        draw_player_seat_cards(surface, player, center_x, card_y, seat_index=idx)
    for idx, player, center_x, card_y, is_human in seat_layout:
        _, _, card_rect = fan_bounds(center_x, card_y, max(len(player.hand), 1), idx)
        draw_player_info_block(surface, player, center_x, card_rect.top, is_human=is_human)

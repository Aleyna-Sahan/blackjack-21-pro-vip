from kart_sistemi import Deck
from oyuncu_sistemi import (
    MIN_BET,
    Player,
    calculate_hand,
    can_afford_bet,
    max_bet_for,
)

deck = Deck()
kasa = Player("Kurpiyer")
oyuncu = Player("Oyuncu", balance=100)
bots = [
    Player("Bot Alex", is_bot=True),
    Player("Bot Sam", is_bot=True),
    Player("Bot Mia", is_bot=True),
]
all_players = bots + [oyuncu]
oyuncu.bet = 10

game_state = "MENU"
player_name = ""
message = ""
current_round = 0
total_rounds = 0
active_input = False


def is_blackjack(hand):
    return len(hand) == 2 and calculate_hand(hand) == 21


def can_bet(balance):
    return max_bet_for(balance) >= MIN_BET


def clamp_human_bet():
    bal = oyuncu.balance
    if not can_bet(bal):
        oyuncu.bet = 0
        return
    oyuncu.bet = max(MIN_BET, min(oyuncu.bet, max_bet_for(bal)))


def prepare_betting_round():
    global message
    clamp_human_bet()
    for bot in bots:
        bot.reset_hand()
    if not can_bet(oyuncu.balance):
        message = "Bahis yapılamıyor — bakiye yetersiz."
    elif total_rounds > 0:
        message = f"Tur {current_round}/{total_rounds} — Bahsinizi belirleyin"
    else:
        message = "Bahsinizi belirleyin"


def start_new_game(rounds):
    global deck, game_state, current_round, total_rounds, message

    oyuncu.name = player_name.strip() if player_name.strip() else "Oyuncu"
    oyuncu.balance = 100
    oyuncu.bet = 10
    oyuncu.hand = []
    oyuncu.status = "Bekliyor"

    for bot in bots:
        bot.balance = 100
        bot.hand = []
        bot.status = "Bekliyor"
        bot.bet = 0

    kasa.hand = []
    kasa.status = "Bekliyor"
    deck = Deck()
    total_rounds = rounds
    current_round = 1
    game_state = "BETTING"
    prepare_betting_round()


def deal_initial_cards():
    kasa.hand = []
    kasa.status = "Bekliyor"

    for p in all_players:
        p.reset_hand()

    if not can_afford_bet(oyuncu.balance, oyuncu.bet):
        return False

    oyuncu.balance -= oyuncu.bet
    for bot in bots:
        if bot.bet > 0 and can_afford_bet(bot.balance, bot.bet):
            bot.balance -= bot.bet
        else:
            bot.bet = 0

    for _ in range(2):
        for p in all_players:
            p.hand.append(deck.deal())
        kasa.hand.append(deck.deal())
    return True


def _payout_player(player, dealer_total, dealer_bj, dealer_bust):
    bet = player.bet
    if bet <= 0:
        return

    total = calculate_hand(player.hand)
    player_bj = is_blackjack(player.hand)
    bust = total > 21 or player.status.startswith("Battı")

    if bust:
        player.status = "Battı"
        return

    if dealer_bj:
        if player_bj:
            player.balance += bet
            player.status = "Berabere (BJ)"
        else:
            player.status = "Kaybetti"
        return

    if player_bj:
        player.balance += int(bet * 2.5)
        player.status = "Blackjack!"
        return

    if dealer_bust:
        player.balance += bet * 2
        player.status = "Kazandı"
    elif total > dealer_total:
        player.balance += bet * 2
        player.status = "Kazandı"
    elif total == dealer_total:
        player.balance += bet
        player.status = "Berabere"
    else:
        player.status = "Kaybetti"


def resolve_game():
    dealer_total = calculate_hand(kasa.hand)
    dealer_bj = is_blackjack(kasa.hand)
    dealer_bust = dealer_total > 21

    for p in all_players:
        _payout_player(p, dealer_total, dealer_bj, dealer_bust)


def run_dealer_turn():
    global game_state, message

    for bot in bots:
        if bot.bet > 0 and calculate_hand(bot.hand) < 17:
            while calculate_hand(bot.hand) < 17:
                bot.hand.append(deck.deal())
        bot.status = "Battı" if calculate_hand(bot.hand) > 21 else "Kaldı"
    while calculate_hand(kasa.hand) < 17:
        kasa.hand.append(deck.deal())
    resolve_game()
    game_state = "GAME_OVER"
    message = "El Tamamlandı!"

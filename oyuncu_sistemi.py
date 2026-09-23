import random

MIN_BET = 10
NEGATIVE_BALANCE_CAP = 100


def max_bet_for(balance):
    """Max wager this round. Negative balance: up to NEGATIVE_BALANCE_CAP; else balance + cap."""
    if balance >= 0:
        return balance + NEGATIVE_BALANCE_CAP
    return NEGATIVE_BALANCE_CAP


def can_afford_bet(balance, amount):
    return amount > 0 and amount <= max_bet_for(balance)


# OOP: Oyuncu Sınıfı
class Player:
    def __init__(self, name, is_bot=False, balance=100):
        self.name = name
        self.is_bot = is_bot
        self.balance = balance
        self.hand = []
        self.bet = 0
        self.status = "Bekliyor"
        
    def reset_hand(self):
        self.hand = []
        self.status = "Bekliyor"
        if self.is_bot:
            cap = max_bet_for(self.balance)
            if cap < MIN_BET:
                self.bet = 0
            elif cap < MIN_BET * 2:
                self.bet = min(cap, MIN_BET)
            elif cap <= 100:
                opts = [b for b in [10, 20, 50, 100] if b <= cap]
                self.bet = random.choice(opts) if opts else cap
            else:
                opts = [b for b in [50, 100, (cap // 20) * 10] if b <= cap]
                self.bet = random.choice(opts) if opts else cap
            self.bet = min(self.bet, cap)

def calculate_hand(hand):
    total = sum(card.get_bj_value() for card in hand)
    aces = sum(1 for card in hand if card.value == 'A')
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total
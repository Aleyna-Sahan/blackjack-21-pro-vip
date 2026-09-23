import random

# OOP: Kart Sınıfı
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def get_bj_value(self):
        if self.value in ['J', 'Q', 'K']: return 10
        elif self.value == 'A': return 11
        return int(self.value)

# OOP: Deste Sınıfı
class Deck:
    def __init__(self):
        suits = ['♠', '♦', '♥', '♣']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, val) for suit in suits for val in values] * 4 
        random.shuffle(self.cards)
        
    def deal(self):
        if len(self.cards) < 15: self.__init__()
        return self.cards.pop()
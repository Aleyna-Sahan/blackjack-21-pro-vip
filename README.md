# ♠️ Blackjack 21 Pro - VIP Edition

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.5+-green?style=for-the-badge&logo=python&logoColor=white)](https://www.pygame.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**Blackjack 21 Pro - VIP Edition** is a desktop Blackjack (21) simulation developed using Python and the **Pygame** library, following **Object-Oriented Programming (OOP)** principles, featuring a modular architecture and autonomous bot AI.

It offers a complete gaming experience with realistic 4-deck card distribution mechanics (The Shoe), dynamic Ace value management, bot AI that makes decisions by analyzing balance and credit limits, and a VIP casino table atmosphere.

---

## 📸 Screenshot
<div align="center">
  <img src="assets/gameplay.png" alt="Blackjack 21 Pro - VIP Edition Gameplay" width="800"/>
</div>

---

## 🎯 Key Features
- **🃏 4-Deck Combined Card System (The Shoe):** Operates by combining 4 full decks for a realistic casino scenario. When the number of cards in the deck drops below 15, the system automatically resets and reshuffles the deck without interrupting the game.
- **⚡ Dynamic Blackjack Rules & Moves:**
  - Face cards (Jack, Queen, King) are worth **10**.
  - **Dynamic Ace Management:** When the hand total exceeds 21, the Ace value automatically drops from 11 to 1 to prevent the player from busting.
  - **Move Options:** `Hit`, `Stand`, and `Double`.
- **🤖 Autonomous Bot AI:** AI players at the table place autonomous bets in tiered amounts (10, 20, 50, 100) suitable for casino dynamics by analyzing their current balances and credit limits at the beginning of the round.
- **💰 Finance & Credit Mechanics:** There is a minimum bet base of 10 units. Players have the flexibility to go into negative balance (credit/debt) down to -100 units even if their balance runs out.
- **🔄 Customizable Game Loop:** **5 Rounds**, **10 Rounds**, or **Unlimited Game** modes offered for player selection at the startup phase.
- **🎨 VIP Interface & Visual Feedback:** Custom green table tones at 1100x700 resolution, circular seating arrangement with radian angles, Segoe UI typography, interactive buttons, and real-time status feedback (*Win, Lose, Tie, Blackjack*).

---

## 🏛️ Architecture and Modular Structure

The project is designed in a modular structure, adhering to the principle of *Separation of Concerns*:

```text
BlackJack/
├── assets/             # In-game screenshots and visual materials
├── game/               # Game loop and round flow controls
├── ui/                 # User interface drawing and rendering components
├── constants.py        # Color palettes, geometric constants, button coordinates
├── display.py          # Graphics engine initializer, font management, FPS Clock
├── kart_sistemi.py     # Card and Deck OOP classes, deck management
├── oyuncu_sistemi.py   # Player class, bot AI, dynamic hand calculation
├── main.py             # Application Entry Point
├── requirements.txt    # Dependencies (pygame)
├── .gitignore          # Files to be ignored by Git
└── README.md           # Project documentation
```

### Module Responsibilities
*   **constants.py (Constants and Configuration):** RGB color definitions for green table tones, card/button colors, shadows, and feedback states. Screen resolution (1100x700), card dimensions (70x100), interface paddings, and table seating angles in radians. Button interaction coordinates (Hit, Stand, Double, Bet +/-) defined with `pygame.Rect` objects.
*   **display.py (Display and Typography):** Initialization of the Pygame engine and window creation with the `init_display()` function. Global Segoe UI font family loaded in different sizes and weights. Pygame Clock object for frame rate synchronization.
*   **kart_sistemi.py (Card and Deck Mechanics):** `Card` class: Models the card suit (Hearts, Spades, Diamonds, Clubs) and value; calculates the blackjack score with `get_bj_value()`. `Deck` class: Combines 4 decks, shuffles with `random.shuffle()`; automatically resets and distributes the deck when the card count falls below 15.
*   **oyuncu_sistemi.py (Player, Bot and Mathematical Logic):** `Player` class: Manages real player and bot data (name, balance, current bet, hand). Bot Logic: Autonomous bet determination algorithm based on balance status within `reset_hand()`. Finance Control: Borrowing control up to -100 units with `max_bet_for()` and `can_afford_bet()`. `calculate_hand()`: Scoring mechanism that dynamically manages the Ace card's 11 or 1 value to prevent busting.
*   **main.py (Main Executor):** The entry point of the system. Boots up screen components (`init_display()`) and starts the game by triggering the main game loop.

---

## 🚀 Installation and Execution

### Requirements
*   Python 3.8 or higher
*   Pygame 2.5+

### Execution Steps

1. Clone the repository:
```bash
git clone https://github.com/Aleyna-Sahan/blackjack-21-pro-vip.git
cd blackjack-21-pro-vip
```

2. Install required libraries:
```bash
pip install -r requirements.txt
```

3. Start the game:
```bash
python3 main.py
```

---

## 🎮 Game Controls

| Control | Function |
| :--- | :--- |
| **Hit** | Draws 1 new card from the deck to the player's hand. |
| **Stand** | Locks the current hand score and passes the turn to the next player/dealer. |
| **Double** | Doubles the bet amount, draws only 1 card, and ends the player's turn. |
| **Bet (+ / -)** | Increases or decreases the bet amount before the round starts. |
| **Round Selection** | Provides the choice of 5 rounds, 10 rounds, or unlimited mode at the beginning of the game. |

---

## 📜 License
This project is licensed under the MIT License.

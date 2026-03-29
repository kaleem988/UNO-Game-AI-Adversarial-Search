# 1. Card Class

class Card:
    COLORS = ["Red", "Blue", "Green", "Yellow"]
    SPECIALS = ["Skip"]

    def __init__(self, color, value):
        self.color = color      # Red, Blue, Green, Yellow
        self.value = value      # 0-9 or Skip

    def is_special(self):
        return self.value == "Skip"

    def matches(self, other):
        #True if this card can be played on top of `other`.
        return self.color == other.color or self.value == other.value

    def __repr__(self):
        return f"{self.color} {self.value}"

    def __eq__(self, other):
        return isinstance(other, Card) and self.color == other.color and self.value == other.value

    def __hash__(self):
        return hash((self.color, self.value))



# 2. Deck Generator

def build_deck():
    deck = []
    for color in Card.COLORS:
        for num in range(10):          # 0-9
            deck.append(Card(color, num))
            deck.append(Card(color, num))  # two of each
        deck.append(Card(color, "Skip"))
        deck.append(Card(color, "Skip"))
    random.shuffle(deck)
    return deck



# 3. Legal Move Generator

def get_valid_moves(hand, top_card):
    """Return list of (index, card) tuples that are playable."""
    return [(i, card) for i, card in enumerate(hand) if card.matches(top_card)]
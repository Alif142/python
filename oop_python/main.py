SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        if SUITS.index(self.suit) == SUITS.index(other.suit) and RANKS.index(
            self.rank
        ) == RANKS.index(other.rank):
            return True
        else:
            return False

    def __lt__(self, other):
        return (
            SUITS.index(self.suit) < SUITS.index(other.suit)
            and RANKS.index(self.rank) < RANKS.index(other.rank)
        ) or (
            SUITS.index(self.suit) > SUITS.index(other.suit)
            and RANKS.index(self.rank) < RANKS.index(other.rank)
        )

    def __gt__(self, other):
        return (
            SUITS.index(self.suit) > SUITS.index(other.suit)
            and RANKS.index(self.rank) > RANKS.index(other.rank)
        ) or (
            SUITS.index(self.suit) < SUITS.index(other.suit)
            and RANKS.index(self.rank) > RANKS.index(other.rank)
        )

    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"

from BlackJack.Deck import Deck

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += Deck.values[card.rank]

    def adjust_for_aces(self):
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())
print(test_player.value)

for card in test_player.cards:
    print(card)
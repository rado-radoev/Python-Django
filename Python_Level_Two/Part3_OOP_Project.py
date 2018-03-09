#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

# Create a deck that has 4 card of each SUITE
# shuffle the deck of Cards
# split the deck in half

# my_cards = [(r,s) for r in RANKS for s in SUITE]

# mycards = []
# for r in RANKS:
#     for s in SUITE:
#         mycards.append[(s,r)]

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        print("Creating new ordered deck")
        self.all_cards = [(r,s) for r in RANKS for s in SUITE]

    def shuffle(self):
        print("Shuffelin deck")
        shuffle(self.all_cards)

    def spli_in_half(self):
        return (self.all_cards[:26], self.all_cards[26:])

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove(self):
        return self.cards.pop()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove()
        print("{} has placed {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove)
            return war_cards

    def still_has_cards(self):
        """
        Return true if player still has cards left
        """
        return len(self.hand.cards) != 0

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Create new deck and split in spli_in_half
deck = Deck()
deck.shuffle()
half1, half2 = deck.spli_in_half()

# Create two players
computer = Player("computer", Hand(half1))

name = input("What is your name?")
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_cards() and computer.still_has_cards():
    total_rounds += 1
    print("Time for new round")
    print("hre are the current standings")
    print(user.name + " has the count: "+str(len(user.hand.cards)))
    print(computer.name + " has the count: "+str(len(computer.hand.cards)))
    print("play a card")
    print("\n")

    table_cards = []

    comp_card = computer.play_card()
    user_card = user.play_card()

    table_cards.append(comp_card)
    table_cards.append(user_card)

    # compare the ranking in the tuple
    if comp_card[1] == user_card[1]:
        war_count = 1
        print("WAR")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(computer.remove_war_cards())

        if RANKS.index(comp_card[1]) < RANKS.index[user_card[1]]:
            user.hand.add(table_cards)
        else:
            computer.hand.add(table_cards)
    else:
        if RANKS.index(comp_card[1]) < RANKS.index[user_card[1]]:
            user.hand.add(table_cards)
        else:
            computer.hand.add(table_cards)

print("Game over, number of rounds: " + str(total_rounds))
print("a war happened " + str(war_count)+ " times")

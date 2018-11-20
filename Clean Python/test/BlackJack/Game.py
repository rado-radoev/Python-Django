from BlackJack.Hand import Hand
from BlackJack.Deck import Deck
from BlackJack.Chips import Chips

playing = True

"""
Function to take bets
"""
def take_bet():
    bet_placed = False

    while not bet_placed:
        try:
            bet = int(input("Enter bet amount: "))

            if Chips.available_chips() >= bet:
                bet_placed = True
                print("Bet allowed")
            else:
                print("Bet not allowed. Not enough chips")
        except:
            print("Only integers are accepted")


def hit(deck, hand):
    card_pulled = Deck.deal()
    Hand.add_card(card_pulled)
    Hand.adjust_for_aces()
    return Hand

def hit_or_stand(deck, hand):
    global playing

    is_choise_made = False

    while not is_choise_made:
        choice = input("Hit or Stand?").lower()
        if (choice == "hit"):
            hit(deck, hand)
            playing = True
            is_choise_made = True
        elif (choice == "stand"):
            playing = False
            is_choise_made = True
        else:
            print("Please choose between \"Hit\" and \"Stand\'")


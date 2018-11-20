from BlackJack.Hand import Hand
from BlackJack.Deck import Deck
from BlackJack.Chips import Chips

playing = True

"""
Function to take bets
"""
def take_bet(chips):
    bet_placed = False

    while not bet_placed:
        try:
            chips.bet = int(input("Enter bet amount: "))

            if chips.bet < chips.total:
                bet_placed = True
                print("Bet allowed")
            else:
                print("Bet not allowed. Not enough chips")
        except:
            print("Only integers are accepted")


def hit(deck, hand):
    card_pulled = deck.deal()
    hand.add_card(card_pulled)
    hand.adjust_for_aces()

def hit_or_stand(deck, hand):
    global playing

    is_choise_made = False

    while not is_choise_made:
        choice = input("Hit or Stand?").lower()
        if (choice == "hit"):
            print("Playing")
            hit(deck, hand)
            playing = True
            is_choise_made = True
        elif (choice == "stand"):
            print("Player stands. Dealer is playing.")
            playing = False
            is_choise_made = True
        else:
            print("Please choose between \"Hit\" and \"Stand\'")

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden> ")
    print("", dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep="\n ")

def show_all(player, dealer):
    print ("\nDealer's Hand: ", *dealer.cards, sep="\n ")
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("Playe's Hand =", player.value)


def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.loose_bet()

def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.loose_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.win_bet()

def push(pleayer, dealer):
    print("Dealer and Player tie! It's a push.")

def game_on():
    global playing
    while True:
        # Print an opening statement
        print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
        Dealer hits until she reaches 17. Aces count as 1 or 11.')

        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Set up the Player's chips
        player_chips = Chips() # Default is 100

        # Prompt player for bet
        take_bet(player_chips)

        # Show cards (one of dealer cards is hidden)
        show_some(player_hand, dealer_hand)

        while playing:
            # Prompt for player to hit or stand
            hit_or_stand(deck, player_hand)

            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

        # if Player hasn't busted play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

                # Show all cards
                show_all(player_hand, dealer_hand)

                # Run different winning scenarios
                if dealer_hand.value > 21:
                    dealer_busts(player_hand, dealer_hand, player_chips)
                elif dealer_hand.value > player_hand.value:
                    dealer_wins(player_hand, dealer_hand, player_chips)
                elif dealer_hand.value < player_hand.value:
                    player_wins(player_hand, dealer_hand, player_chips)
                else:
                    push(player_hand, dealer_hand)


        # Inform Player of their chips total
        print ("\nPlayer's winning stand at: ", player_chips.total)

        new_game = input("Would you like to play another hand? Enter 'y' or 'n'")

        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    game_on()
import random


# Asks user to start the game
def main():
    Start = input("Would you like to play a hand of blackjack? (Type Y for yes or N for no) :")
    if Start.upper() == 'Y':
        print('Yes')
        continue_game()
    else:

        print("Thank you for stopping by!")


# Function to be called to deal cards individually
def deal():
    cards = ['One', 'Two', 'Three', 'Four', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen',
             'King', 'Ace']
    return random.choice(cards)


# Calls the deal function to create both hands sends values to be counted once user decides they are satisfied with
# their hand then checks if either player or dealer has gone bust and if not sends the hands to be compared
def continue_game():
    option = ""
    hand = [deal(), deal()]
    dealerHand = [deal(), deal()]
    show_cards(hand)

    while option.upper() != 'STAY':
        option = input("type Hit for another card, type Stay to stay :")
        if option.upper() == 'HIT':
            hand.append(deal())
            show_cards(hand)

        else:
            handValue = count_cards(hand)

    dealerItems = dealer(dealerHand)
    if dealerItems[0] > 21:
        print("The dealer went bust you won")
    elif handValue > 21:
        print('You went bust the dealer won')
    else:
        compare_hands(handValue, dealerItems[0])

    print('Your Final hand is: ', hand,"The dealer's final hand is: ", dealerItems[1])
    anotherHand = input('Would you like to play another hand type Y for yes or N for no: ')
    if anotherHand.upper() == 'Y':
        continue_game()


# Shows the player's hand to them when called
def show_cards(hand):
    print("Your hand is now :")
    print(hand)


# Takes a hand as input in list form and returns the number which the cards add up too
def count_cards(hand):
    ace_check = False
    hand_value = 0
    card_values = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
                   'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
    for i in range(0, (len(hand))):
        hand_value += card_values[hand[i]]
        if hand[i] == 'Ace':
            ace_check = True
    if hand_value > 21 and ace_check == True:
        hand_value = hand_value - 10
        return hand_value

    else:
        return hand_value


# Compares hands if neither party has gone bust
def compare_hands(handValue, dealerValue):
    if handValue > dealerValue:
        print('Congradulations you won')

    elif handValue < dealerValue:
        print("Dealer wins this hand")

    elif handValue == dealerValue:
        print('Its a tie')


# provides dealer hand with some logic for when to deal a third card will add functionality for more later
def dealer(dealerHand):
    dealerValue = count_cards(dealerHand)
    if dealerValue < 13:
        dealerHand.append(deal())
        dealerValue = count_cards(dealerHand)

    dealerItems = [dealerValue,dealerHand]
    return dealerItems


main()

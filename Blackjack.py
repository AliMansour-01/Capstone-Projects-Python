#blackjack capstone project

import random
from Blackjack_art import logo

def clear():
    print("\n" * 100)
def deal_card():
    card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    return random.choice(card)

def calculate_scores(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user, computer):
    if user == computer:
        return "It's a draw"
    elif computer == 0:
        return("Lose, opponent has a blackjack")
    elif user == 0:
        return("Win with a blackjack")
    elif user > 21:
        return("you went over, you  loser!")
    elif computer > 21:
        return("Dealer went over, you win!")
    elif user > computer:
        return("You win!")
    else:
        return "You lose!"

def play_game():

    user_cards = []
    comp_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not game_over:

        user_score = calculate_scores(user_cards)
        comp_score = calculate_scores(comp_cards)

        print(f" Your cards: {user_cards}, current score: {user_score} ")
        print(f" Your cards: {comp_cards}, current score: {comp_score} ")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            user_input = input("Type 'hit' to get another card, and 'stand' to pass: \n")

            if user_input == 'hit':
                user_cards.append(deal_card())
            else:
                game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_scores(comp_cards)
    print(f" Your Final Hand: {user_score} ")
    print(f" Dealer's Final Hand: {comp_score} ")
    print(compare(user_score, comp_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    print(logo)
    play_game()


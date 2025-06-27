import art
import random


def deal_card():
    """Returns a randomly chosen card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(card_list):
    """Calculates the score by summing all values in the provided list and checks if the user
     or computer has a Blackjack, also checks if either of them have gone above 21 in their score
     and have Ace in their hand, in which case it replaces it by removing the Ace card and appends
     1 into the list"""
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0

    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)

    return sum(card_list)

def compare(score_of_user ,score_of_computer):
    """Checks the user score and computer score against the rules of the games
    and returns the result of the game"""
    if score_of_user == score_of_computer:
        return "Its a draw 🙃"
    elif score_of_computer == 0:
        return "Its a blackjack for computer, you lose 😱"
    elif score_of_user == 0:
        return "You win a Blackjack! Great job 😎"
    elif score_of_user > 21:
        return "You went over 21 so you lose!😆"
    elif score_of_computer > 21:
        return "The computer went over 21, so you win!😁🥇"
    elif score_of_user > score_of_computer:
        return "You win🤠"
    else:
        return "You Lose😤"

def play_game():
    """Plays the BlackJack game"""
    print(art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score :{user_score}")
        print(f"Computer's first card: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_user_deal= input("Type 'y' to get another card, type 'n' to pass: ")
            if should_user_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score !=0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand:{user_cards}, your final score:{user_score}")
    print(f"Computer's final hand:{computer_cards}, computer's final score:{computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play the BlackJack Game ? Type 'y' to play and Type 'n' to quit: ") == "y":
    print("\n"*20 )
    play_game()



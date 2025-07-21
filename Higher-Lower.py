#import required modules
import art
import random
from game_data import data

def format_account(account):
    """Takes an account as input and returns its printable format"""
    account_name = account["name"]
    account_desp = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desp}, from {account_country}"

def check_answer(user_guess, followers_of_a, followers_of_b):
    """ Takes in the user guess and followers counts from both the accounts to
        compare them and return if they are right or wrong in their guess"""
    if followers_of_a > followers_of_b:
        return user_guess == "a"
    else:
        return user_guess == "b"


print(art.logo)
score = 0
continue_game = True
account_b=random.choice(data)

# Make the game repeatable
while continue_game:
    # Generate a random account from game data
    # Make account at position B become the next account at position A
    account_a=account_b
    account_b=random.choice(data)

    if account_b==account_a:
        account_b=random.choice(data)

    print(f"Compare A: {format_account(account_a)}.")
    print(art.vs)
    print(f"Compare B: {format_account(account_b)}.")


    #Ask user for a guess
    guess = input("Who has more followers?Type 'A' or 'B': ").lower()
    # Clear the screen by printing some blank lines through new line character
    print("\n"*20)
    #display logo
    print(art.logo)

    #Check if user is correct
    ## Get follower count of each account
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    is_right = check_answer(user_guess=guess,followers_of_a=a_followers,followers_of_b=b_followers)


    # Give the user feedback on their guess
    if is_right:
        # Keep track of current score
        score+=1
        print(f"You're right! Current score:{score}")
    else:
        print(f"Sorry, that's wrong! Final score:{score}")
        continue_game=False




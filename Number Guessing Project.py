#TODO 1: import and print the logo

#declaring global variables helps to modify code easily just by changing these variables.
FOR_HARD = 5
FOR_EASY = 10

def start_game():
    """starts the number guessing game"""
    import art
    print(art.logo)

    #TODO 2:initialize the game by saying a welcome note and range of the number
    print("Welcome to this game of guessing the number:) ")
    print(" I am thinking of a number between 1 and 100.")

    #TODO 3:Generate a random number between 1 and 100
    import random
    generated_num = random.randint(1,100)

    #TODO 4: ask the user for difficulty level and assign number of guess based on it
    difficulty = input("Choose a difficulty.Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        guesses = FOR_EASY
    elif difficulty == 'hard':
        guesses = FOR_HARD
    else:
        print("You choose an invalid entry so click on the run button to start again!")
        return

    #TODO 5: write a function that takes number of guesses as input and plays the game until all guesses are exhausted.
    def play_game(num_of_guesses, right_ans):
        """Takes the number of guesses and right answer as input based on difficulty
           level and randomly generated number respectively.Then allows the user to guess the
           number based on number of guesses they got - user wins if guesses correctly else loses!"""
        while num_of_guesses != 0:
            if num_of_guesses > 1:
                print(f"You have {num_of_guesses} attempts remaining to guess correctly!")
            else:
                print("This is your last chance! Good luck ")
            make_guess = int(input("Make a guess: "))
            num_of_guesses -= 1
            if make_guess == right_ans:
                print(f"You Got it, the answer was {right_ans}!")
                return
            elif num_of_guesses == 0:
                print(f"Oops the right answer was {right_ans}, You lose!")
                return
            elif make_guess > right_ans:
                print("Too high.")
                print("Guess again!")
            else:
                print("Too low.")
                print("Guess again!")

    play_game(num_of_guesses=guesses,right_ans=generated_num)

start_game()

"""So this was my version of the game but we could also optimize it more 
   by writing functions for comparison of right answer and generating a random number.
"""



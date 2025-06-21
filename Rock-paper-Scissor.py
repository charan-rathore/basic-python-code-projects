rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
options = [rock, paper , scissors]
user = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors\n"))
print("you chose:")
print(options[user])
comp = random.randint(0,2)
print("computer chose: ")
print(options[comp])

if user>=3 or user<0:
    print("your choice is invalid, so you lose!")
elif options[user] == options[comp]:
    print("its a draw")
elif user == 0 and comp == 2:
    print("you win")
elif comp==0 and user ==2:
    print("you lose")
elif comp > user:
    print("you lose")
elif user > comp:
    print("you win")


# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo
print(logo)

list_of_bidders = {}
to_continue = True


def comapre_bids(bidder_list):
    max_bid = 0
    winner = ""
    for bidder in bidder_list:
        if bidder_list[bidder] > max_bid:
            max_bid = bidder_list[bidder]
            winner = bidder
    print(f"highest bid is ${max_bid} and winner is {winner} ")

while to_continue:
    name = input("enter your name : ")
    bid = int(input("What is your bid ?: $"))
    list_of_bidders[name] = bid
    other_user = input("Are there any other user who want to bid? Type 'yes' or 'no'.\n ").lower()
    if other_user == "no":
        to_continue = False
        comapre_bids(list_of_bidders)
    elif other_user == "yes":
        print("\n" * 20)


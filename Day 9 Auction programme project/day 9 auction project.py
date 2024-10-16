import os
from art import logo  # Assuming you have an art.py file with the logo

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    return winner, highest_bid

print(logo)  # Display the logo from art.py

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    price = float(input("What is your bid?: $"))
    bids[name] = price
    
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        bidding_finished = True
    elif should_continue == "yes":
        clear_screen()

winner, winning_bid = find_highest_bidder(bids)
print(f"The winner is {winner} with a bid of ${winning_bid}")
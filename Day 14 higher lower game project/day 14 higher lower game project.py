from art import logo
from art import vs
from game_data import data
import random
import os

# Account format 
def account_format(account):
    '''Format the account data'''
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f'{account_name}, a {account_description}, from {account_country}'

# Check if the user guess is correct
def check_answer(choose, a_follower, b_follower):
    '''Takes the user guess and follower count, and returns if they got it right'''
    if choose == 'a' and a_follower > b_follower:
        return True
    elif choose == 'b' and b_follower > a_follower:
        return True
    else:
        return False

# Function to clear the screen
def clear_screen():
    '''Clears the terminal screen'''
    os.system('cls' if os.name == 'nt' else 'clear')

# Main game logic
def play_game():
    print(logo)
    score = 0
    continue_game = True
    
    # Generate random accounts
    account_a = random.choice(data)
    account_b = random.choice(data)
    
    while continue_game:
        account_a = account_b  # Set B to A
        account_b = random.choice(data)
        
        # Make sure A and B are not the same
        while account_a == account_b:
            account_b = random.choice(data)
        
        clear_screen()  # Clear the screen at the start of each round
        print(f"Score: {score}\n")  # Display score at the top
        print(logo)
        print(f"Compare A: {account_format(account_a)}")
        print(vs)
        print(f"Against B: {account_format(account_b)}")
        
        # User input
        choose = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']
        
        # Check if the user is correct
        if check_answer(choose, a_follower_count, b_follower_count):
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            continue_game = False
            print(f"Sorry, that's wrong. Final score: {score}.")

# Run the game
play_game()

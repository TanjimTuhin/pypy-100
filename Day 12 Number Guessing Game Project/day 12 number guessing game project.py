from art import logo
print(logo)
#choosing random number from 1 to 100
print('Welcome to the gussing Game!')
print("I'm thinking of number between 1 to 100")
import random
answer=random.randint(1,100)
print(f'pssst,the correct answer {answer}')



easy_level=10
hard_level=5
#make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":        
        return easy_level
    elif level == "hard":        
        return hard_level



#Function to check user's huess against actual number 
def check_answer(guess,answer,turns):
    if guess>answer:
        print('Too high')
        return turns-1
    elif guess<answer:
        print('Too low')
        return turns-1
    else:
        print(f'You got it!,the answer is {answer}')


#track the number of turns and reduce by 1 if they get it wrong


#let the user guess a number 
turns=set_difficulty()

#Repeat the guessing functionality if they get it wrong
guess=0
while guess!=answer:
    print(f'You have {turns} attempt to guess the number')
    guess=int(input('Make a guess:'))
    turns=check_answer(guess,answer,turns)
    if turns==0:
        print('You have run out of guesses, you lose')
        break


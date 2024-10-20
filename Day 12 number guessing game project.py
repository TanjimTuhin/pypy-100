print('Welcome to the Number Guessing Game')
import random


hard=True
while hard:
    loop_count=0
    total_count=10
    computer_guess=random.randint(1,101)
    while loop_count<total_count:
        user_guess = int(input('Guess a number between 1 and 100: '))

        if user_guess != computer_guess:
            if user_guess<computer_guess:
                print('Too low')
            elif user_guess>computer_guess:
                print('Too high')
        else:
            print('Congratulations, you guessed the number correctly!')
        loop_count+= 1
        remain=total_count-loop_count
        print(f'you have {remain} attempts remaining to guess the number')
        if remain==0:
            print('Game Over!!!')
            hard=False

 # Ask if the user wants to play again after the game ends
play_again = input("Do you want to play again? (yes/no): ").lower()
if play_again != 'yes':
        hard = False
        print('Thank you for playing!')
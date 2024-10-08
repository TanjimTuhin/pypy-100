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

#Write your code below this line 👇

import random

print('What do you choose? Type 0 for Rock,1 for Paper , 2 for Scissors.')
your_choice=int(input('Your Choice'))

computer_choice=random.randint(0,2)

if your_choice==0:
    print(rock)
    if computer_choice==0:
        print(rock)
        print('computer choose rock. It\'s a Tie')
    elif computer_choice==1:
        print(paper)
        print('computer choose paper. Computer Win')
    else :
        print(scissors)
        print('computer choose Scissors. You Win!')  
if your_choice==1:
    print(paper)
    if computer_choice==0:
        print(rock)
        print('computer choose rock. You Win!')
    elif computer_choice==1:
        print(paper)
        print('computer choose paper.It\'s a Tie')
    else :
        print(scissors)
        print('computer choose Scissors.Computer Win')  
else:
    print(scissors)
    if computer_choice==0:
        print(rock)
        print('computer choose rock. Computer Win')
    elif computer_choice==1:
        print(paper)
        print('computer choose paper.You Win!')
    else :
        print(scissors)
        print('computer choose Scissors.It\'s a Tie')                


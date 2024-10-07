print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

combined_name=name1+name2
lowercase=combined_name.lower()
t=lowercase.count('t')
r=lowercase.count('r')
u=lowercase.count('u')
e=lowercase.count('e')
first_disit=t+r+u+e

l=lowercase.count('l')
o=lowercase.count('o')
v=lowercase.count('v')
e=lowercase.count('e')
second_disit=l+o+v+e

score=int(str(first_disit)+str(second_disit))

if(score<10)or(score>90):
 print(f'Your score is {score}, you go togsther like coke and mentos.')
elif (50>=score>=40):
 print(f'Your score is {score}, you are alright together.')
else:
 print(f'Your score is {score}.')

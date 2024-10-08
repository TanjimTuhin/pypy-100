name_string = input("Enter names separated by commas then space: ")
name = name_string.split(", ")


#name = [n.strip() for n in name_string.split(",")]
#//Split the input string by "," and strip extra spaces around each name

import random
item=len(name)



random_choice=random.randint(0,item-1)

person_who_will_pay=name[random_choice]

print( person_who_will_pay +' is going to buy the meal today!')
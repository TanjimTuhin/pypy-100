enemies =1

def increase_enemies():
   # global enemies  #make this emeny global  
    #enemies+=2
    print(f'enemies inside function:{enemies}')
    return enemies+1
enemies=increase_enemies()

print(f'enemies outside function:{enemies}')
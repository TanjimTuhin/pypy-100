game_level=3
enemies=['skeleton','zombie','alien']

def game():
    if game_level<5:
        new_enemy=enemies[0]

    print(new_enemy) #in block -> will work

print(new_enemy) #out of block -> won't work
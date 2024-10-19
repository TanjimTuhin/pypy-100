###local scope

def drink_potion():
    print("You drink a potion and feel invigorated.")
    potion_strength=2 #(local scope)
    print(potion_strength) #accessable
    return "invigorated"
drink_potion()
#print(potion_strength) #not accessible 


###global Scope

player_health=10 #global scope
def game():#namespace
    def take_damage(damage):
        global player_health
        player_health=damage
        print(f"Player health is {player_health}")
        #player_health=10 #local scope       
    take_damage(player_health)
print(f"Player health is {player_health}")
#player_health=10 #global scope

def assign(player):
    print(f"Welcome {player}")


trial=1
while (trial<=2):
    print("1. Jack \n2. Manu\n")
    player=input("Choose your player?")
    if player=="Jack":print("your powers are speed and flight") 
    elif player=="Manu":print("your powers are invisibility and you can move objects with your mind")
    else:
        trial+=1
        continue
    
    
print(f"hello {player}")
assign(player)


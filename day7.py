import random

word = random.choice(world_list)
word_to_show = []

for letter in word:
    word_to_show.append("_")

lifes = 6
used=[]
while lifes != 0:
    
    print(word_to_show)
    print(f"Lifes: {lifes}")
    print(f"Used letter: {used}")
    player_letter = input("Give me letter: \n")

    i=0
    for letter in word:
        if letter == player_letter:
            word_to_show[i]= player_letter
        i+=1

    if word.find(player_letter) == -1  and player_letter not in used:
        lifes -=1
        used.append(player_letter)

    if word_to_show.count("_")<1:
        print(f"YOU WIN!!! {word}")
        break
    elif lifes == 0:
        print(f"GAME OVER!! {word}")
        break  

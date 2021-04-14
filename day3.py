print("Welcome to Treasure Island. Your Mission is to find the treasure.")
ch_1 = input("You are on island, in right you see something moving. In left you see boat. left or right?\n")
if ch_1 == "right":
    print("It was tiger. You get eaten. Game Over")
elif ch_1 == "left":
    ch_2 = input("Boat is empty. You can escape from island. You can swim or wait for miracle. swim or wait?\n")
    if ch_2 == "swim":
        print("You don't found treasure. GAME OVER")
    elif ch_2 == "wait":
        ch_3 = input("From heaven fall down 3 doors. You have to choose? red, blue or yellow?\n")
        if ch_3 == "red":
            print("Behind door is fire. You Dead")
        elif ch_3 == "blue":
            print("From door came out shark and eat you. GAME OVER")
        elif ch_3 == "yellow":
            print("YOU FOUND TREASSURE!!")
from random import randint

choices = ["rock", "paper", "scissors"]

player = int(input("Choice: 0:rock 1:paper 2:scissors\n"))
while player >= 3 or player <=0:
    player = int(input("ZŁA CYFRA, podaj ponownie.\n"))

computer = randint(0,2)

print(f"Computer: {choices[computer]}")
print(f"Player: {choices[player]}\n")

if player == 0 and computer == 2:
    print("WIN")
elif player == 2 and computer == 0:
    print("LOSE")
elif player > computer:
    print("WIN")
elif player < computer:
    print("LOSE")
elif player == computer:
    print("TIE")
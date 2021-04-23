from replit import clear
bidders = {}

print("Hello in auction")

choice = ""
while choice != "no":
    clear()
    name = input("What's your name?\n")
    price = int(input("What is your price?\n"))
    bidders[name] = price
    choice = input("Any others bidders? yes/no\n")
winner_price = max(bidders.values())

for bidder in bidders:
    if bidders.get(bidder) == winner_price:
        winner = bidder
print(f"Winner is {winner} with ${winner_price}")


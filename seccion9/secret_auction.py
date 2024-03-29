import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


from art import logo

print(logo)

bids = {}

biding_finished = False

def find_highest_bidder(bidding_record):
    # {"Carlos": 123, "Angela": 341}
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")        

while not biding_finished:
    name = input("What's your name: ")
    price = int(input("What's your bid: $"))
    bids[name] = price

    should_continue = input("Are there any other bidders= Type 'yes or no'.\n")

    if should_continue == "no":
        biding_finished = True
        find_highest_bidder(bids)
    elif should_continue== "yes": 
        clear_console()






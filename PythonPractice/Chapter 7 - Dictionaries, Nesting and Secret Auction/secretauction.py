print("Welcome to the secret auction program.")


bidding = True
bidder_dict = {}
win_bid_amount = 0
win_bid = ""

while bidding:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidder_dict[name] = bid
    bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    if bidders == "yes":
        print("\n" * 20)
    else:
        bidding = False
        for key in bidder_dict:
            if bidder_dict[key] > win_bid_amount:
                win_bid_amount = bidder_dict[key]
                win_bid = key
        print(f"{win_bid} won with ${win_bid_amount}")



print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12 or 15? "))
split = float(input("How many people to split the bill? "))
split_amount = round(total*(1+(tip/100))/split,2)
print("Each person should pay: $" + str(split_amount))
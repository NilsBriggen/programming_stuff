print("Welcome to Python Pizza deliveries!")
size = input("What size pizza do you want? S, M or L ")
pepperoni = input("Do you want pepperoni? Y or N ")
cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M" or size == "L":
        bill += 3

if cheese == "Y":
    bill += 1

print(f"Your pizza costs {bill} Fr.")
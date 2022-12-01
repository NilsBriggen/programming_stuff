print("Welcome to the tip calculator")
bill = input("How much was the bill? \nFr.")
persons = input("how much Persons split the bill?\n")
tip = input("How much tip would you like to add? 10, 12 or 15 percent?\n")

finaltip = int(tip) / 100 + 1
print(finaltip)
finalbill = round(float(bill) * float(finaltip) / int(persons), 2)
finalbill = "{:.2f}".format(finalbill)
print(f"Each of you would have to pay: {finalbill}Fr.")
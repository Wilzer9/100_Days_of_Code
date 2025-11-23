print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
valor_gorjeta = int(bill * (tip/100))
people = int(input("How many people to split the bill? "))
total = round((valor_gorjeta+bill) / people, 2)

print(f"Each person should pay: ${total}")
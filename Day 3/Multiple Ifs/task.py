print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 5

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        print("Please pay $12.")
        bill = 12
    photo = str(input("Want photos ?"))
    if photo == "yes":
        bill += 3
        print(f"O total com a fota fica ${bill}")
    else:
        print(f"total ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")

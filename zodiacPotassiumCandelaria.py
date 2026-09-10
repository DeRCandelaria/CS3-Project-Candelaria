ch_sign = [
    "Monkey",
    "Rooster",
    "Dog",
    "Pig",
    "Rat",
    "Ox",
    "Tiger",
    "Rabbit",
    "Dragon",
    "Snake",
    "Horse",
    "Goat",
]

year = int(input("Enter your birth year: "))

if year < 1900:
    print("Invalid year, it should not be earlier than 1900. Try again.\n")
else:
        ch_zodiac = ch_sign[year % 12]
        print(f"Your Chinese zodiac sign is {ch_zodiac}")




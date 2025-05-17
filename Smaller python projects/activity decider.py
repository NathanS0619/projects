mood = input("Are you happy or tired today? ")
weather = input("Is it rainy or sunny today? ")

if mood == "happy" and weather == "sunny":
    print("Go for a hike!")
elif mood == "happy" and weather == "rainy":
    print("Relax indoors.")
elif mood == "tired" and weather == "sunny":
    print("Go for a SHORT hike.")
elif mood == "tired" and weather == "rainy":
    print("Relax indoors.")
else:
    print("Invalid entry!")
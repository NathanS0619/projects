import random
num_list = range(1, 10)
random_num = random.choice(num_list)

while True:
    guess = int(input("Guess the number 1-10: "))

    if guess == random_num:
        print("Congratulations! You guessed correctly!")
        break
    elif guess < random_num:
        print("Too low!")       
    elif guess > random_num:
        print("Too high!")
    else:
        print("Invalid entry!")
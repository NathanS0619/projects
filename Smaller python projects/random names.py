import random
first_names = ("Christian", "Dylan", "Travis", "Katelyn")
last_names = ("Sachs", "Katina", "Peck", "Mehner")

random_full_name = random.choice(first_names) + " " + random.choice(last_names)

print(random_full_name)
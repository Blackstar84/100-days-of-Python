import random
names_string = "Angela, Ben, Jenny, Michael, Cloe"
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

long_items = len(names)

# Generate random numbers between 0 and the las index
random_name = random.randint(0, long_items -1)
print(f"{names[random_name]} is going to buy the meal today!")
import random
import my_module

#random_integer = random.randint(1, 10)

#print(my_module)

random_float = random.random()

#print(random_float)

# decimal random entre 0 y 5
random_decimal = random.uniform(0, 5)

#print(random_decimal)

# Otra opción es modificar nuestro random float y multiplicarlo por 5
random_float_decimal = random.random() * 5
#print(random_float_decimal)

love_score = random.randint(1, 100)

print(f"Your love score is {love_score}")
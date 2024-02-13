# El problema inicial lo teníamos en la primera condición, para ser fizzbuzz tiene que ser divisible por 3  y por 5
# en nuestro código lo teníamos de la siguiente manera:
# if number % 3 == 0 or number % 5 == 0:
# Como podemos ver tiene or en lugar de and, ese es el primer error, luego tenía if uno bajo el otro en lugar de elif

# Este es el código original con los errores que debemos corregir
# Target is the number up to which we count
# target = int(input())
# for number in range(1, target + 1):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])




target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
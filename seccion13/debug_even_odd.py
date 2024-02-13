# Which number do you want to check?
number = int(input())
# En lugar de preguntar estabamos intentando asignar un resultado, faltaba un = más debía ser
# if number % 2 == 0 
# if number % 2 = 0:
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
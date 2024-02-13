# Which year do you want to check?

# El problema estaba en que no estabamos convirtiendo a int el año que ingresaba el usuario
# por tanto intentaba comparar un string con un int por ello el error
# year = int(input())
# con agregarle la conversión a int solucionamos el código y ya funciona correctamente
year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
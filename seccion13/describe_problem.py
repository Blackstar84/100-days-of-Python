############DEBUGGING#####################

# # Describe Problem
# El rango va del 1 al 19 no incluyendo al 20, por ese motivo no llega a imprimir
# Ya que el último número del range no es incluído, sería del 1 al 19 en este caso
# Se modifica el rango a 21 para que tome el 20 y así pueda ejecutarse ese print
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()



# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# # El error se produce ya que nuestra lista tiene un rango de 0 a 5
# dice_num = randint(1, 6)
# Solucionamos poniendo el rango de 0 a 5 en lugar de 1 al 6
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# Si el año es igual a 1994 no va a entrar en ninguno de los if
# Para solucionar esto pondremos que si el año es menor o igual a 1994 millenial o mayor o igual a 1994 y que imprima Gen Z
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# Aquí da error porque no tenemos identación en el print que se encuentra dentro del if
# otro error es que tomamos el input de age sin convertirlo a int e intentamos comparar un string con un int
# para ello ponemos dentro de un int el input donde preguntamos por la edad
# age = int(input("How old are you?"))

# # Aquí en el print faltaba la f para poder utilizar el fstring y poder meter variables dentro del print 
# if age > 18:
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# El error es que estamos teniendo doble igual word_per_page == int(input("Number of words per page: ")) en lugar de 
# un sólo igual que es de asignación word_per_page = int(input("Number of words per page: "))
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"pages = {pages}")
# print(f"word_per_page = {word_per_page}")
# print(total_words)

# #Use a Debugger
# El problema con este código es que el append lo esta haciendo fuera del ciclo for
# por ese motivo sólo el último item de la lista es agregado a la nueva lista b_list
# Para solucionar esto, damos identación al append para que quede dentro del ciclo for
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        # Al meter aquí ya vamos a tener nuestra lista con los números multiplicados por dos
        b_list.append(new_item)
    # b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])
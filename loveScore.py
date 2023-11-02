name1 = input("Ingrese el nombre de la primera persona: ")
name2 = input("Ingrese el nombre de la segunda persona: ")

# Combina los nombres y convierte todo a letras minúsculas
combined_names = (name1 + name2).lower()

# Contar la ocurrencia de las letras en "true" y "love"
t_count = combined_names.count("t")
r_count = combined_names.count("r")
u_count = combined_names.count("u")
e_count = combined_names.count("e")

l_count = combined_names.count("l")
o_count = combined_names.count("o")
v_count = combined_names.count("v")

# Calcula el puntaje de amor
love_score = int(str(t_count + r_count + u_count + e_count) + str(l_count + o_count + v_count + e_count))

# Imprime el resultado
print("The Love Calculator is calculating your score...")
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
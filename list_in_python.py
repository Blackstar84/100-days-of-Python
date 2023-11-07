states_of_america = ["Delaware", "Pensylvania", "New Jersey", "Georgia"]
# Para acceder directamente podemos hacerlo con el índice
print(states_of_america[0])

# Para modificarlo lo seteamos accediendo al índice y luego establecemos el nuevo valor
states_of_america[1] = "Pensilvania"

print(states_of_america[1])

# Para agregar un nuevo elemento al final de la lista lo hacemos de la siguiente manera

states_of_america.append("Angelaland")
print(states_of_america)

# Extiende la lista agregando varios valores que se definen dentro de los corchetes

states_of_america.extend(["Angelaland2", "Jack Bauer Land"])

print(states_of_america)

# Inserta un elemento en una posición específica

states_of_america.insert(0, "Nuevo")
print(states_of_america)

# Elimina el primer item de la lista que coincida con el valor buscado
states_of_america.remove("Nuevo")
print(states_of_america)

# elimina un elemento especificando una posición

states_of_america.pop(1)
print(states_of_america)



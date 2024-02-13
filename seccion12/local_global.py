""" enemies = 1

def increase_enemies():
    enemies = 2
    print(enemies)


increase_enemies()
print(enemies)     """


# Si por ejemplo queremos ir aumentando en 1 la cantidad de enemigos cada vez que se llama
# a la función, debemos declarar la variable enemies explícitamente como global dentro de la función increase_enemies
# Sólo de esta manera podemos acceder a modificar la variable enemies que fue declarada como global, caso contrario no podríamos
# ir aumentando su valor cada vez que se utilice la función increase_enemies

""" enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()

print(f"enemies outside function: {enemies}") """

enemies = 1

def increase_enemies():
    #print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()

print(f"enemies outside function: {enemies}")


enemies = increase_enemies()

print(f"enemies outside function: {enemies}")


print(enemies)
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Primero que nada verificamos si el frente esta vacío, de ser así nos movemos
while front_is_clear():
    move()
# Luego giramos a la izquierda    
turn_left()

# Aquí entramos hasta que llegemos a la meta
while not at_goal():
    # Si la derecha del robot esta libre giramos a la derecha y nos movemos
    if right_is_clear():
        turn_right()
        move()
    # Si el frente del robot esta libre nos movemos    
    elif front_is_clear():
        move()
    # Caso que la derecha y el frente no estén libres ponemos la dirección del robot a la izquierda    
    else:
        turn_left()            
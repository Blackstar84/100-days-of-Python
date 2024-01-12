# Solución Clase
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Una forma es esta, la otra es usando un for
jump()
jump()
jump()
jump()
jump()
jump()


# Mi solución
while not at_goal():
    jump()

# Solución Clase
while at_goal() != True:
    jump()






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

for step in range(0, 6):
    jump()



# Mi Solución
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def continues_move():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(0, 6):
    continues_move()








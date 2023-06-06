def turn_around():
    turn_left()
    turn_left()
    turn_left()
def cir1():
    turn_left()
    move()
    turn_around()
    move()
    turn_around()
    move()

def jump():
    move()
    cir1()
    turn_left()

for step in range(6):
    jump()
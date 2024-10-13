import pgzrun
import random

WIDTH = 1200
HIGHT = 650

ship = Actor("galaga")
bug = Actor("bug")

ship.pos = (WIDTH//2 , HIGHT-60)

speed= 5

bullets = []
enenmies = []

score = 0

enenmies.append(Actor("bug"))
enenmies[-1].x = 10
enenmies[-1].y = -100

def displayScore():
    screen.draw.text(str(score),(30,50))

def on_key_down():
    if key ==bkeys.SPACE:
        bullets.append(Actor("bullets"))
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y - 50

def update():
    global score
    if keyboard.left:
        ship.x = ship.x - speed
        if ship.x <= 0:
            ship.x = 0

    elif keyboard.right:
        ship.x = ship.x + speed
        if ship.x >= WIDTH:
            ship.x = WIDTH

for bullet in bullets:

    if bullets.y <=0:
        bullets.remove(bullet)
    else:
        bullet.y = bullet.y - 10




    






import pgzrun
import random
WIDTH=500
HEIGHT=500
def draw():
    r=0
    g=random.randint(0,255)
    b=255
    radius=250
    for q in range(25):
        screen.draw.circle((WIDTH//2,HEIGHT//2),radius,(r,g,b))
        radius-=10
        r+=10
        b-=10




pgzrun.go()

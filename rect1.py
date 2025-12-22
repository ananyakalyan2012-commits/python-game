import pgzrun
import random
WIDTH=500
HEIGHT=500
def draw():
    r=0
    g=255
    b=random.randint(0,255)
    width=WIDTH-100
    height=HEIGHT-200
    for i in range(10):
        rect=Rect((0,0),(width,height))
        rect.center=(250,250)
        screen.draw.rect(rect,(r,g,b))
        width-=20
        height-=20
        r+=20
        g-=20









pgzrun.go()

import pgzrun
import random
import time
WIDTH=500
HEIGHT=500
TITLE="bumblebee game"
score=0
game_over=False
bee=Actor("bumblebee")
bee.pos=(300,300)
msg=""
flower=Actor("flower")
flower.pos=("150,430")


def draw():
    screen.blit("background",(0,0))
    flower.draw()
    bee.draw()
    screen.draw.text("Score: "+ str(score),
                     color="black", topleft=(10,10))
    if game_over:
        screen.fill("red")
        global msg
        msg="Time's up! \nYour Final Score:"
        screen.draw.text(msg+str(score),
                         midtop=(WIDTH/2,20),
                         fontsize=50, color="black")

def place_flower():
    flower.x=random.randint(30,(WIDTH-30))
    flower.y=random.randint(30,(HEIGHT-30))

def time_up():
    global game_over
    game_over=True      

def update():
    global score
    if keyboard.left:
        bee.x=bee.x-2
    if keyboard.right:
        bee.x=bee.x+2
    if keyboard.up:
        bee.y=bee.y-2
    if keyborad.down:
        bee.y=bee.y+2

    flower_collected=bee.colliderect(flower)                
    
    if flower_collected==True:
        score=score+5
        place_flower()

clock.schedule(time_up, 60.0)      
    
pgzrun.go()

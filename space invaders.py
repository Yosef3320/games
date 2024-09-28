# importing the moduels
import turtle
import math
import random
import pygame # type: ignore
pygame.mixer.init()



# seting up the screen
wn = turtle.Screen()
wn.setup(width=1.0, height=1.0)  #  We did this
wn.screensize(800, 800) #  we did this
width = wn.window_width() // 2  #  Half width for borders  --> We did this
height = wn.window_height() // 2  #  Half height for borders  --> we did this
wn.bgcolor("black")
wn.title("SPACE INVADERS")
turtle.tracer(2)

#  Optional: Maximize window directly
wn._root.attributes('-fullscreen', True)

# drawing the border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-width, -height)  #  we added this
# border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(width * 2)  #  Move forward by full width --> we did this
    # border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()



score = 0
scorepen = turtle.Turtle()
scorepen.speed(0)
scorepen.color("white")
scorepen.penup()
scorepen.setposition(-800,405)
scorestring = "Score: %s"%score
scorepen.write(scorestring, False, align="left",font=("Arial",23,"normal"))
scorepen.hideturtle()


# creating the player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
# player.setposition(0, -250)
player.setposition(0, -height + 80)  #  Position above the bottom border --> We did this
player.setheading(90)

playerspeed = 15

numberofenemies = 5
enemies = []
for i in range(numberofenemies):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("maroon")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-360,360)
    y = random.randint(260,410)
    #  y = random.randint(-200, height - 50)  #  Position below the top border
    #  x = random.randint()
    enemy.setposition(x,y)

enemyspeed = 2

# create the bullet
bullet = turtle.Turtle()
bullet.color("gold")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bulletspeed = 20

bulletstate = "ready"

# turning left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -width + 20:  #  Adjust to border --> We added this
        x = -width + 20  #  --> we added this
    #  if x < -280:
    #      x = -280
    player.setx(x)

def move_right():
    
    x = player.xcor()
    x += playerspeed
    if x > width - 20:  #  Adjust to border --> we added this
        x = width - 20  #  we added this
    #  if x > 280:
    #      x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "firing"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()
        sound = pygame.mixer.Sound(r"C:\Users\joe\OneDrive\Documents\python\Joe Games\Music files\lazer.mp3")
        sound.play()
def iscolision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
        
def byebye():
    turtle.bye()

# keyboard byndings
turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(fire_bullet,"space")
turtle.onkeypress(byebye,"Escape")

# main game loop
while True:
    if wn._root.winfo_exists():  #  Check if the window exists
        wn.update()
        for enemy in enemies:
            #   move the enemy
            x = enemy.xcor()
            x += enemyspeed
            enemy.setx(x)

            # move the enemy back and down --> we did this whole section
            if enemy.xcor() > width:
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                enemyspeed *= -1

            if enemy.xcor() < -width:
                for e in enemies:
                    y = e.ycor()
                    y -= 40 
                    e.sety(y)
                enemyspeed *= -1
            if iscolision(bullet, enemy):
                bullet.hideturtle()
                bulletstate = "ready"
                bullet.setposition(0, -400)
                x = random.randint(-360,360)
                y = random.randint(260,410)
                enemy.setposition(x,y)
                score += 10
                scorestring = "Score: %s"%score
                scorepen.clear()
                scorepen.write(scorestring, False, align="left",font=("Arial",23,"normal"))
                sound2 = pygame.mixer.Sound(r"C:\Users\joe\OneDrive\Documents\python\Joe Games\Music files\explosion.mp3")
                sound2.play()
            if iscolision(player, enemy):
                sound3 = pygame.mixer.Sound(r"C:\Users\joe\OneDrive\Documents\python\Joe Games\Music files\explosion.mp3")
                sound3.play()
                player.hideturtle()
                enemy.hideturtle()
                print("GAME OVER")
                break
            if enemy.ycor() < -height:
                sound4 = pygame.mixer.Sound(r"C:\Users\joe\OneDrive\Documents\python\Joe Games\Music files\explosion.mp3")
                sound4.play()
                player.hideturtle()
                enemy.hideturtle()
                print("GAME OVER")
                turtle.bye()
                break
            

        #  if enemy.xcor() > 280:
        #      y = enemy.ycor()
        #      y -= 40
        #      enemyspeed *= -1
        #      enemy.sety(y)
        
        #  if enemy.xcor() < -280:
        #      y = enemy.ycor()
        #      y -= 40
        #      enemyspeed *= -1
        #      enemy.sety(y)

        # move the bullet
        if bulletstate == "firing":
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)

        if bullet.ycor() > height: #  --> we did this
        # if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = "ready"
    else:
        break  #  Exit the loop if the window is closed
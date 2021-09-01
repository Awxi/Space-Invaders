import turtle
import os
import math
import random

#set up screen
wn = turtle.Screen()
wn.bgcolor("grey")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")

#Register the shapes
turtle.register_shape("Invader.gif")
turtle.register_shape("Player.gif")

#draw Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set the score to zero
score = 0 

#Draw the score 
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("White")
score_pen.penup()
score_pen.setposition(-290,270)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align ="left", font = ("Arial",14,"normal"))
score_pen.hideturtle()

#create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("Player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15

#choose a n umber of enemies
number_of_enemies = 5
#create an empty list of enemies
enemies =[]

#add enemies to the list
for i in range(number_of_enemies):
    #creating enemies
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("Invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x,y)

    enemyspeed = 4

#weapon
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20

#define bullet state
#ready-ready to fire
#fire- bullet is firing
bulletstate = "ready"

#move player
def move_left():
    x = player.xcor()
    x-= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #declare bullet state as a global if it needs to change
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
        

#keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#Main Game Loop
while True:

    for enemy in enemies:  
        #Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
    
        #Move the enemy back and down
        if enemy.xcor() > 280:
            #move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change direction
            enemyspeed *= -1
        

        if enemy.xcor() < -280:
            #move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change direction of all enemies
            enemyspeed *= -1

        #check for a collision between the bullet and the enemy
        if isCollision(bullet,enemy):
            #reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0,-400)
            #Reset the enemy
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setposition(x,y)
            #update score
            score +=10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align ="left", font = ("Arial",14,"normal"))
            


        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break


    #move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #check the bullet
    if bullet.ycor() > 285:
        bullet.hideturtle()
        bulletstate = "ready"

    #check for a collision between the bullet and the enemy
    if isCollision(bullet,enemy):
        #reset the bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0,-400)
        #Reset the enemy
        enemy.setposition(-200,250)

    if isCollision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("Game Over")
        break




delay = input("Press enter to finish.")
#importing modules
import turtle
import math
#background
wn=turtle.Screen()
wn.bgcolor("black")

#enemy attributes
enemy=turtle.Turtle()
enemy.shape("circle")
enemy.color("yellow")
enemy.speed(40)
enemy.penup()
enemy.setpos(-200,250)

#bullet attributes
bullet=turtle.Turtle()
bullet.shape("circle")
bullet.color("yellow")
bullet.speed(6)
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bulletstate="not shot"

#speed of bullet
bullet_speed=40

    
#beginning score
score=0

#score text
text=turtle.Turtle()
text.color("red")
text.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

#speed of enemy
enemyspeed=2

#spacecraft
bob=turtle.Turtle()
bob.shape("triangle")
bob.color("red")
bob.speed(0)
bob.penup()

bob.left(90)
bob.back(250)


#speed of bob
bobspeed=15

def right():
    #move right
    x=bob.xcor()
    x+=bobspeed
    bob.setx(x)
    
def left():
    #move left
    x=bob.xcor()
    x-=bobspeed
    bob.setx(x)
#shoot    
def shoot():
    global bulletstate
    #changing bulletstate
    if(bulletstate=="not shot"):
        bulletstate="shot"
        x=bob.xcor()
        y=bob.ycor()
        bullet.setpos(x,y+10)
        bullet.showturtle()
    

    
#keyboard bindings
turtle.listen()
turtle.onkey(right,"Right")
turtle.onkey(left,"Left")
turtle.onkey(shoot,"space")

#some game stuff
while True:
    wn.update()
    #enemy movement
    x=enemy.xcor()
    x+=enemyspeed
    enemy.setx(x)
    
    #bullet movement
    y=bullet.ycor()
    y+=bullet_speed
    bullet.sety(y)
    
    #stop bullet
    if(y>275):
        bullet.hideturtle()
        bulletstate="not shot"
        
    #boundary conditions for enemy
    if(enemy.xcor()>280):
        y=enemy.ycor()
        y-=40
        enemyspeed*=-1
        enemy.sety(y)
        
    if(enemy.xcor()<-280):
        y=enemy.ycor()
        y-=40
        enemyspeed*=-1
        enemy.sety(y)
        
    #distance between bob and enemy     
    d=math.sqrt(math.pow(bob.xcor()-enemy.xcor(),2)+math.pow(bob.ycor()-enemy.ycor(),2))
    
    #distance between bob and bullet
    d1=math.sqrt(math.pow(bullet.xcor()-enemy.xcor(),2)+math.pow(bullet.ycor()-enemy.ycor(),2))
    
    if(d1<20):
        #when shot enemy
        enemy.setpos(-200,250)
        score = score+10
        text.clear()
        text.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
    
    if(d<20):
        #when enemy reaches bob
        enemy.setpos(-200,250)
        score = score-10
        text.clear()
        text.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
        
    
    

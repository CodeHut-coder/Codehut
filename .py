import turtle
import math

wn=turtle.Screen()
wn.bgcolor("black")

enemy=turtle.Turtle()
enemy.shape("circle")
enemy.color("yellow")
enemy.speed(40)
enemy.penup()
enemy.setpos(-200,250)

bullet=turtle.Turtle()
bullet.shape("circle")
bullet.color("yellow")
bullet.speed(6)
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bulletstate="not shot"


bullet_speed=40

    

score=0
text=turtle.Turtle()
text.color("red")
text.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

enemyspeed=2

bob=turtle.Turtle()
bob.shape("triangle")
bob.color("red")
bob.speed(0)
bob.penup()

bob.left(90)
bob.back(250)



bobspeed=15

def right():
    x=bob.xcor()
    x+=bobspeed
    bob.setx(x)
    
def left():
    x=bob.xcor()
    x-=bobspeed
    bob.setx(x)
    
def shoot():
    global bulletstate
    if(bulletstate=="not shot"):
        bulletstate="shot"
        x=bob.xcor()
        y=bob.ycor()
        bullet.setpos(x,y+10)
        bullet.showturtle()
    

    

turtle.listen()
turtle.onkey(right,"Right")
turtle.onkey(left,"Left")
turtle.onkey(shoot,"space")

while True:
    wn.update()
    x=enemy.xcor()
    x+=enemyspeed
    enemy.setx(x)
    
    y=bullet.ycor()
    y+=bullet_speed
    bullet.sety(y)
    
    if(y>275):
        bullet.hideturtle()
        bulletstate="not shot"
    
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
        
    d=math.sqrt(math.pow(bob.xcor()-enemy.xcor(),2)+math.pow(bob.ycor()-enemy.ycor(),2))
    d1=math.sqrt(math.pow(bullet.xcor()-enemy.xcor(),2)+math.pow(bullet.ycor()-enemy.ycor(),2))
    
    if(d1<20):
        enemy.setpos(-200,250)
        score = score+10
        text.clear()
        text.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
    
    if(d<20):
        enemy.setpos(-200,250)
        score = score-10
        text.clear()
        text.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
        
    
    

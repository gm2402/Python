import turtle
#Importing Turtle library for basic graphic

#Black background Screen 
wd = turtle.Screen()
wd.title("Ping Pong - Gautam")
wd.bgcolor('white')
wd.setup(width=800, height=600)
wd.tracer(0)

# player A
play_a=turtle.Turtle()
play_a.speed(0)#Animation speed (max)
play_a.shape('square')
play_a.color('yellow')
play_a.shapesize(stretch_wid=5, stretch_len=1)
play_a.penup()
play_a.goto(-350, 0)

# player B
play_b = turtle.Turtle()
play_b.speed(0)#Animation speed (max)
play_b.shape('square')
play_b.color('blue')
play_b.shapesize(stretch_wid=5, stretch_len=1)
play_b.penup()
play_b.goto(+350, 0)

# ball
p_ball=turtle.Turtle()
p_ball.speed(0)#Animation speed (max)
p_ball.shape('square')
p_ball.color('black')
p_ball.penup()
p_ball.goto(0, 0)
p_ball.dx=0.3#To make our ball move
p_ball.dy=-0.3

#pen
pen = turtle.Turtle()
pen.speed(0)#Animation speed
pen.color('red')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
#pen.write("Player A: 0 Player B: 0",align='center',font=('Times New Roman',24,'normal'))

#Function to move player A up and Down
def play_a_up():
    y = play_a.ycor()#Returns turtle's y co-ord
    y += 15#Add 15 pixels to y
    play_a.sety(y)

def play_a_down():
    y = play_a.ycor()#Returns turtle's y co-ord
    y -= 15#subtract 15 pixels to y
    play_a.sety(y)

#Function to move player B up and Down
def play_b_up():
    y = play_b.ycor()#Returns turtle's y co-ord
    y += 15#Add 15 pixels to y
    play_b.sety(y)

def play_b_down():
    y = play_b.ycor()#Returns turtle's y co-ord
    y -= 15#subtract 15 pixels to y
    play_b.sety(y)


#Keyboard binding
wd.listen()
wd.onkeypress(play_a_up, "w")
wd.onkeypress(play_a_down, "s")
wd.onkeypress(play_b_up, "Up")
wd.onkeypress(play_b_down, "Down")


#Game loop
while True:
    wd.update()

    #Move the ball
    p_ball.setx(p_ball.xcor()+p_ball.dx)
    p_ball.sety(p_ball.ycor()+p_ball.dy)

    #Top Border
    # Comparing balls y co-ordinate
    if p_ball.ycor() > 290:
        p_ball.sety(290)
        p_ball.dy *=-1 

    #Bottom Border
    if p_ball.ycor() < -290:
        p_ball.sety(-290)
        p_ball.dy *=-1

    #Left Border 
    if p_ball.xcor() > 390:
        p_ball.goto(0,0)
        p_ball.dx *=-1

    #Right Border 
    if p_ball.xcor() < -390:
        p_ball.goto(0,0)
        p_ball.dx *=-1 

    #Playing with ball
    #Right player
    if (p_ball.xcor() > 340 and p_ball.xcor() < 350) and (p_ball.ycor() < play_b.ycor() + 40 and p_ball.ycor()> p_ball.ycor() - 40):
        p_ball.setx(340)
        p_ball.dx *= -1

    #Left player
    if (p_ball.xcor()<-340 and p_ball.xcor() >- 350) and (p_ball.ycor() < play_a.ycor() + 40 and p_ball.ycor()> p_ball.ycor() - 40):
        p_ball.setx(-340)
        p_ball.dx *= -1

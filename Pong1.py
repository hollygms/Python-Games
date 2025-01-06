import turtle

wn = turtle.Screen()
wn.title("Flipped Pong by Holly")
wn.bgcolor("black")
wn.setup(width=600, height=800)
wn.tracer(0)

#Score
score_L= 0
score_R= 0

# Top Paddle
paddleT =  turtle.Turtle()
paddleT.speed(0)
paddleT.shape("square")
paddleT.color("white")
paddleT.shapesize(stretch_wid=1, stretch_len=5)
paddleT.penup()
paddleT.goto(0,370)

# Bottom Paddle
paddleB =  turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=1, stretch_len=5)
paddleB.penup()
paddleB.goto(0,-360)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# pen
penL = turtle.Turtle()
penL.speed(0)
penL.color("white")
penL.penup()
penL.hideturtle()
penL.goto(-290, 0)
penL.write("0", align="left", font=("Courier", 24, "normal"))

penR = turtle.Turtle()
penR.speed(0)
penR.color("white")
penR.penup()
penR.hideturtle()
penR.goto(280, 0)
penR.write("0", align="right", font=("Courier", 24, "normal"))

#Functions
def paddleT_right():
    x = paddleT.xcor()
    x += 20
    paddleT.setx(x)

def paddleT_left():
    x = paddleT.xcor()
    x += -20
    paddleT.setx(x)

def paddleB_right():
    x = paddleB.xcor()
    x += 20
    paddleB.setx(x)

def paddleB_left():
    x = paddleB.xcor()
    x += -20
    paddleB.setx(x)

#Key bindings
wn.listen()

wn.onkeypress(paddleT_right, "d")
wn.onkeypress(paddleT_left, "a")

wn.onkeypress(paddleB_right, "Right")
wn.onkeypress(paddleB_left, "Left")

#Main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    if ball.xcor() > 280:
        ball.setx(280)
        ball.dx *= -1

    if ball.xcor() < -290:
        ball.setx(-290)
        ball.dx *= -1
    
    if ball.ycor() > 400:
        ball.goto(0,0)
        ball.dy *= -1
        score_R += 1
        penR.clear()
        penR.write("{}".format(score_R), align="center", font=("Courier", 24, "normal"))

    if ball.ycor() < -395:
        ball.goto(0,0)
        ball.dy *= -1
        score_L += 1
        penL.clear()
        penL.write("{}".format(score_L), align="center", font=("Courier", 24, "normal"))


    #Collisions
    if (ball.ycor() > 350 and ball.ycor() < 370) and (ball.xcor() < paddleT.xcor() + 60) and (ball.xcor() > paddleT.xcor() - 60):
        ball.sety(350)
        ball.dy *= -1

    if (ball.ycor() < -340 and ball.ycor() > -360) and (ball.xcor() < paddleB.xcor() + 55) and (ball.xcor() > paddleB.xcor() - 55):
        ball.sety(-340)
        ball.dy *= -1
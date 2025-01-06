import turtle
import time
import random

delay = 0.1

#score
score = 0
highScore = 0

#screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) #turns off screen updates

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

#functions 
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

def gameOver():
    time.sleep(0.5)
    head.goto(0,0)
    head.direction = "stop"
    global score
    score = 0
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, highScore), align="center", font=("Courier", 24, "normal"))
    global delay
    delay = 0.1
    x = random.randint(-290, 280)
    y = random.randint(-290, 290)
    food.goto(x,y)
        
#hide segments
    for segment in segments:
        segment.goto(1000, 1000)
    
#clear the segments list
    segments.clear()

#keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")


#main game loop
while True:
    wn.update()

    #border collision
    if head.xcor() > 270 or head.xcor() < -280 or head.ycor()>280 or head.ycor() < -270:
        gameOver()
        
    #check with collision with food
    if head.distance(food) < 20:
        #move food to random spot
        x = random.randint(-290, 280)
        y = random.randint(-290, 290)
        food.goto(x,y)

        #add segment
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #shorten delay
        delay -= 0.001

        #increase score
        score += 10

        if score > highScore:
            highScore = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, highScore), align="center", font=("Courier", 24, "normal"))

    #move the end segments first
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #move segment 0 to where head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


    move()

    #check for head collisions with body
    for segment in segments:
        if segment.distance(head) < 20:
            gameOver()

    time.sleep(delay)
wn.mainloop()
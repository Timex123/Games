import turtle
import time
import random

wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("White")
wn.setup(width=600, height=600)
wn.tracer(0) #turns off the screen updates

delay = 0.1

#Score
score = 0
high_score = 0


# Snake
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("Black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score: 0", align="center", font=("Times New Roman", 24, "normal"))

#Body
segment = []

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

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"


#Keyboard
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

while True:
    wn.update()

    #Collision with borders
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for s in segment:
            s.goto(500,500)
        segment.clear()

        score = 0
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Times New Roman", 24, "normal"))

    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #Add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.penup()
        segment.append((new_segment))

        delay -=0.001

        #Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Times New Roman", 24, "normal"))

    #Move the segments 1+
    for index in range(len(segment) - 1, 0, -1):
        x = segment[index - 1].xcor()
        y = segment[index - 1].ycor()
        segment[index].goto(x, y)

    #Move segment 0 into head place
    if len(segment) > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x,y)

    move()

    # Body collisions
    for s in segment:
        if s.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction == "stop"

            for s in segment:
                s.goto(500, 500)
            segment.clear()

            score = 0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Times New Roman", 24, "normal"))

    time.sleep(delay)

wn.mainloop()

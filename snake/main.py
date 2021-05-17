import turtle
import time
import random

# delay
delay = 0.1

# SCORE

score = 0
high_score = 1

# set up screen
wn = turtle.Screen()
wn.title("Snake Game By Chef")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)  # turns off screen updates

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Snake Body
segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Sore: 0", align="center", font=("Courier", 24, "normal"))


# Functions

# Set Direction Values

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


# directions and values
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


# keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")

# Main Loop

while True:
    wn.update()

    # CHECK FOR COLLISION
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # hide segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear Segments
        segments.clear()

        delay = 0.1

        # Reset Score
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Food Collision
    if head.distance(food) < 20:
        # Move food
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add body length
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        delay -=0.005


        score += 1

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))

    # Move end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Hits own body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide segments
            for segment in segments:
                segment.goto(1000, 1000)

            delay = 0.1

            # Clear Segments
            segments.clear()
            score = 0
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))


    time.sleep(delay)

wn.mainloop()

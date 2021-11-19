import turtle,tkinter,winsound
# By: Jenil Chudgar
# Class: VI G
# Date: 09.11.2021

# Screen
win = turtle.Screen()
win.title("Pong")
win.bgcolor("white")
win.setup(width=800, height=600)
win.tracer(0)

# Image
img = tkinter.Image("photo", file="icon.png")
turtle._Screen._root.iconphoto(True, img)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.penup()
paddle_a.goto(x=-340, y=0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.penup()
paddle_b.goto(x=340, y=0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(x=0, y=0)
ball.dx = 0.2
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.ht()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0",align="center",font=("Calibri",24,"normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 10
    paddle_a.sety(y=y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 10
    paddle_a.sety(y=y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 10
    paddle_b.sety(y=y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 10
    paddle_b.sety(y=y)


# Keyboard Binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main Loop
while True:
    win.update()

    # Move The Ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1

    pen.clear()
    pen.write(f"Player A: {score_a}  Player B: {score_b}",align="center",font=("Calibri",24,"normal"))

    # Paddel and Ball Collisions
    if ((ball.xcor() < -340) and (ball.ycor() < paddle_a.ycor() + 40) and (ball.ycor() > paddle_a.ycor() - 50)):
        ball.setx(-340)
        ball.dx *= -1

    if ((ball.xcor() > 340) and (ball.ycor() < paddle_b.ycor() + 40) and (ball.ycor() > paddle_b.ycor() - 50)):
        ball.setx(340)
        ball.dx *= -1
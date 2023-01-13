import turtle

win = turtle.Screen()
win.title("Pong Game by Roda Anshur")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)


# Score 
score_a = 0
score_b = 0


# Bar A
bar_a = turtle.Turtle()
bar_a.speed(0)
bar_a.shape("square")
bar_a.color("pink")
bar_a.shapesize(stretch_wid=5, stretch_len=1)
bar_a.penup()
bar_a.goto(-350, 0)

# Bar B
bar_b = turtle.Turtle()
bar_b.speed(0)
bar_b.shape("square")
bar_b.color("pink")
bar_b.shapesize(stretch_wid=5, stretch_len=1)
bar_b.penup()
bar_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("pink")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.125
ball.dy  = 0.125

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("pink")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0 Player B: 0", align="center", font=("Courier", 17, "bold"))


# function
def bar_a_up():
    y = bar_a.ycor()
    y += 20
    bar_a.sety(y)

def bar_a_down():
    y = bar_a.ycor()
    y -= 20
    bar_a.sety(y)

def bar_b_up():
    y = bar_b.ycor()
    y += 20
    bar_b.sety(y)

def bar_b_down():
    y = bar_b.ycor()
    y -= 20
    bar_b.sety(y)

# keyboard binding 
win.listen()
win.onkeypress(bar_a_up, "w")
win.onkeypress(bar_a_down, "s")
win.onkeypress(bar_b_up, "Up")
win.onkeypress(bar_b_down, "Down")

# main part of game
while True:
    win.update()

    #moving the ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)
    

    #border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player 1: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 17, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player 1: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 17, "bold"))

    # where bar and ball meet
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor()< bar_b.ycor() + 40 and ball.ycor() > bar_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < 340 and ball.xcor() < -350) and (ball.ycor()< bar_b.ycor() + 40 and ball.ycor() > bar_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

        
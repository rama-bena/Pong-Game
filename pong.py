import turtle

wn = turtle.Screen()
wn.title("Pong by Rama Bena")
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

#* KONSTANTA
INCREASE_SPEED = 0.01
DEFAULT_SPEED  = 0.05

#* Score
score_a = 0
score_b = 0

#* Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#* Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#* Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = DEFAULT_SPEED
ball.dy = DEFAULT_SPEED

#* Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A:0  Player B: 0", align='center', font=('Courier', 24, 'normal'))

#* --------------------------------- Function --------------------------------- #
def paddle_a_up():
    y = paddle_a.ycor()
    if y+50>=300:
        return
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y-50<=-300:
        return
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y+50>=300: 
        return
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y-50<=-300:
        return
    y -= 20
    paddle_b.sety(y)

def write_score():
    pen.clear()
    pen.write(f"Player A:{score_a}  Player B: {score_b}", align='center', font=('Courier', 24, 'normal'))

def speed_add():
    ball.dx += -INCREASE_SPEED if ball.dx<0 else INCREASE_SPEED
    ball.dy += -INCREASE_SPEED if ball.dy<0 else INCREASE_SPEED

def speed_reset():
    ball.dx = DEFAULT_SPEED
    ball.dy = DEFAULT_SPEED

#* ----------------------------- Keyboard Binding ----------------------------- #
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')


#* ------------------------------ Main Game Loop ------------------------------ #
while True:
    wn.update()
    #* Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #* Paddle and ball collisions
    if (-350<=ball.xcor()<=-340) and (paddle_a.ycor()+40>=ball.ycor()>=paddle_a.ycor()-40): # paddle_a
        ball.setx(-340)
        ball.dx *= -1
        speed_add()

    if (340<=ball.xcor()<=350) and (paddle_b.ycor()+40>=ball.ycor()>=paddle_b.ycor()-40): # paddle_b
        ball.setx(340)
        ball.dx *= -1
        speed_add()

    #* Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390: # lewat batas kanan
        ball.goto(0, 0)
        ball.dx *= -1
        speed_reset()
        score_a += 1
        write_score()

    if ball.xcor() < -390: # lewat batas kiri
        ball.goto(0, 0)
        ball.dx *= -1
        speed_reset()
        score_b += 1
        write_score()










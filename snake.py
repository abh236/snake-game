import turtle
import random
import time
delay = 0.1
sc=0
hs=0
bodies=[]
# Create a new turtle screen and set its background color


s= turtle.Screen()
w_l=600
h_l=600
s.setup(width=w_l,height=h_l)
s.bgcolor("light blue")
s.title("Snake Game")


# Create the snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue")
turtle.colormode(255)

head.fillcolor((250,0,0))
head.penup()
head.goto(0,0)
head.direction = "stop"

# Create the snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
c1=random.randint(0,255)
d1=random.randint(0,255)
e1=random.randint(0,255)
food.color((c1,d1,e1))
food.penup()
food.ht()
food.goto(200,200)
food.st()


# creating a score body
score = turtle.Turtle()
score.speed(0)
score.ht()
score.penup()
score.goto(-250,250)
score.st()
score.color("black")
score.write("Score: 0   |  Highest Score:0",font=("Arial",24,"bold"))

# function to move the snake
def moveup():
  if head.direction != "down":
    head.direction = "up"
def movedown():
  if head.direction != "up":
    head.direction = "down"
def moveright():
  if head.direction != "left":
    head.direction = "right"
def moveleft():
  if head.direction != "right":
    head.direction = "left"
def backtohome():
  head.direction="stop"

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

# event handling
s.listen()
s.onkey(moveup,"w")
s.onkey(moveup,"Up")
s.onkey(movedown,"s")
s.onkey(movedown,"Down")
s.onkey(moveright,"d")
s.onkey(moveright,"Right")
s.onkey(moveleft,"a")
s.onkey(moveleft,"Left")
s.onkey(backtohome,"Escape")

# main loop
while True:
  s.update()
  width = s.window_width()
  height = s.window_height()
  if width != w_l or height != w_l:
    w_l = width
    h_l = height
    
   
  # check collision with border
  if head.xcor() >w_l/2-10 :
    head.setx(-w_l/2+10)
  if head.xcor() < -w_l/2+10:
    head.setx(w_l-10)
  if head.ycor() >h_l/2-10 :
    head.sety(-h_l/2+10)
  if head.ycor() < -h_l/2+10:
    head.sety(h_l/2-10)
  # check collision with food
  if head.distance(food) < 20 :
    x = random.randint(int(-w_l/2+10),int(w_l/2-10))
    y = random.randint(int(-h_l/2+10),int(h_l/2-10))
    c=random.randint(0,255)
    d=random.randint(0,255)
    e=random.randint(0,255)
    food.color((c,d,e))
    food.goto(x,y)
    # increase the body of snake
    body=turtle.Turtle()
    body.speed(0)
    body.penup()
    body.shape("square")
    turtle.colormode(255)
    body.color((c1,d1,e1))
    c1=c
    d1=d
    e1=e
    bodies.append(body)

    sc = sc + 10
    delay=delay-0.001
    if sc>hs:
      hs= sc
    score.clear()  
    score.write("Score:{}  |   Highest Score:{}".format(sc,hs),font=("Arial",24,"bold"))

   # move snake bodies
  for index in range(len(bodies)-1,0,-1):
    x=bodies[index-1].xcor()
    y=bodies[index-1].ycor()
    bodies[index].goto(x,y)
  if len(bodies)>0:
      x=head.xcor()
      y=head.ycor()
      bodies[0].goto(x,y)
  move()  


# check collision with bodies
  for body in bodies:
    if body.distance(head) < 20:
      time.sleep(1)
      head.goto(0,0)
      head.direction="stop"
      for body in bodies:  
        body.ht()

      bodies.clear()
      sc=0
      delay=0.1
      score.clear()
      score.write("Score:{}  |   Highest Score:{}".format(sc,hs),font=("Arial",24,"bold"))
  time.sleep(delay)


s.exitonclick() 
#Spider
import turtle as trtl
spider = trtl.Turtle()

#web
spider.penup()
spider.pensize(10)
spider.goto(0,0)
spider.color("blue")
spider.pendown()
spider.goto(0,400)

#Create spider abdomen
spider.penup()
spider.color("black")
spider.goto(0,0)
spider.pendown()
spider.pensize(80)
spider.circle(40)

#create spider hour glass
spider.penup()
spider.goto(0,40)
spider.pendown()
spider.pensize(20)
spider.color("red")
spider.circle(20,360,3)
spider.penup()
spider.goto(0,20)
spider.pendown()
spider.left(180)
spider.circle(20,360,3)

#create spider head
spider.color("black")
spider.penup()
spider.goto(0,-40)
spider.pendown()
spider.pensize(40)
spider.circle(20)

#Spider led configeration
leg=4
size=150
angle=90
turns=3
location=90/leg
spider.pensize(10)
x=0
y=0

#spider legs
while (x < leg):
  spider.penup()
  spider.goto(40,-20)
  spider.pendown()
  spider.setheading(location*x)
  spider.circle(size,angle,turns)
  x = x + 1

spider.right(180)

while (y < leg):
  spider.penup()
  spider.goto(-40,-20)
  spider.pendown()
  spider.setheading(location*y -45)
  spider.circle(size,angle,turns)
  y = y + 1

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()

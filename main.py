import random
import turtle

from colors import color_list

turtle.colormode(255)
draw_area = turtle.Screen()
draw_area.bgcolor("black")


timmy = turtle.Turtle()
timmy.hideturtle()

timmy.pu()
timmy.setpos(-300, -300)
timmy.pd()
timmy.speed(0)

cur_x = timmy.xcor()
cur_y = timmy.ycor()


def draw_painting():
  for y in range(0, 501, 50):
    for x in range(0, 501, 50):
      timmy.setpos(cur_x + x, cur_y + y)
      timmy.pd()
      timmy.color(random.choice(color_list))
      timmy.dot(20)
      timmy.pu()


draw_painting()

screen = turtle.Screen()
screen.exitonclick()
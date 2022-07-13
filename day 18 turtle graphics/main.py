import random


from turtle import Turtle, Screen


Screen().colormode(255)
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

t = Turtle()
t.speed("fastest")
def square():
    for x in range(4):

        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)

def triangle(): #equilateral triangle
    for x in range(3):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(120) # external angles of triangle

def right_triangle():

    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(110)
    timmy_the_turtle.right(120)
    timmy_the_turtle.forward(120)
    timmy_the_turtle.right(180)


def dashed_line():
    for x in range (10):
        t.pu()
        t.forward(10)
        t.pd()
        t.forward(10)

def color_change():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    list = [r, g, b]
    mytuple = tuple(list)

    #print(mytuple)
    t.pencolor(mytuple)




def draw_polygon(n,l):
    """l = length of sides, n is number of sides"""
    for _ in range(n):
        t.right(25)
        t.forward(250)

        color_change()
        t.forward(l)
        t.right(360 / n)

def random_direction():
    direction = [90, 180, 270, 360] #90 degree change in angle
    b = range(0, 350)# all angles
    a = random.choice(b)
    return a

def random_walk():

    for x in range(1000):
        color_change()
        widths = random.randint(1, 20)
        t.width(widths)
        t.right(random_direction())

        print(random_direction())
        t.forward(400)
        # t.right(180)
        # t.forward(100)

def spirograph(gap_size):
    for x in range(int(360/gap_size)):
        color_change()
        t.circle(100)
        t.setheading(t.heading() + gap_size)

# t.width(4)
# t.forward(100)

spirograph(5)
# draw_polygon(3, 100)
# draw_polygon(4, 100)
# draw_polygon(5, 100)
# draw_polygon(6, 100)
# draw_polygon(7, 100)
# draw_polygon(8, 100)
# draw_polygon(9, 100)
# draw_polygon(10, 100)
# draw_polygon(11, 100)
# draw_polygon(12, 100)
# draw_polygon(13, 100)
# draw_polygon(14, 100)
# draw_polygon(15, 100)
# draw_polygon(16, 100)
# draw_polygon(17, 100)
























screen = Screen()
screen.exitonclick()



import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 500, height = 400)
#user_bet = screen.textinput(title="Make your bet", prompt= "which Turtle?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
list1 = [10, 10, 10, 20, 20, 50, 20, 30, 30, 10, 10, 10]



def get_set_go(t,x):
    race = True
    while race == True:
        t.fd(random.choice(list1))
        t.pos()
        print(t.pos())
        if x >= (200, 0):
            print ("you win")
            print(t)
            race = False

def test(t):
    #x = (190, 200)
    if t >= (200, 000):
        print("it works")

tim = Turtle(shape="turtle")
tim.penup()
tim.color("red")
tim.goto(x=230, y=100)
get_set_go(tim,tim.pos())


t2 = Turtle(shape="turtle")
t2.penup()
t2.color("blue")
t2.goto(x=-230, y=60)
get_set_go(t2, t2.pos())

t3 = Turtle(shape="turtle")
t3.penup()
t3.color("green")
t3.goto(x=-230, y=140)
get_set_go(t3, t3.pos())

t4 = Turtle(shape="turtle")
t4.penup()
t4.color("purple")
t4.goto(x=-230, y=180)
get_set_go(t4, t4.pos())


t5 = Turtle(shape="turtle")
t5.penup()
t5.color("Yellow")
t5.goto(x=-230, y=20)
get_set_go(t5, t5.pos())


t6 = Turtle(shape="turtle")
t6.penup()
t6.color("orange")
t6.goto(x=-230, y=-20)
get_set_go(t6, t6.pos())


#test(tim.pos())
screen.exitonclick()

#want to make checkered line at x postion 200.
#Need to figure out in get_set_go what vec2d is and compare it or convert it to int

#vector is a tuple
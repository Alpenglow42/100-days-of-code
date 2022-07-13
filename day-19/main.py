



from turtle import Turtle, Screen

t = Turtle()
screen = Screen()



def forward():
    t.fd(5)


def right():
    t.right(10)

def left():
    t.left(10)

def back():
    t.back(5)


def clear():
    t.clear()

def home():
    t.home()

screen.listen()
screen.onkey(key = "w", fun = forward)
screen.onkey(key = "d", fun = right)
screen.onkey(key = "a", fun = left)
screen.onkey(key = "s", fun = back)
screen.onkey(key = "c", fun = clear)
screen.onkey(home, "h")

screen.exitonclick()
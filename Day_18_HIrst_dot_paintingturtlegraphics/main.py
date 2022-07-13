# This is a sample Python script.
import turtle
import random
from turtle import Screen
import colorgram
from functools import reduce

# rgb_colors = []
# colors = colorgram.extract("hirstspotpainting.jpg",30)
#
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)
screen = Screen()
screen.colormode(255)


list1 = [ (71, 37, 30), (164, 151, 53),(130, 34, 23), (58, 40, 43),
(246, 242, 234), (248, 241, 245), (239, 247, 241), (239, 242, 247), (197, 166, 116), (141, 80, 57), (219, 201, 139),
(60, 93, 118), (136, 162, 182),  (52, 116, 86), (71, 37, 30), (192, 95, 79),
(145, 178, 149), (22, 91, 70), (164, 142, 156), (111, 75, 80), (227, 175, 164), (28, 58, 75),
(135, 25, 31), (179, 204, 173), (27, 81, 88), (18, 68, 57), (89, 146, 127), (43, 66, 87), (168, 102, 106),
(224, 174, 179), (114, 127, 145)
]


listbad = [ ]

#cr = random.choice(list1)

y = 1
c = 0
d = 0


def turtle_start_pos():
    turtle.left(180)
    turtle.penup()
    turtle.fd(400)
    turtle.left(90)
    turtle.fd(300)
    turtle.left(90)





def line_dot():
    global d
    for x in range(20):

        turtle.dot(20, random.choice(list1))
        d += 1
        if d <= 19:# make d count 1 less than range
            turtle.fd(50)

        #turtle.penup()
        #print(cr)





turtle_start_pos()

while c <= 20:

    t = 0


    line_dot()
    if t == 0:
        turtle.left(90)
        turtle.fd(40)
        turtle.left(90)
        c += 1
        t = 1
        d = 0
        line_dot()
    if t == 1:
        turtle.right(90)
        turtle.fd(40)
        turtle.right(90)
        c += 1
        t = 0
        d = 0


turtle.exitonclick()

# when turle turn misses dot at end of row it turns from.
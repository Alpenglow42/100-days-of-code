import random
from turtle import Turtle
from scoreboard import Scoreboard

scoreboard = Scoreboard()

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CarIncrease = 1

y1 = random.randint(-100, -50)
y2 = random.randint(-200, -150)
y3 = random.randint(50, 100)

CarLanes = [y1, y2, y3]

class CarManager:


    def __init__(self):

        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):

        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-289, 280)
        new_car.goto(300, random_y)
        self.all_cars.append(new_car)

        # print(scoreboard.level)
        # increase how often car is produced
        if scoreboard.level <= 4:
            random_chance = random.randint(1, 6)


        elif scoreboard.level >= 5:
            random_chance = random.randint(1, 5)



        elif scoreboard.level >= 8:
            random_chance = random.randint(1, 4)

        elif scoreboard.level >= 10:
            random_chance = random.randint(1, 3)

        if random_chance == 1:


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += CarIncrease

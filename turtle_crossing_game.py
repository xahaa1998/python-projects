##-----------this code has 4 classes and i separated them by their names as comment-----------##

## -------------------------------------main.py--------------------------------------##
from turtle import Screen
from score import Score
from player import Player
from car_manager import Car_Manager
import time

car=Car_Manager()
score=Score()
player=Player()
screen=Screen()
screen.setup(800,600)
screen.listen()
screen.onkey(player.up,"Up")
screen.tracer(0)

is_on=True
while is_on:
    time.sleep(0.1)
    screen.update()
    car.random_car()
    car.move_car()

    for one_car in car.all_cars:
        if player.distance(one_car) < 25:
            is_on = False
            score.game_over()

    if player.ycor()>=280:
        score.increase_score()
        player.increase_score()
        car.increase_score()

screen.exitonclick()

##----------------------------------- car manger.py --------------------------------------##

from turtle import Turtle
import random
COLORS = ["red","blue","green","yellow","orange","purple","pink","brown","black",]

class Car_Manager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = 5
        self.create_car()

    def create_car(self):
        car = Turtle("square")
        car.speed(0)
        car.penup()
        random_color = random.choice(COLORS)
        car.color(random_color)
        car.shapesize(stretch_len=2, stretch_wid=1)
        random_y = random.randint(-250, 250)
        car.goto(350, random_y)
        self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def random_car(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            self.create_car()

    def increase_score(self):
        self.car_speed +=5
## --------------------------------- player.py ------------------------------------------##

from turtle import Turtle
SPEED_NUM=10
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.speed(SPEED_NUM)
        self.goto(0,-280)
        self.setheading(90)

    def up(self):
        self.setheading(90)
        self.forward(10)

    def increase_score(self):
        self.goto(0,-280)
        self.speed (SPEED_NUM+10)


## ------------------------------------- score.py -----------------------------------------------##

from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score=1
        self.speed(0)
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-320,250)
        self.display()

    def display(self):
        self.clear()
        self.write(f"level {self.score}",align="left",font=("arial",20,"normal"))

    def increase_score(self):
        self.score+=1
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align="center",font=("arial",30,"italic"))



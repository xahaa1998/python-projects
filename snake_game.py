#MAIN PART(MAIN.PY)
import time
from  snake import *
from food import Food
from score import Score

snake=Snake()
food=Food()
score=Score()
score.text()


screen=Screen()
screen.setup(900,700)
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")
screen.onkey(snake.left,"a")

on=True
while on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    if snake.segment[0].distance(food) < 20:
        food.refresh()
        score.increase()
        snake.extend()
    if snake.segment[0].xcor() > 440 or snake.segment[0].xcor() < -440 or snake.segment[0].ycor() >340 or snake.segment[0].ycor() <-330:
        on=False
        score.game_over()
    for i in snake.segment[1:]:
        if snake.segment[0].distance(i)<10:
            on=False
            score.game_over()

screen.exitonclick()

#SNAKE PART(SANKE.PY)
from turtle import *

class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()

    def add_segment(self, position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segment.append(t)

    def create_snake(self):
        n = [(0,0),(-20, 0), (-40, 0)]
        for i in n:
            self.add_segment(i)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for i in range(len(self.segment)-1,0,-1):
            x=self.segment[i-1].xcor()
            y=self.segment[i-1].ycor()
            self.segment[i].goto(x,y)
        self.segment[0].forward(20)

    def up(self):
        if self.segment[0].heading() !=270:
            self.segment[0].setheading(90)
    def down(self):
        if self.segment[0].heading() !=90:
            self.segment[0].setheading(270)
    def right(self):
        if self.segment[0].heading() !=180:
            self.segment[0].setheading(0)
    def left(self):
        if self.segment[0].heading() !=0:
            self.segment[0].setheading(180)

#FOOD PART(FOOD.PY)

from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.penup()
        #self.hideturtle()
        self.color("white")
        self.speed(0)
        self.score=0
        self.refresh()


    def refresh(self):
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)
        self.goto(new_x,new_y)
#SCORE PART(SCORE.PY)
from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.speed(0)
        self.color("white")
        self.hideturtle()

    def text(self):
        self.goto(0, 300)
        self.write(f"score : {self.score}", align="center", font=("arial", 20, "normal"))

    def increase(self):
        self.clear()
        self.score+=1
        self.write(f"score : {self.score}", align="center", font=("arial", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER! ",align="center",font=("arial",30,"italic"))




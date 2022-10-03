from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


x_pos = -230
y_pos = -100

for turtle_index in range(0, 6):
    race_turtle = Turtle(shape="turtle")
    race_turtle.penup()
    race_turtle.goto(x_pos, y_pos)
    y_pos += 40
    race_turtle.color(colors[turtle_index])
    all_turtles.append(race_turtle)


if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lose! The {winning_color} turtle is the winner!")





screen.exitonclick()

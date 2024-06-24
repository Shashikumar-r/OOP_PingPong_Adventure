from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.penup()
        self.x_move = 10
        self.y_move = 10

    # TODO 4:- create a ball

    def ball_move(self):
        x_axis = self.xcor() + self.x_move
        y_axis = self.ycor() + self.y_move
        self.goto(x_axis, y_axis)

    # TODO 5:- detect a collision with wall
    def bouncing_ball_y(self):
        self.y_move *= -1

    # TODO 6:- detect a collision with paddle
    def bouncing_ball_x(self):
        self.x_move *= -1

    # TODO 6:- if ball voes outside of boundary rest_position
    def reset_position(self):
        self.goto(0,0)
        self.bouncing_ball_x()











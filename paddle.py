from turtle import Turtle,Screen
class Paddle(Turtle):     # In Paddle class have another class Turtle :- Inheritance
    def __init__(self):
        super().__init__()
        screen = Screen()
        screen.listen()

    # TODO 2:-create a paddle
    # TODO 3:-create a another paddle


    def common_paddle(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(1, 3.8)
        self.setheading(90)

    # TODO 2.1:-paddle responds to key presses

    def paddle_forward(self):
        self.fd(90)

    def paddle_backward(self):
        self.bk(90)

    def r_paddle_move(self,screen):
        screen.onkey(key="Up", fun=self.paddle_forward)
        screen.onkey(key="Down", fun=self.paddle_backward)

# TODO 3.1:-paddle responds to key presses

    def l_paddle_move(self,screen):
        screen.onkey(key="w", fun=self.paddle_forward)
        screen.onkey(key="s", fun=self.paddle_backward)


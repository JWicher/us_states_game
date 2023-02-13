from turtle import Turtle

FONT = ('Courier', 15, 'normal')
ALIGN = 'center'

class State(Turtle):

    def __init__(self, state_name):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.state_name = state_name

    def put_label(self, coordinates):
        self.goto(coordinates)
        self.write(self.state_name, align=ALIGN, font=FONT)

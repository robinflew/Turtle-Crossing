import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.penup()
        self.turtle.goto(STARTING_POSITION)
        self.turtle.setheading(90)
        self.screen = turtle.Screen()
        self.screen.listen()
        self.screen.onkey(self.move, "Up")

    def move(self):
        self.turtle.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.turtle.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.turtle.goto(STARTING_POSITION)

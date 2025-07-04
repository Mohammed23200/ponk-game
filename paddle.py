from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self,position):
        super().__init__(shape='square')  # Fixed this line
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(x=position, y=0)
        self.x_position = position  # Store the x position
    
    def up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.x_position, y=new_y)  # Use stored x position

    def down(self):  # Changed to lowercase 'd'
        new_y = self.ycor() - 20
        self.goto(x=self.x_position, y=new_y)  # Use stored x position

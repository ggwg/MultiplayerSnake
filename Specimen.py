# Simple Snake Game in Python 3 for Beginners
# By @TokyoEdTech

import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

class Gamestate:

    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.title("Snake Game by @TokyoEdTech")
        self.wn.bgcolor("green")
        self.wn.setup(width=1000, height=1000)
        self.wn.tracer(0) # Turns off the screen updates
        # Game statistics pen
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))
        # Food 
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("circle")
        self.food.color("red")
        self.food.penup()
        self.food.goto(0,100)
        # Players
        self.p1 = Snake()
        # Segments
    def start(self):
        global score, high_score, delay
        # Keyboard bindings
        self.wn.listen()
        self.wn.onkeypress(self.p1.go_up, "w")
        self.wn.onkeypress(self.p1.go_down, "s")
        self.wn.onkeypress(self.p1.go_left, "a")
        self.wn.onkeypress(self.p1.go_right, "d")

        # Main game loop
        while True:
            self.wn.update()

            # Check for a collision with the border
            if self.p1.getXPos()>500 or self.p1.getXPos()<-500 or self.p1.getYPos()>500 or self.p1.getYPos()<-500:
                time.sleep(1)
                self.p1.head.goto(0,0)
                head.direction = "stop"

                # Hide the segments
                for segment in self.p1.segments:
                    segment.goto(1000, 1000)
                
                # Clear the segments list
                self.p1.segments.clear()

                # Reset the score
                score = 0

                # Reset the delay
                delay = 0.1

                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


            # Check for a collision with the food
            if self.p1.head.distance(self.food) < 20:
                # Move the food to a random spot
                x = random.randint(-290, 290)
                y = random.randint(-290, 290)
                self.food.goto(x,y)

                # Add a segment
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("grey")
                new_segment.penup()
                self.p1.segments.append(new_segment)

                # Shorten the delay
                delay -= 0.001

                # Increase the score
                score += 10

                if score > high_score:
                    high_score = score
                
                self.pen.clear()
                self.pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

            # Move the end segments first in reverse order
            for index in range(len(self.p1.segments)-1, 0, -1):
                x = self.p1.segments[index-1].xcor()
                y = self.p1.segments[index-1].ycor()
                self.p1.segments[index].goto(x, y)

            # Move segment 0 to where the head is
            if len(self.p1.segments) > 0:
                x = self.p1.getXPos()
                y = self.p1.getYPos()
                self.p1.segments[0].goto(x,y)

            self.p1.move()    

            # Check for head collision with the body segments
            for segment in self.p1.segments:
                if segment.distance(self.p1.head) < 20:
                    time.sleep(1)
                    self.p1.head.goto(0,0)
                    self.head.direction = "stop"
                
                    # Hide the segments
                    for segment in self.p1.segments:
                        segment.goto(1000, 1000)
                
                    # Clear the segments list
                    self.p1.segments.clear()

                    # Reset the score
                    score = 0

                    # Reset the delay
                    delay = 0.1
                
                    # Update the score display
                    pen.clear()
                    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            time.sleep(delay)
        self.wn.mainloop()
class Snake:

    def __init__(self):
        self.head = turtle.Turtle() 
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("black")
        self.head.penup()
        self.head.goto(0,0)
        self.head.direction = "stop"
        # Snake segments
        self.segments = []

    def getXPos(self):
        return self.head.xcor()

    def getYPos(self):
        return self.head.ycor() 

        # Functions
    def go_up(self):
        if self.head.direction != "down":
            self.head.direction = "up"

    def go_down(self):
        if self.head.direction != "up":
            self.head.direction = "down"

    def go_left(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def go_right(self):
        if self.head.direction != "left":
            self.head.direction = "right"

    def move(self):
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + 20)

        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - 20)

        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - 20)

        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + 20)

newGame = Gamestate() 
newGame.start()
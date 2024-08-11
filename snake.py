import turtle
import random
import time 

delay = 0.2
score = 0
high_score = 0

# Creating the window and setting height and width
wn = turtle.Screen()
wn.title("Dragon Game")
wn.bgcolor("#478778")
wn.setup(width=700, height=700)
wn.tracer(0)

# Creating a border for the game
border = turtle.Turtle()
border.speed(5)
border.pensize(4)
border.penup()
border.goto(-310, 250)
border.pendown()
border.color('white')
border.forward(600)
border.right(90)
border.forward(500)
border.right(90)
border.forward(600)
border.right(90)
border.forward(500)
border.penup()
border.hideturtle()

# Creating the head with a larger size
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.shapesize(stretch_wid=1.5, stretch_len=1.5)  # Increase size
head.penup()
head.goto(0, 150)
head.direction = "stop"

# Adding eyes to the head
eye1 = turtle.Turtle()
eye1.speed(0)
eye1.shape("circle")
eye1.color("white")
eye1.shapesize(stretch_wid=0.3, stretch_len=0.3)
eye1.penup()
eye1.goto(-10, 165)  # Position eye1 on the head

eye2 = turtle.Turtle()
eye2.speed(0)
eye2.shape("circle")
eye2.color("white")
eye2.shapesize(stretch_wid=0.3, stretch_len=0.3)
eye2.penup()
eye2.goto(10, 165)  # Position eye2 on the head

# Adding pupils to the eyes
pupil1 = turtle.Turtle()
pupil1.speed(0)
pupil1.shape("circle")
pupil1.color("black")
pupil1.shapesize(stretch_wid=0.1, stretch_len=0.1)
pupil1.penup()
pupil1.goto(-10, 168)  # Position pupil1 on the eye1

pupil2 = turtle.Turtle()
pupil2.speed(0)
pupil2.shape("circle")
pupil2.color("black")
pupil2.shapesize(stretch_wid=0.1, stretch_len=0.1)
pupil2.penup()
pupil2.goto(10, 168)  # Position pupil2 on the eye2

# Adding a tongue
tongue = turtle.Turtle()
tongue.speed(0)
tongue.shape("square")
tongue.color("pink")
tongue.shapesize(stretch_wid=0.1, stretch_len=0.5)
tongue.penup()
tongue.goto(0, 140)  # Position tongue below the head
tongue.setheading(270)  # Point the tongue downward

# Creating food 
food = turtle.Turtle()
food_color = random.choice(['red', 'green', 'blue'])
food_shape = random.choice(['circle', 'square', 'triangle'])
food.speed(0)
food.shape(food_shape)
food.color(food_color)
food.penup()
food.goto(20, 20)

# Creating space to show score and high score
scoreBoard = turtle.Turtle()
scoreBoard.speed(0)
scoreBoard.shape("square")
scoreBoard.color("white")
scoreBoard.penup()
scoreBoard.hideturtle()
scoreBoard.goto(0, 250)
scoreBoard.write("Score: 0 High Score: 0", align="center", font=("Courier", 25, "bold"))

# Assigning key directions
def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        eye1.sety(eye1.ycor() + 20)  # Move eyes with the head
        eye2.sety(eye2.ycor() + 20)
        pupil1.sety(pupil1.ycor() + 20)  # Move pupils with the eyes
        pupil2.sety(pupil2.ycor() + 20)
        tongue.sety(tongue.ycor() + 20)  # Move tongue with the head
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        eye1.sety(eye1.ycor() - 20)
        eye2.sety(eye2.ycor() - 20)
        pupil1.sety(pupil1.ycor() - 20)
        pupil2.sety(pupil2.ycor() - 20)
        tongue.sety(tongue.ycor() - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        eye1.setx(eye1.xcor() - 20)
        eye2.setx(eye2.xcor() - 20)
        pupil1.setx(pupil1.xcor() - 20)
        pupil2.setx(pupil2.xcor() - 20)
        tongue.setx(tongue.xcor() - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        eye1.setx(eye1.xcor() + 20)
        eye2.setx(eye2.xcor() + 20)
        pupil1.setx(pupil1.xcor() + 20)
        pupil2.setx(pupil2.xcor() + 20)
        tongue.setx(tongue.xcor() + 20)

wn.listen()
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

segments = []

# Track when the game over message should appear
game_over_time = None

# Main Game 
while True: 
    wn.update()

    # Ending the game on collision with any of the walls
    if head.xcor() > 280 or head.xcor() < -300 or head.ycor() > 240 or head.ycor() < -240:
        if game_over_time is None:
            game_over_time = time.time()  
        wn.clear()
        wn.bgcolor('blue')
        scoreBoard.goto(0, 0)
        scoreBoard.write("Game Over!\nYour score is: {}".format(score), align="center", font=("Courier", 30, "bold"))
        if time.time() - game_over_time > 15:  
            scoreBoard.clear()
            scoreBoard.write("Try again\nYour score is: {}".format(score), align="center", font=("Courier", 30, "bold"))
            break

    # If head collects food
    if head.distance(food) < 20:
        score += 10
        if score > high_score:
            high_score = score
        scoreBoard.clear()
        scoreBoard.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 25, "bold"))

        # Creating food at a random location
        x_cord = random.randint(-290, 270)
        y_cord = random.randint(-240, 240)
        food_color = random.choice(['red', 'green', 'blue'])
        food_shape = random.choice(['circle', 'square', 'triangle'])
        food.speed(0)
        food.shape(food_shape)
        food.color(food_color)
        food.goto(x_cord, y_cord)

        # Adding a new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("white smoke")
        new_segment.penup()
        segments.append(new_segment)

        # Decreasing delay to speed up the game
        delay *= 0.95

    # Moving the snake and ending the game on collisions of head with body segments
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Checking for collision with the body (tail)
    for segment in segments:
        if segment.distance(head) < 20:
            if game_over_time is None:
                game_over_time = time.time()  
            wn.clear()
            wn.bgcolor('blue')
            scoreBoard.goto(0, 0)
            scoreBoard.write("Game Over!\nYour Score is: {}".format(score), align="center", font=("Courier", 30, "bold"))
            if time.time() - game_over_time > 10:  
                scoreBoard.clear()
                scoreBoard.write("Try again\nYour Score is: {}".format(score), align="center", font=("Courier", 30, "bold"))
                break

    time.sleep(delay)






# make the game breakout with turtle using oop and classes

import turtle


class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.color("white")
        self.goto(0, -250)

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0, -230)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset(self):
        self.goto(0, -230)
        self.bounce_y()


class Brick(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.color("white")
        self.goto(x, y)


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(-290, 270)
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="left", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 16, "normal"))


class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Breakout")
        self.screen.tracer(0)
        self.paddle = Paddle()
        self.ball = Ball()
        self.scoreboard = Scoreboard()
        self.bricks = []
        self.screen.listen()
        self.screen.onkey(self.paddle.move_left, "Left")
        self.screen.onkey(self.paddle.move_right, "Right")
        self.create_bricks()
        self.game_is_on = True

    def create_bricks(self):
        for x in range(-280, 280, 80):
            for y in range(250, 350, 20):
                brick = Brick(x, y)
                self.bricks.append(brick)

    def check_collision(self):
        for brick in self.bricks:
            if self.ball.distance(brick) < 20:
                self.ball.bounce_y()
                self.bricks.remove(brick)
                brick.hideturtle()
                self.scoreboard.increase_score()

        if self.ball.distance(self.paddle) < 20:
            self.ball.bounce_y()

        if self.ball.xcor() > 280 or self.ball.xcor() < -280:
            self.ball.bounce_x()

        if self.ball.ycor() > 280:
            self.ball.bounce_y()

        if self.ball.ycor() < -280:
            self.scoreboard.game_over()
            self.game_is_on = False

    def play(self):
        while self.game_is_on:
            self.screen.update()
            self.ball.move()
            self.check_collision()

        self.screen.exitonclick()


game = Game()
game.play()





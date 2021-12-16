import arcade
import random

WIDTH = 800
HEIGHT = 800
TITLE = "ArcadeNoid"


class Ball:
    def __init__(self, x, y, radius, color):
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color

        self.dx = 100
        self.dy = 300


    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)

    def update(self, delta_time):
        self.x = self.x + self.dx * delta_time
        self.y = self.y + self.dy * delta_time
        if self.x >= WIDTH - self.radius or self.x <= 0 + self.radius:
            self.dx = -self.dx
        if self. y  >= HEIGHT - self.radius or self.y <= 0 + self.radius:
            self.dy = -self.dy


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        self.background_color = arcade.color.BLOND
        self.ball = Ball(400, 400, 20, arcade.color.CARIBBEAN_GREEN)
        self.ball1 = Ball(400, 400, 20, arcade.color.CARIBBEAN_GREEN)
        self.ball1.dx = 300
        self.ball1.dy = 150

    def update(self, delta_time: float):
        self.ball.update(delta_time)
        self.ball1.update(delta_time)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()
        self.ball1.draw()




MyGame().run()
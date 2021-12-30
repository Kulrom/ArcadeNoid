import random


import arcade

from configs import WIDTH, HEIGHT, TITLE, N
from ball import Ball
from paddle import Paddle


def random_color():
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)
    return (r, g, b)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        self.background_color = arcade.color.BLOND
        self.paddle = Paddle(WIDTH * 0.5, HEIGHT/16)
        self.ball = Ball(100, 100)

    def update(self, delta_time: float):
        self.ball.update(delta_time)
        self.paddle.update(delta_time)


    def on_draw(self):
        arcade.start_render()
        self.ball.draw()
        self.paddle.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.paddle.move_left = True
        elif symbol == arcade.key.RIGHT:
            self.paddle.move_right = True

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.paddle.move_left = False
        elif symbol == arcade.key.RIGHT:
            self.paddle.move_right = False


MyGame().run()

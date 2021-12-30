import random


import arcade

from configs import WIDTH, HEIGHT, TITLE, N
from ball import Ball


def random_color():
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)
    return (r, g, b)





class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        self.background_color = arcade.color.BLOND
        self.balls = []
        for i in range(N):
            self.balls.append(Ball(random.randrange(WIDTH), random.randrange(HEIGHT), 20, arcade.color.CARIBBEAN_GREEN))

    def update(self, delta_time: float):
        for i in range(N):
            self.balls[i].update(delta_time)
            for j in range(N):
                if i != j:
                    colision = self.balls[i].is_colise_other_ball(self.balls[j])
                    if colision == True:
                        self.balls[i].color = random_color()


    def on_draw(self):
        arcade.start_render()
        for i in range(N):
            self.balls[i].draw()


MyGame().run()

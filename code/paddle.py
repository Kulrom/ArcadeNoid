import arcade
from configs import *

class Paddle(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__('..\\resources\\png\\paddleBlu.png', scale=SPRITE_SCALE)
        self.center_x = center_x
        self.center_y = center_y
        self.move_left = False
        self.move_right = False
        self.speed = 600

    def update(self, dt):
        if self.move_right and self.move_left:
            pass
        elif self.move_left:
            self.center_x -= self.speed * dt
        elif self.move_right:
            self.center_x += self.speed * dt

        if self.center_x <= 0 + self.width * 0.5:
            self.center_x = 0 + self.width * 0.5

        if self.center_x >= WIDTH - self.width * 0.5:
            self.center_x = WIDTH - self.width * 0.5


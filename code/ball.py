import arcade
import math

from configs import *

class OldBall:
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
        if self.x <= 0 + self.radius:
            self.dx = - self.dx
            self.x = 0 + self.radius
        if self.x >= WIDTH - self.radius:
            self.dx = - self.dx
            self.x = WIDTH - self.radius
        if self.y <= 0 + self.radius:
            self.dy = - self.dy
            self.y = 0 + self.radius
        if self.y >= HEIGHT - self.radius:
            self.dy = - self.dy
            self.y = HEIGHT - self.radius


    def get_dist(self, other_ball: 'Ball'):
        """вычисляет расстояние между мячами"""
        x1 = other_ball.x
        x2 = self.x
        dx = x1 - x2
        y1 = other_ball.y
        y2 = self.y
        dy = y1 - y2
        c = math.sqrt(dx*dx + dy*dy)
        return c

    def is_colise_other_ball(self, other_ball: 'Ball'):
        c = self.get_dist(other_ball)
        if c <= self.radius + other_ball.radius:
            return True
        else:
            return False

class Ball(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__('..\\resources\\png\\ballGrey.png', scale=SPRITE_SCALE)
        self.radius = self.width * 0.5
        self.dx = 100
        self.dy = 300
        self.center_x = center_x
        self.center_y = center_y

    def update(self, dt):
        self.center_x = self.center_x + self.dx * dt
        self.center_y = self.center_y + self.dy * dt
        if self.center_x <= 0 + self.radius:
            self.dx = - self.dx
            self.center_x = 0 + self.radius
        if self.center_x >= WIDTH - self.radius:
            self.dx = - self.dx
            self.center_x = WIDTH - self.radius
        if self.center_y <= 0 + self.radius:
            self.dy = - self.dy
            self.center_y = 0 + self.radius
        if self.center_y >= HEIGHT - self.radius:
            self.dy = - self.dy
            self.center_y = HEIGHT - self.radius
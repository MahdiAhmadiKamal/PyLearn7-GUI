import random
import arcade


class Enemy(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__("pictures\enemy.png")
        self.center_x = random.randint(0, w)
        self.center_y = h
        self.angle = -90
        self.width = 90
        self.height = 67.5
        self.speed = 0.8

    def move(self,accel):
        self.center_y -= self.speed
        self.speed += accel

class Missile(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__("pictures\missile.png")
        self.center_x = random.randint(0, w)
        self.center_y = h
        self.angle = 0
        self.width = 75
        self.height = 75
        self.speed = 0.75

    def move(self,accel):
        self.center_y -= self.speed
        self.speed += accel
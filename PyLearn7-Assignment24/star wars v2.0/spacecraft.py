import arcade
from bullet import Bullet
# from heart import Heart

class Spacecraft(arcade.Sprite):
    def __init__(self, w):
        super().__init__("D:\PyLearn7\Assignments\PyLearn7-Game\PyLearn7-Assignment14\pictures\my_spacecraft.png")
        self.center_x = w//2
        self.center_y = 80
        self.change_x = 0
        self.change_y = 0
        self.width = 100
        self.height = 100
        self.speed = 6
        self.game_width = w
        self.bullet_list = []
        

    def move(self):
        if self.change_x == -1:
            if self.center_x > 0:
                self.center_x = self.center_x - self.speed      # or self.center_x -= self.speed
        elif self.change_x == 1:
            if self.center_x < self.game_width:
                self.center_x = self.center_x + self.speed      # or self.center_x += self.speed

    def fire(self):
        new_bullet = Bullet(self)
        self.bullet_list.append(new_bullet)



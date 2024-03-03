import arcade


class Heart(arcade.Sprite):
    def __init__(self):
        super().__init__("D:\PyLearn7\Assignments\PyLearn7-Game\PyLearn7-Assignment14\pictures\heart.png")
        self.center_x = 0
        self.center_y = 20
        self.width = 25
        self.height = 25
    

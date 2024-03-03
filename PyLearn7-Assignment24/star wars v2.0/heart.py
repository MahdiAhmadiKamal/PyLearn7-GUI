import arcade


class Heart(arcade.Sprite):
    def __init__(self):
        super().__init__("pictures\heart.png")
        self.center_x = 0
        self.center_y = 20
        self.width = 25
        self.height = 25
    

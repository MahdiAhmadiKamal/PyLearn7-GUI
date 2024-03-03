import time
import threading
import arcade
from spacecraft import Spacecraft
from enemy import Enemy, Missile
from heart import Heart


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600, height=700, title="Star Wars Game")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png") 
        self.me = Spacecraft(self.width)
        # self.enemy = Enemy(self.width, self.height)
        self.enemies_list = []
        self.missiles_list = []
        # self.start_time = time.time()       #
        self.enemy_gap_time = 3               
        self.missile_gap_time = 5
        self.heart_list = [None, None, None]
        self.condition = ""
        self.score = 0
        self.shoot_sound = arcade.sound.load_sound(":resources:sounds/laser2.wav")
        self.explosion_sound = arcade.sound.load_sound(":resources:sounds/explosion2.wav")

        self.enemy_thread = threading.Thread(target=self.create_enemy)
        self.missile_thread = threading.Thread(target=self.create_enemy)
        self.enemy_thread.start()
        self.missile_thread.start()


    # methods
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width, self.height, self.background)
        arcade.draw_text(self.score, self.width-50, 15, arcade.color.WHITE, 20)
        self.me.draw()
        # self.my_hearts.draw()
        # self.enemy.draw()
        for enemy in self.enemies_list:
            enemy.draw()

        for missile in self.missiles_list:
            missile.draw()

        for bullet in self.me.bullet_list:
            bullet.draw()

        for heart in self.heart_list: 
            heart.draw()

        if self.condition == "Game Over":
            arcade.start_render()
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text("Game Over",self.width/4, self.height/2, arcade.color.WHITE, 45)
     
    def on_key_press(self, symbol: int, modifiers: int):
        
        if symbol==arcade.key.A or symbol==arcade.key.LEFT:    #left direction
            # self.me.move("L")
            self.me.change_x = -1
        elif symbol==arcade.key.D or symbol==arcade.key.RIGHT:   #right direction
            # self.me.move("R")
            self.me.change_x = 1
        elif symbol==arcade.key.S or symbol==arcade.key.DOWN:   #stop
            self.me.change_x = 0
        elif symbol==arcade.key.SPACE:
            self.me.fire()
            arcade.sound.play_sound(self.shoot_sound)

    def on_key_release(self, symbol: int, modifiers: int):
        self.me.change_x = 0   

    def create_enemy(self):
        while True:
            self.new_enemy = Enemy(self.width, self.height)
            self.new_missile = Missile(self.width, self.height)
            self.enemies_list.append(self.new_enemy)
            self.missiles_list.append(self.new_missile)
            time.sleep(self.enemy_gap_time)
            time.sleep(self.missile_gap_time)
       
    def on_update(self, delta_time: float):
        # self.end_time = time.time()             #
        
        for i in range(len(self.heart_list)):
            self.heart_list[i]=Heart()
            self.heart_list[i].center_x=30*i+30

        for enemy in self.enemies_list:
            if arcade.check_for_collision(self.me, enemy):
                self.condition = "Game Over"
                # exit(0)

        for missile in self.missiles_list:
            if arcade.check_for_collision(self.me, missile):
                self.condition = "Game Over"

        for enemy in self.enemies_list:
            if len(self.heart_list) == 0:
                self.condition = "Game Over"
                # exit(0)
            elif enemy.center_y + enemy.height/2 <0:
          
                self.enemies_list.remove(enemy)
                self.heart_list.remove(self.heart_list[-1])

        for missile in self.missiles_list:
            if len(self.heart_list) == 0:
                self.condition = "Game Over"

            elif missile.center_y + missile.height/2 <0:
          
                self.missiles_list.remove(missile)
                self.heart_list.remove(self.heart_list[-1])
                
        for enemy in self.enemies_list:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(enemy, bullet):
                    self.enemies_list.remove(enemy)
                    self.me.bullet_list.remove(bullet)
                    self.score += 1
                    arcade.sound.play_sound(self.explosion_sound)

        for missile in self.missiles_list:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(missile, bullet):
                    self.missiles_list.remove(missile)
                    self.me.bullet_list.remove(bullet)
                    self.score += 1
                    arcade.sound.play_sound(self.explosion_sound)
                    

        # self.enemy.move()
        self.me.move()
        
        for enemy in self.enemies_list:
            enemy.move(0.0)

        for missile in self.missiles_list:
            missile.move(0.015)

        # for enemy in self.enemies_list:
        #     enemy.move()

        for bullet in self.me.bullet_list:
            bullet.move()

        # for enemy in self.enemies_list:
        #     if enemy.center_y + enemy.height/2 < 0:  
        #        self.enemies_list.remove(enemy)  

        for bullet in self.me.bullet_list:
            if bullet.center_y <0:
                self.me.bullet_list.remove(bullet)

        # if (self.end_time-self.start_time) >= self.enemy_gap_time:      #
        #     self.new_enemy = Enemy(self.width, self.height)             #
        #     self.enemies_list.append(self.new_enemy)                    #
        #     self.start_time=time.time()                                 #

        # if random.randint(1, 80)==6:   
        #     self.new_enemy = Enemy(self.width, self.height)
        #     self.enemies_list.append(self.new_enemy)

window = Game()
arcade.run()

import arcade

# -- constants -- #
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_SPEED = 2

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab7")
        self.ball = Ball(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3, 0, 0, 20, (207,97,195))
        self.diamond = Diamond(SCREEN_WIDTH / 2 + 100, SCREEN_HEIGHT / 3, 0, 0, 30, 30, (151,97,207), 90)
    
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color((97,186,207))
        arcade.draw_lrtb_rectangle_filled(
            0,
            SCREEN_WIDTH,
            SCREEN_HEIGHT / 4,
            0,
            (78,173,68)
        )
        self.ball.draw()
        self.diamond.draw()

    def on_update(self, delta_time):
        self.ball.update()
        self.diamond.update()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.change_y += BALL_SPEED
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.diamond.change_y += BALL_SPEED
        elif key == arcade.key.DOWN:
            self.diamond.change_y -= BALL_SPEED
        elif key == arcade.key.LEFT:
            self.diamond.change_x -= BALL_SPEED
        elif key == arcade.key.RIGHT:
            self.diamond.change_x += BALL_SPEED

class Ball():
    def __init__(self, pos_x, pos_y, change_x, change_y, size, colour):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.change_x = change_x
        self.change_y = change_y
        self.size = size
        self.colour = colour

    def draw(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.size, self.colour)
        
    def update(self):
        self.pos_x += self.change_x
        self.pos_y += self.change_y

        if self.pos_x < self.size:
            self.pos_x = self.size
        if self.pos_x > SCREEN_WIDTH - self.size:
            self.pos_x = SCREEN_WIDTH - self.size
        
        if self.pos_y < self.size:
            self.pos_y = self.size
        if self.pos_y > SCREEN_HEIGHT - self.size:
            self.change_y = -BALL_SPEED
        elif self.pos_y < SCREEN_HEIGHT / 4 - self.size:
            self.change_y = BALL_SPEED

class Diamond():
    def __init__(self, pos_x, pos_y, change_x, change_y, width, height, colour, angle):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.colour = colour
        self.angle = angle

    def draw(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.width, self.height, self.colour, self.angle)

    def update(self):
        self.pos_x += self.change_x
        self.pos_y += self.change_y
        self.angle += BALL_SPEED

        if self.pos_x < self.width:
            self.pos_x = self.width
        if self.pos_x > SCREEN_WIDTH - self.width:
            self.pos_x = -BALL_SPEED
        
        if self.pos_y < self.height:
            self.pos_y = self.height
        if self.pos_y > SCREEN_HEIGHT - self.height:
            self.change_y = -BALL_SPEED
        elif self.pos_y < SCREEN_HEIGHT / 4 - self.height:
            self.change_y = BALL_SPEED

def main():
    window = Game()
    arcade.run()

main()
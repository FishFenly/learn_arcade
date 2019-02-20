## Lab 8 - Sprites ##
import random
import arcade

# -- constants -- #
SCALE_PLAYER = 5
SCALE_OBJECT = 3
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
COUNT_OBJECT = 2
SPEED = 2

class Player(arcade.Sprite):
    """ The player class """
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.angle = self.change_angle

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class Rock(arcade.Sprite):
    """ Bad sprite - A rock, subclass of Object """
    def reset_pos(self):
        self.center_y = random.randrange(0, SCREEN_HEIGHT - SCALE_OBJECT)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class Metal(arcade.Sprite):
    """ Good sprite - Some scrap metal, subclass of Object """
    def update(self):
        pass

class Game(arcade.Window):
    """ Main game class """
    def __init__(self, width, height, title):
        """ Initialise the game and its objects """
        super().__init__(width, height, title)

        self.player_list = None
        self.rock_list = None
        self.metal_list = None
        self.player_sprite = None
        self.score = 0
        self.done = False

        self.hitrock_sound = arcade.load_sound("assets/explosion.wav")
        self.hitmetal_sound = arcade.load_sound("assets/good.wav")

        self.set_mouse_visible(False)

        arcade.set_background_color((0,0,0))

    def setup(self):
        """ 
        Setup the game, create sprites and other game items.
        Seperated from initialisation logic so that it can be called to restart. 
        """
        # Setup sprite lists
        self.player_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()
        self.metal_list = arcade.SpriteList()

        # reset the score to 0
        self.score = 0

        # setup the player sprite's image and location
        self.player_sprite = Player("assets/ship.png", SCALE_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(COUNT_OBJECT):
            rock = Rock("assets/rock.png", SCALE_OBJECT)
            metal = Metal("assets/metal.png", SCALE_OBJECT)
            rock.center_x = random.randrange(SCREEN_WIDTH)
            rock.center_y = random.randrange(SCREEN_HEIGHT)
            metal.center_x = random.randrange(SCREEN_WIDTH)
            metal.center_y = random.randrange(SCREEN_HEIGHT)
            rock.change_x = random.randrange(-3, 4)
            rock.change_y = random.randrange(-3, 4)

            self.rock_list.append(rock)
            self.metal_list.append(metal)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.metal_list.draw()
        self.rock_list.draw()

        # Score text
        arcade.draw_text(
            "Score: {}".format(self.score), # text value
            10, # start x position
            20,  # start y position
            (255,255,255), # text colour
            14 # text font size
        )
        if self.done:
            arcade.draw_text(
                "GAME OVER!",
                SCREEN_WIDTH / 3, # start x position
                SCREEN_HEIGHT / 2,  # start y position
                (246,10,37), # text colour
                26 #1 text font size
            )

    def update(self, deltatime):
        if not self.done:
            self.player_list.update()
            self.rock_list.update()
            self.metal_list.update()

        rock_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite,
            self.rock_list
        )
        metal_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite,
            self.metal_list
        )
        for rock in rock_hit_list:
            self.score -= 1
            rock.kill()
            #arcade.play_sound(self.hitrock_sound)
        for metal in metal_hit_list:
            self.score += 1
            metal.kill()
            #arcade.play_sound(self.hitmetal_sound)
        if len(self.metal_list) == 0:
            self.done = True

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y += SPEED
            self.player_sprite.change_angle = 90
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y -= SPEED
            self.player_sprite.change_angle = 270
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x -= SPEED
            self.player_sprite.change_angle = 180
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x += SPEED
            self.player_sprite.change_angle = 0
        elif key == arcade.key.Q:
            quit()

    # def on_key_release(self, key, modifiers):
    #     if key == arcade.key.LEFT or key == arcade.key.RIGHT:
    #         self.player_sprite.change_x = 0
    #     elif key == arcade.key.UP or key == arcade.key.DOWN:
    #         self.player_sprite.change_y = 0


if __name__ == "__main__":
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8")
    game.setup()
    arcade.run()
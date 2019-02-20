import random
import arcade

#--- constants ---#
SPRITE_SCALE_PLAYER = 0.5
SPRITE_SCALE_COIN = 0.2
COIN_COUNT = 200
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite example")

        self.player_list = None # put sprites in lists. Even with one sprite you should still
        self.coin_list = None # put them in lists because "SpriteList" optimises drawing

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ 
        This setup function will create sprites and get the game setup.
        It's not called automatically so we can call it again to restart the game.
        """

        self.player_list = arcade.SpriteList() # http://arcade.academy/arcade.html#arcade.sprite.SpriteList
        self.coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("assets/character.png", SPRITE_SCALE_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("assets/coin_01.png", SPRITE_SCALE_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()

        # Put text on the screen for the score 
        arcade.draw_text("Score: {}".format(self.score), 10, 20, (255,255,255), 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handles mouse movement """

        # Move the center of the player sprite with the mouse

        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_key_press(self, key, modifiers):
        if key == arcade.key.Q:
            exit()

    def update(self, delta_time):
        """
        1. update each sprite
        2. check if player is touching a coin
        3. remove any coins colliding with player and append score
        """
        
        self.coin_list.update() # call update for all coin sprites
        
        coin_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, 
            self.coin_list
        ) # create a list of all sprites that have hit the player by comparing the two sprites x + y

        for coin in coin_hit_list:
            coin.kill() # sprite classes have a kill method to remove it from existence
            self.score += 1

def app():
    window = Game()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    app()
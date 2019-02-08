import arcade
import learn_arcade.constants as c

def app():
    arcade.open_window(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.SCREEN_TITLE)
    arcade.set_background_color((62,199,216))

    arcade.start_render()

    arcade.finish_render()

    arcade.run()
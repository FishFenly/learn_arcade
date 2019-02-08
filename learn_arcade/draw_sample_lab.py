import arcade
import learn_arcade.constants as c

def app():
    arcade.open_window(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.SCREEN_TITLE)
    arcade.set_background_color((62,199,216))

    arcade.start_render()

    # --- a tree scene ---

    # draw the grass, which is the full width of the window and a quarter of the height
    arcade.draw_lrtb_rectangle_filled(
        0,
        c.SCREEN_WIDTH,
        c.SCREEN_HEIGHT / 4,
        0,
        (59,192,52)
    )

    # draw the first tree
    arcade.draw_rectangle_filled(
        c.SCREEN_WIDTH - 100,
        c.SCREEN_HEIGHT - 100,
        10,
        10,
        (),
        90
    )

    arcade.finish_render()

    arcade.run()
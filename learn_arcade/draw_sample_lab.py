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
    # draw the sun
    arcade.draw_circle_filled(
        c.SCREEN_WIDTH / 1.3,
        c.SCREEN_HEIGHT / 1.1,
        50,
        (231,229,88)
    )

    # draw the first tree trunk
    arcade.draw_rectangle_filled(
        c.SCREEN_WIDTH / 6,
        c.SCREEN_HEIGHT / 2,
        30,
        300,
        (92,76,62)
    )
    # first tree leaves
    arcade.draw_circle_filled(
        c.SCREEN_WIDTH / 6,
        c.SCREEN_HEIGHT / 2 + 150,
        100,
        (51,100,54)
    )
    # second tree trunk
    arcade.draw_rectangle_filled(
        c.SCREEN_WIDTH / 1.2,
        c.SCREEN_HEIGHT / 2,
        30,
        300,
        (92,76,62)
    )
    # second tree leaves
    arcade.draw_circle_filled(
        c.SCREEN_WIDTH / 1.2,
        c.SCREEN_HEIGHT / 2 + 150,
        100,
        (51,100,54)
    )

    arcade.finish_render()

    arcade.run()
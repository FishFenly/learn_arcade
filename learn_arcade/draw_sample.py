import arcade
import learn_arcade.constants as c

def run():
    arcade.open_window(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.SCREEN_TITLE) # draws the window

    arcade.set_background_color((255,255,255)) # clear the screen and set a background colour
    arcade.start_render() # get ready to draw

    # draw a rect by specifying the cords of each edge
    arcade.draw_lrtb_rectangle_filled(
        5, # x cord of left edge
        35, # x cord of right edge
        590, # y cord for top edge
        570, # y cord for bottom edge
        (43,222,31) # colour
    )
    # draw a rect by specifying its center x,y then its heigh and width
    arcade.draw_rectangle_filled(
        100, # x cord of rect center
        520, # y cord of rect center
        45, # width
        25, # height
        (31,149,222) # colour
    )
    # draw a rotated rect
    arcade.draw_rectangle_filled(
        200, # x cord of rect center
        520, # y cord of rect center
        45, # width
        25, # height
        (222,149,31), # colour
        45 # rotation degrees
    )

    arcade.finish_render() # finish

    arcade.run() # starts the game loop to keep everything open
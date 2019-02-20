import arcade
import learn_arcade.constants as c

def draw_sea():
    """ The sea """
    arcade.draw_lrtb_rectangle_filled(
        0,
        c.SCREEN_WIDTH,
        c.SCREEN_HEIGHT / 1.5,
        0,
        (27,244,220)
    )

def draw_fish(x, y):
    """ A fish, takes the x and y cords """
    fish_colour = (244,196,27)
    arcade.draw_ellipse_filled(
        x,
        y,
        20,
        10,
        fish_colour
    )

def draw_sun():
    """ The sun """
    colour = (241,244,27)
    arcade.draw_circle_filled(
        c.SCREEN_WIDTH / 1.3,
        c.SCREEN_HEIGHT / 1.1,
        50,
        colour
    )

def draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    draw_sun()
    draw_sea()
    draw_fish(draw.fish1_x,50)
    draw_fish(draw.fish2_x,300)
    draw_fish(draw.fish3_x,150)
    draw.fish1_x +=1
    draw.fish2_x +=1
    draw.fish3_x +=1

draw.fish1_x = 20
draw.fish2_x = 100
draw.fish3_x = 500

def main():
    arcade.open_window(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.SCREEN_TITLE)
    arcade.set_background_color((27,224,244))

    arcade.schedule(draw, 1/60) # call the draw function every 60th of a second
    arcade.run()

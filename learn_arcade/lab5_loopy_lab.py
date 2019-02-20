import arcade

def draw_section_outlines():
    # bottom square
    arcade.draw_rectangle_outline(150, 150, 300, 300, (0,0,0)) #1
    arcade.draw_rectangle_outline(450, 150, 300, 300, (0,0,0)) #2
    arcade.draw_rectangle_outline(750, 150, 300, 300, (0,0,0)) #3
    arcade.draw_rectangle_outline(1050, 150, 300, 300,(0,0,0)) #4

    # top square borders
    arcade.draw_rectangle_outline(150, 450, 300, 300, (0,0,0)) #5
    arcade.draw_rectangle_outline(450, 450, 300, 300, (0,0,0)) #6
    arcade.draw_rectangle_outline(750, 450, 300, 300, (0,0,0)) #7
    arcade.draw_rectangle_outline(1050, 450, 300, 300,(0,0,0)) #8

def draw_section_1():
    for row in range(30):
        for column in range(30):
            x = column * 10 + 6
            y = row * 10 + 6
            arcade.draw_rectangle_filled(x, y, 5, 5, (255,255,255))

def draw_section_2():
    for row in range(30):
        for column in range(30):
            x = ((column * 10) + 6) + 300
            y = (row * 10) + 6
            if (x%4) == 2:
                arcade.draw_rectangle_filled(x, y, 5, 5, (255,255,255))
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, (0,0,0))

def draw_section_3():
    for row in range(30):
        for column in range(30):
            x = ((column * 10) + 6) + 600
            y = (row * 10) + 6
            if (y%4) == 2:
                arcade.draw_rectangle_filled(x, y, 5, 5, (255,255,255))
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, (0,0,0))

def draw_section_4():
    for row in range(30):
        for column in range(30):
            x = ((column * 10) + 6) + 900
            y = (row * 10) + 6
            if (x%4) and (y%4) == 2:
                arcade.draw_rectangle_filled(x, y, 5, 5, (255,255,255))
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, (0,0,0))
            print("x is {}, y is {}".format(x,y))


def draw_section_5():
    for row in range(30):
        for column in range(row, 30, 1):
            x = (column * 10) + 6
            y = ((row * 10) + 6) + 300
            arcade.draw_rectangle_filled(x, y, 5, 5, (255,255,255))

def draw_section_6():
    for row in range(30):
        for column in range(row, 0, -1):
            x = ((column * 10) + 6) + 300
            y = ((row * 10) + 6) + 300
            arcade.draw_rectangle_filled(x, y, 5, 5, (255,255,255))

def draw_section_7():
    for row in range(30):
        for column in range(row + 1):
            x = ((column * 10) + 6) + 600
            y = ((row * 10) + 6) + 300
            arcade.draw_rectangle_filled(x, y, 5, 5, (255,255,255))


def draw_section_8():
    pass

def app():
    arcade.open_window(1200, 600, "sure")
    arcade.set_background_color((62,199,216))

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()
    arcade.run()

app()

# score = 16
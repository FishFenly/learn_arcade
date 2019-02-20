Arcade Package API
This page documents the Application Programming Interface (API) for the Python Arcade library.

For example code, see Example Code.

Submodules
Window Commands Module
This submodule has functions that control opening, closing, rendering, and otherwise managing windows. It also has commands for scheduling pauses and scheduling interval functions.

arcade.window_commands.close_window()[source]
Closes the current window, and then runs garbage collection. The garbage collection is necessary to prevent crashing when opening/closing windows rapidly (usually during unit tests).

arcade.window_commands.create_orthogonal_projection(left, right, bottom, top, near, far, dtype=None)[source]
Creates an orthogonal projection matrix. :param float left: The left of the near plane relative to the plane’s centre. :param float right: The right of the near plane relative to the plane’s centre. :param float top: The top of the near plane relative to the plane’s centre. :param float bottom: The bottom of the near plane relative to the plane’s centre. :param float near: The distance of the near plane from the camera’s origin. It is recommended that the near plane is set to 1.0 or above to avoid rendering issues at close range. :param float far: The distance of the far plane from the camera’s origin. :param dtype: :rtype: numpy.array :return: A projection matrix representing the specified orthogonal perspective. .. seealso:: http://msdn.microsoft.com/en-us/library/dd373965(v=vs.85).aspx

arcade.window_commands.finish_render()[source]
Swap buffers and displays what has been drawn. If programs use derive from the Window class, this function is automatically called.

arcade.window_commands.get_projection()[source]
arcade.window_commands.get_scaling_factor(window)[source]
arcade.window_commands.get_viewport() -> (<class 'float'>, <class 'float'>, <class 'float'>, <class 'float'>)[source]
Get the current viewport settings.

arcade.window_commands.get_window() → Optional[pyglet.window.BaseWindow][source]
Return a handle to the current window.

Param:	None
Return window:	Handle to the current window.
Raises:	None
arcade.window_commands.pause(seconds: numbers.Number)[source]
Pause for the specified number of seconds. This is a convenience function that just calls time.sleep()

Parameters:	seconds (float) – Time interval to pause in seconds.
arcade.window_commands.quick_run(time_to_pause: numbers.Number)[source]
Only run the application for the specified time in seconds. Useful for unit testing or continuous integration (CI) testing where there is no user interaction.

Args:
time_to_pause:	Number of seconds to pause before automatically closing.
arcade.window_commands.run()[source]
Run the main loop. After the window has been set up, and the event hooks are in place, this is usually one of the last commands on the main program.

arcade.window_commands.schedule(function_pointer: Callable, interval: numbers.Number)[source]
Schedule a function to be automatically called every interval seconds.

Args:
function_pointer:
 	Pointer to the function to be called.
interval:	Interval to call the function.
Returns:
None
Raises:
None
arcade.window_commands.set_background_color(color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]])[source]
This specifies the background color of the window.

Args:
color (tuple):	List of 3 or 4 bytes in RGB/RGBA format.
Returns:
None
Raises:
None
arcade.window_commands.set_viewport(left: numbers.Number, right: numbers.Number, bottom: numbers.Number, top: numbers.Number)[source]
This sets what coordinates the window will cover.

By default, the lower left coordinate will be (0, 0) and the top y coordinate will be the height of the window in pixels, and the right x coordinate will be the width of the window in pixels.

If a program is making a game where the user scrolls around a larger world, this command can help out.

Note: It is recommended to only set the view port to integer values that line up with the pixels on the screen. Otherwise if making a tiled game the blocks may not line up well, creating rectangle artifacts.

Args:
left:	Left-most (smallest) x value.
right:	Right-most (largest) x value.
bottom:	Bottom (smallest) y value.
top:	Top (largest) y value.
Returns:
None
Raises:
None
arcade.window_commands.set_window(window: pyglet.window.BaseWindow)[source]
Set a handle to the current window.

Args:
window:	Handle to the current window.
arcade.window_commands.start_render()[source]
Get set up to render. Required to be called before drawing anything to the screen.

Draw Commands Module
This module contains commands for basic graphics drawing commands. (Drawing primitives.)

Many of these commands are slow, because they load everything to the graphics card each time a shape is drawn. For faster drawing, see the Buffered Draw Commands.

class arcade.draw_commands.Texture(name, image=None)[source]
Bases: object

Class that represents a texture. Usually created by the load_texture or load_textures commands.

Attributes:
id:	ID of the texture as assigned by OpenGL
width:	Width of the texture image in pixels
height:	Height of the texture image in pixels
draw(center_x: float, center_y: float, width: float, height: float, angle: float = 0, alpha: float = 1, transparent: bool = True, repeat_count_x=1, repeat_count_y=1)[source]
arcade.draw_commands.draw_arc_filled(center_x: float, center_y: float, width: float, height: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], start_angle: float, end_angle: float, tilt_angle: float = 0, num_segments: int = 128)[source]
Draw a filled in arc. Useful for drawing pie-wedges, or Pac-Man.

Args:
center_x:	x position that is the center of the arc.
center_y:	y position that is the center of the arc.
width:	width of the arc.
height:	height of the arc.
color:	color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
start_angle:	start angle of the arc in degrees.
end_angle:	end angle of the arc in degrees.
tilt_angle:	angle the arc is tilted.
Returns:
None
Raises:
None
arcade.draw_commands.draw_arc_outline(center_x: float, center_y: float, width: float, height: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], start_angle: float, end_angle: float, border_width: float = 1, tilt_angle: float = 0, num_segments: int = 128)[source]
Draw the outside edge of an arc. Useful for drawing curved lines.

Args:
center_x:	x position that is the center of the arc.
center_y:	y position that is the center of the arc.
width:	width of the arc.
height:	height of the arc.
color:	color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
start_angle:	start angle of the arc in degrees.
end_angle:	end angle of the arc in degrees.
border_width:	width of line in pixels.
angle:	angle the arc is tilted.
Returns:
None
Raises:
None
arcade.draw_commands.draw_circle_filled(center_x: float, center_y: float, radius: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]])[source]
Draw a filled-in circle.

Args:
center_x:	x position that is the center of the circle.
center_y:	y position that is the center of the circle.
radius:	width of the circle.
color:	color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
num_segments (int):
 	float of triangle segments that make up this circle. Higher is better quality, but slower render time.
Returns:
None
Raises:
None
arcade.draw_commands.draw_circle_outline(center_x: float, center_y: float, radius: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], border_width: float = 1)[source]
Draw the outline of a circle.

Args:
center_x:	x position that is the center of the circle.
center_y:	y position that is the center of the circle.
radius:	width of the circle.
color:	color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
border_width:	Width of the circle outline in pixels.
num_segments:	float of triangle segments that make up this circle. Higher is better quality, but slower render time.
Returns:
None
Raises:
None
arcade.draw_commands.draw_ellipse_filled(center_x: float, center_y: float, width: float, height: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], tilt_angle: float = 0, num_segments: int = 128)[source]
Draw a filled in ellipse.

Args:
center_x:	x position that is the center of the circle.
center_y:	y position that is the center of the circle.
height:	height of the ellipse.
width:	width of the ellipse.
color:	color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
angle:	Angle in degrees to tilt the ellipse.
num_segments:	float of triangle segments that make up this circle. Higher is better quality, but slower render time.
Returns:
None
Raises:
None
arcade.draw_commands.draw_ellipse_outline(center_x: float, center_y: float, width: float, height: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], border_width: float = 1, tilt_angle: float = 0, num_segments=128)[source]
Draw the outline of an ellipse.

Args:
center_x:	x position that is the center of the circle.
center_y:	y position that is the center of the circle.
height:	height of the ellipse.
width:	width of the ellipse.
color:	color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
border_width:	Width of the circle outline in pixels.
tilt_angle:	Angle in degrees to tilt the ellipse.
Returns:
None
Raises:
None
arcade.draw_commands.draw_line(start_x: float, start_y: float, end_x: float, end_y: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], line_width: float = 1)[source]
Draw a line.

Args:
start_x:	x position of line starting point.
start_y:	y position of line starting point.
end_x:	x position of line ending point.
end_y:	y position of line ending point.
color:	color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
border_width:	Width of the line in pixels.
Returns:
None
Raises:
None
arcade.draw_commands.draw_line_strip(point_list: Union[Tuple[Union[Tuple[float, float], List[float]], ...], List[Union[Tuple[float, float], List[float]]]], color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], line_width: float = 1)[source]
Draw a multi-point line.

Args:
point_list: color: line_width:
arcade.draw_commands.draw_lines(point_list: Union[Tuple[Union[Tuple[float, float], List[float]], ...], List[Union[Tuple[float, float], List[float]]]], color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], line_width: float = 1)[source]
Draw a set of lines.

Draw a line between each pair of points specified.

Args:
point_list:	List of points making up the lines. Each point is in a list. So it is a list of lists.
color:	color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
border_width:	Width of the line in pixels.
Returns:
None
Raises:
None
arcade.draw_commands.draw_lrtb_rectangle_filled(left: float, right: float, top: float, bottom: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]])[source]
Draw a rectangle by specifying left, right, top, and bottom edges.

Args:
left:	The x coordinate of the left edge of the rectangle.
right:	The x coordinate of the right edge of the rectangle.
top:	The y coordinate of the top of the rectangle.
bottom:	The y coordinate of the rectangle bottom.
color:	The color of the rectangle.
border_width:	The width of the border in pixels. Defaults to one.
Returns:
None
Raises:
AttributeErrror:
 	Raised if left > right or top < bottom.
arcade.draw_commands.draw_lrtb_rectangle_outline(left: float, right: float, top: float, bottom: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], border_width: float = 1)[source]
Draw a rectangle by specifying left, right, top, and bottom edges.

Args:
left:	The x coordinate of the left edge of the rectangle.
right:	The x coordinate of the right edge of the rectangle.
top:	The y coordinate of the top of the rectangle.
bottom:	The y coordinate of the rectangle bottom.
color:	The color of the rectangle.
border_width:	The width of the border in pixels. Defaults to one.
Returns:
None
Raises:
AttributeErrror:
 	Raised if left > right or top < bottom.
arcade.draw_commands.draw_parabola_filled(start_x: float, start_y: float, end_x: float, height: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], tilt_angle: float = 0)[source]
Draws a filled in parabola.

Args:
start_x:	The starting x position of the parabola
start_y:	The starting y position of the parabola
end_x:	The ending x position of the parabola
height:	The height of the parabola
color:	The color of the parabola
tilt_angle:	The angle of the tilt of the parabola
Returns:
None
Raises:
None
arcade.draw_commands.draw_parabola_outline(start_x: float, start_y: float, end_x: float, height: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], border_width: float = 1, tilt_angle: float = 0)[source]
Draws the outline of a parabola.

Args:
start_x:	The starting x position of the parabola
start_y:	The starting y position of the parabola
end_x:	The ending x position of the parabola
height:	The height of the parabola
color:	The color of the parabola
border_width:	The width of the parabola
tile_angle:	The angle of the tilt of the parabola
Returns:
None
Raises:
None
arcade.draw_commands.draw_point(x: float, y: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], size: float)[source]
Draw a point.

Args:
x:	x position of point.
y:	y position of point.
color:	color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
size:	Size of the point in pixels.
Returns:
None
Raises:
None
arcade.draw_commands.draw_points(point_list: Union[Tuple[Union[Tuple[float, float], List[float]], ...], List[Union[Tuple[float, float], List[float]]]], color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], size: float = 1)[source]
Draw a set of points.

Args:
point_list:	List of points Each point is in a list. So it is a list of lists.
color:	color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
size:	Size of the point in pixels.
Returns:
None
Raises:
None
arcade.draw_commands.draw_polygon_filled(point_list: Union[Tuple[Union[Tuple[float, float], List[float]], ...], List[Union[Tuple[float, float], List[float]]]], color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]])[source]
Draw a polygon that is filled in.

Args:
point_list:	List of points making up the lines. Each point is in a list. So it is a list of lists.
color:	color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
Returns:
None
Raises:
None
arcade.draw_commands.draw_polygon_outline(point_list: Union[Tuple[Union[Tuple[float, float], List[float]], ...], List[Union[Tuple[float, float], List[float]]]], color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], line_width: float = 1)[source]
Draw a polygon outline. Also known as a “line loop.”

Args:
point_list:	List of points making up the lines. Each point is in a list. So it is a list of lists.
color:	color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
border_width:	Width of the line in pixels.
Returns:
None
Raises:
None
arcade.draw_commands.draw_rectangle_filled(center_x: float, center_y: float, width: float, height: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], tilt_angle: float = 0)[source]
Draw a filled-in rectangle.

Args:
center_x:	x coordinate of rectangle center.
center_y:	y coordinate of rectangle center.
width:	width of the rectangle.
height:	height of the rectangle.
color:	color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
angle:	rotation of the rectangle. Defaults to zero.
arcade.draw_commands.draw_rectangle_outline(center_x: float, center_y: float, width: float, height: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], border_width: float = 1, tilt_angle: float = 0)[source]
Draw a rectangle outline.

Args:
x:	x coordinate of top left rectangle point.
y:	y coordinate of top left rectangle point.
width:	width of the rectangle.
height:	height of the rectangle.
color:	color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
border_width:	width of the lines, in pixels.
angle:	rotation of the rectangle. Defaults to zero.
Returns:
None
Raises:
None
arcade.draw_commands.draw_texture_rectangle(center_x: float, center_y: float, width: float, height: float, texture: arcade.draw_commands.Texture, angle: float = 0, alpha: float = 1, repeat_count_x=1, repeat_count_y=1)[source]
Draw a textured rectangle on-screen.

Args:
center_x:	x coordinate of rectangle center.
center_y:	y coordinate of rectangle center.
width:	width of the rectangle.
height:	height of the rectangle.
texture:	identifier of texture returned from load_texture() call
angle:	rotation of the rectangle. Defaults to zero.
alpha:	Transparency of image.
Returns:
None
Raises:
None
arcade.draw_commands.draw_triangle_filled(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]])[source]
Draw a filled in triangle.

Args:
x1:	x value of first coordinate.
y1:	y value of first coordinate.
x2:	x value of second coordinate.
y2:	y value of second coordinate.
x3:	x value of third coordinate.
y3:	y value of third coordinate.
color:	Color of triangle.
Returns:
None
Raises:
None
arcade.draw_commands.draw_triangle_outline(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], border_width: float = 1)[source]
Draw a the outline of a triangle.

Args:
x1:	x value of first coordinate.
y1:	y value of first coordinate.
x2:	x value of second coordinate.
y2:	y value of second coordinate.
x3:	x value of third coordinate.
y3:	y value of third coordinate.
color:	Color of triangle.
border_width:	Width of the border in pixels. Defaults to 1.
Returns:
None
Raises:
None
arcade.draw_commands.draw_xywh_rectangle_filled(bottom_left_x: float, bottom_left_y: float, width: float, height: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]])[source]
Draw a filled rectangle extending from bottom left to top right

Args:
bottom_left_x:	The x coordinate of the left edge of the rectangle.
bottom_left_y:	The y coordinate of the bottom of the rectangle.
width:	The width of the rectangle.
height:	The height of the rectangle.
color:	The color of the rectangle.
Returns:
None
Raises:
None
arcade.draw_commands.draw_xywh_rectangle_outline(bottom_left_x: float, bottom_left_y: float, width: float, height: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], border_width: float = 1)[source]
Draw a rectangle extending from bottom left to top right

Args:
bottom_left_x:	The x coordinate of the left edge of the rectangle.
bottom_left_y:	The y coordinate of the bottom of the rectangle.
width:	The width of the rectangle.
height:	The height of the rectangle.
color:	The color of the rectangle.
border_width:	The width of the border in pixels. Defaults to one.
Returns:
None
Raises:
None
arcade.draw_commands.draw_xywh_rectangle_textured(bottom_left_x: float, bottom_left_y: float, width: float, height: float, texture: arcade.draw_commands.Texture, angle: float = 0, alpha: float = 1, transparent: bool = True, repeat_count_x=1, repeat_count_y=1)[source]
Draw a texture extending from bottom left to top right.

Args:
bottom_left_x:	The x coordinate of the left edge of the rectangle.
bottom_left_y:	The y coordinate of the bottom of the rectangle.
width:	The width of the rectangle.
height:	The height of the rectangle.
texture:	identifier of texture returned from load_texture() call
angle:	rotation of the rectangle. Defaults to zero.
alpha:	Transparency of image.
Returns:
None
Raises:
None
arcade.draw_commands.get_four_byte_color(color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]]) → Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]][source]
Given a RGB list, it will return RGBA. Given a RGBA list, it will return the same RGBA.

Parameters:	color – Color
Returns:	color: Color
arcade.draw_commands.get_four_float_color(color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]]) -> (<class 'float'>, <class 'float'>, <class 'float'>, <class 'float'>)[source]
Given a 3 or 4 RGB/RGBA color where each color goes 0-255, this returns a RGBA list where each item is a scaled float from 0 to 1.

Parameters:	color –
Returns:	
arcade.draw_commands.get_image(x=0, y=0, width=None, height=None)[source]
Get an image from the screen. You can save the image like:

image = get_image() image.save(‘screenshot.png’, ‘PNG’)

arcade.draw_commands.get_pixel(x: int, y: int)[source]
Given an x, y, will return RGB color value of that point.

arcade.draw_commands.load_texture(file_name: str, x: float = 0, y: float = 0, width: float = 0, height: float = 0, mirrored: bool = False, flipped: bool = False, scale: float = 1) → arcade.draw_commands.Texture[source]
Load image from disk and create a texture.

Note, if the code is to load only part of the image, the given x, y coordinates will start with the origin (0, 0) in the upper left of the image. When drawing, Arcade uses (0, 0) in the lower left corner when drawing. Be careful about this reversal.

For a longer explanation of why computers sometimes start in the upper left, see: http://programarcadegames.com/index.php?chapter=introduction_to_graphics&lang=en#section_5

Args:
filename (str):	Name of the file to that holds the texture.
x (float):	X position of the crop area of the texture.
y (float):	Y position of the crop area of the texture.
width (float):	Width of the crop area of the texture.
height (float):	Height of the crop area of the texture.
scale (float):	Scale factor to apply on the new texture.
Returns:
The new texture.
Raises:
None
arcade.draw_commands.load_textures(file_name: str, image_location_list: Union[Tuple[Union[Tuple[float, float], List[float]], ...], List[Union[Tuple[float, float], List[float]]]], mirrored: bool = False, flipped: bool = False) → List[arcade.draw_commands.Texture][source]
Load a set of textures off of a single image file.

Note, if the code is to load only part of the image, the given x, y coordinates will start with the origin (0, 0) in the upper left of the image. When drawing, Arcade uses (0, 0) in the lower left corner when drawing. Be careful about this reversal.

For a longer explanation of why computers sometimes start in the upper left, see: http://programarcadegames.com/index.php?chapter=introduction_to_graphics&lang=en#section_5

Args:
file_name:	Name of the file.
image_location_list:
 	List of image locations. Each location should be a list of four floats. [x, y, width, height].
mirrored=False:	If set to true, the image is mirrored left to right.
flipped=False:	If set to true, the image is flipped upside down.
Returns:
list:	List of textures loaded.
Raises:
SystemError:	
arcade.draw_commands.make_transparent_color(color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], transparency: float)[source]
Given a RGB color, along with an alpha, returns a RGBA color tuple.

arcade.draw_commands.rotate_point(x: float, y: float, cx: float, cy: float, angle: float) -> (<class 'float'>, <class 'float'>)[source]
Rotate a point around a center.

Parameters:	
x – x value of the point you want to rotate
y – y value of the point you want to rotate
cx – x value of the center point you want to rotate around
cy – y value of the center point you want to rotate around
angle – Angle, in degrees, to rotate
Returns:	
Return rotated (x, y) pair

arcade.draw_commands.trim_image(image: <module 'PIL.Image' from 'c:\\program files (x86)\\python37-32\\lib\\site-packages\\PIL\\Image.py'>) → <module 'PIL.Image' from 'c:\\program files (x86)\\python37-32\\lib\\site-packages\\PIL\\Image.py'>[source]
Returns an image with extra whitespace cropped out.

Buffered Draw Commands Module
Drawing commands that use the VBOs.

This module contains commands for basic graphics drawing commands, but uses Vertex Buffer Objects. This keeps the vertices loaded on the graphics card for much faster render times.

class arcade.buffered_draw_commands.Shape[source]
Bases: object

draw()[source]
class arcade.buffered_draw_commands.ShapeElementList[source]
Bases: typing.Generic

A program can put multiple drawing primitives in a ShapeElementList, and then move and draw them as one. Do this when you want to create a more complex object out of simpler primitives. This also speeds rendering as all objects are drawn in one operation.

angle
Get the angle of the ShapeElementList in degrees.

append(item: T)[source]
Add a new shape to the list.

center_x
Get the center x coordinate of the ShapeElementList.

center_y
Get the center y coordinate of the ShapeElementList.

draw()[source]
Draw everything in the list.

move(change_x: float, change_y: float)[source]
Move all the shapes ion the list :param change_x: Amount to move on the x axis :param change_y: Amount to move on the y axis

remove(item: T)[source]
Remove a specific shape from the list.

class arcade.buffered_draw_commands.VertexBuffer(vbo_vertex_id: ctypes.c_ulong, size: float, draw_mode: int, vbo_color_id: ctypes.c_ulong = None)[source]
Bases: object

This class represents a vertex buffer object for internal library use. Clients of the library probably don’t need to use this.

Attributes:
vbo_id:	ID of the vertex buffer as assigned by OpenGL
size:	
width:	
height:	
color:	
arcade.buffered_draw_commands.create_ellipse(center_x: float, center_y: float, width: float, height: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], border_width: float = 1, tilt_angle: float = 0, num_segments=32, filled=True) → arcade.buffered_draw_commands.Shape[source]
This creates an ellipse vertex buffer object (VBO). It can later be drawn with render_ellipse_filled. This method of drawing an ellipse is much faster than calling draw_ellipse_filled each frame.

Note: This can’t be unit tested on Appveyor because its support for OpenGL is poor.

arcade.buffered_draw_commands.create_ellipse_filled(center_x: float, center_y: float, width: float, height: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], tilt_angle: float = 0, num_segments=128) → arcade.buffered_draw_commands.Shape[source]
Create a filled ellipse. Or circle if you use the same width and height.

arcade.buffered_draw_commands.create_ellipse_filled_with_colors(center_x: float, center_y: float, width: float, height: float, outside_color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], inside_color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], tilt_angle: float = 0, num_segments=32) → arcade.buffered_draw_commands.Shape[source]
Draw an ellipse, and specify inside/outside color. Used for doing gradients.

arcade.buffered_draw_commands.create_ellipse_outline(center_x: float, center_y: float, width: float, height: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], border_width: float = 1, tilt_angle: float = 0, num_segments=128) → arcade.buffered_draw_commands.Shape[source]
Create an outline of an ellipse.

arcade.buffered_draw_commands.create_line(start_x: float, start_y: float, end_x: float, end_y: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], line_width: float = 1) → arcade.buffered_draw_commands.Shape[source]
Create a line to be rendered later. This works faster than draw_line because the vertexes are only loaded to the graphics card once, rather than each frame.

arcade.buffered_draw_commands.create_line_generic(point_list: Union[Tuple[Union[Tuple[float, float], List[float]], ...], List[Union[Tuple[float, float], List[float]]]], color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], shape_mode: int, line_width: float = 1) → arcade.buffered_draw_commands.Shape[source]
This function is used by create_line_strip and create_line_loop, just changing the OpenGL type for the line drawing.

arcade.buffered_draw_commands.create_line_generic_with_colors(point_list: Union[Tuple[Union[Tuple[float, float], List[float]], ...], List[Union[Tuple[float, float], List[float]]]], color_list: Iterable[Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]]], shape_mode: int, line_width: float = 1) → arcade.buffered_draw_commands.Shape[source]
This function is used by create_line_strip and create_line_loop, just changing the OpenGL type for the line drawing.

arcade.buffered_draw_commands.create_line_loop(point_list: Union[Tuple[Union[Tuple[float, float], List[float]], ...], List[Union[Tuple[float, float], List[float]]]], color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], line_width: float = 1)[source]
Create a multi-point line loop to be rendered later. This works faster than draw_line because the vertexes are only loaded to the graphics card once, rather than each frame.

arcade.buffered_draw_commands.create_line_strip(point_list: Union[Tuple[Union[Tuple[float, float], List[float]], ...], List[Union[Tuple[float, float], List[float]]]], color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], line_width: float = 1)[source]
Create a multi-point line to be rendered later. This works faster than draw_line because the vertexes are only loaded to the graphics card once, rather than each frame.

arcade.buffered_draw_commands.create_lines(point_list: Union[Tuple[Union[Tuple[float, float], List[float]], ...], List[Union[Tuple[float, float], List[float]]]], color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], line_width: float = 1)[source]
Create a multi-point line loop to be rendered later. This works faster than draw_line because the vertexes are only loaded to the graphics card once, rather than each frame.

arcade.buffered_draw_commands.create_lines_with_colors(point_list: Union[Tuple[Union[Tuple[float, float], List[float]], ...], List[Union[Tuple[float, float], List[float]]]], color_list: Iterable[Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]]], line_width: float = 1)[source]
arcade.buffered_draw_commands.create_polygon(point_list: Union[Tuple[Union[Tuple[float, float], List[float]], ...], List[Union[Tuple[float, float], List[float]]]], color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], border_width: float = 1)[source]
Draw a convex polygon. This will NOT draw a concave polygon. Because of this, you might not want to use this function.

arcade.buffered_draw_commands.create_rectangle(center_x: float, center_y: float, width: float, height: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], border_width: float = 1, tilt_angle: float = 0, filled=True) → arcade.buffered_draw_commands.Shape[source]
This function creates a rectangle using a vertex buffer object. Creating the rectangle, and then later drawing it with render_rectangle is faster than calling draw_rectangle.

arcade.buffered_draw_commands.create_rectangle_filled(center_x: float, center_y: float, width: float, height: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], tilt_angle: float = 0) → arcade.buffered_draw_commands.Shape[source]
Create a filled rectangle.

arcade.buffered_draw_commands.create_rectangle_filled_with_colors(point_list, color_list) → arcade.buffered_draw_commands.Shape[source]
This function creates multiple rectangle/quads using a vertex buffer object. Creating the rectangles, and then later drawing it with render is faster than calling draw_rectangle.

arcade.buffered_draw_commands.create_rectangle_outline(center_x: float, center_y: float, width: float, height: float, color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], border_width: float = 1, tilt_angle: float = 0) → arcade.buffered_draw_commands.Shape[source]
Create a rectangle outline.

arcade.buffered_draw_commands.create_triangles_filled_with_colors(point_list, color_list) → arcade.buffered_draw_commands.Shape[source]
This function creates multiple rectangle/quads using a vertex buffer object. Creating the rectangles, and then later drawing it with render is faster than calling draw_rectangle.

arcade.buffered_draw_commands.get_rectangle_points(center_x: float, center_y: float, width: float, height: float, tilt_angle: float = 0) → Union[Tuple[Union[Tuple[float, float], List[float]], ...], List[Union[Tuple[float, float], List[float]]]][source]
Utility function that will return all four coordinate points of a rectangle given the x, y center, width, height, and rotation.

arcade.buffered_draw_commands.render(shape: arcade.buffered_draw_commands.VertexBuffer)[source]
Render an shape previously created with a create function.

Application Class Module
The main window class that all object-oriented applications should derive from.

class arcade.application.Window(width: float = 800, height: float = 600, title: str = 'Arcade Window', fullscreen: bool = False, resizable: bool = False, update_rate=0.016666666666666666)[source]
Bases: pyglet.window.Window

Window class

get_location() → Tuple[int, int][source]
Return the X/Y coordinates of the window

get_size()[source]
Get the size of the window.

get_viewport() -> (<class 'float'>, <class 'float'>, <class 'float'>, <class 'float'>)[source]
Get the viewport. (What coordinates we can see.)

on_draw()[source]
Override this function to add your custom drawing code.

on_key_press(symbol: int, modifiers: int)[source]
Override this function to add key press functionality.

on_key_release(symbol: int, modifiers: int)[source]
Override this function to add key release functionality.

on_mouse_drag(x: float, y: float, dx: float, dy: float, buttons: int, modifiers: int)[source]
Override this function to add mouse button functionality.

on_mouse_motion(x: float, y: float, dx: float, dy: float)[source]
Override this function to add mouse functionality.

on_mouse_press(x: float, y: float, button: int, modifiers: int)[source]
Override this function to add mouse button functionality.

on_mouse_release(x: float, y: float, button: int, modifiers: int)[source]
Override this function to add mouse button functionality.

on_mouse_scroll(x: int, y: int, scroll_x: int, scroll_y: int)[source]
User moves the scroll wheel.

on_resize(width, height)[source]
Override this function to add custom code to be called any time the window is resized.

on_update(delta_time: float)[source]
Move everything.

Args:
dt (float):	Time interval since the last time the function was called.
set_max_size(width: float, height: float)[source]
Wrap the Pyglet window call to set maximum size

Args:
width:	width in pixels.
height:	height in pixels.
Returns:
None
Raises:
ValueError
set_min_size(width: float, height: float)[source]
Wrap the Pyglet window call to set minimum size

Args:
width:	width in pixels.
height:	height in pixels.
set_mouse_visible(visible=True)[source]
If true, user can see the mouse cursor while it is over the window. Set false, the mouse is not visible. Default is true.

set_size(width: float, height: float)[source]
Ignore the resizable flag and set the size

set_update_rate(rate: float)[source]
Set how often the screen should be updated. For example, self.set_update_rate(1 / 20) will set the update rate to 60 fps

set_viewport(left: numbers.Number, right: numbers.Number, bottom: numbers.Number, top: numbers.Number)[source]
Set the viewport. (What coordinates we can see. Used to scale and/or scroll the screen.)

set_visible(visible=True)[source]
Set if the window is visible or not. Normally, a program’s window is visible.

test(frames=10)[source]
Used by unit test cases. Runs the event loop twice. :return:

update(delta_time: float)[source]
Move everything. For better consistency in naming, use on_update instead.

Args:
dt (float):	Time interval since the last time the function was called.
arcade.application.open_window(width: numbers.Number, height: numbers.Number, window_title: str, resizable: bool = False) → pyglet.window.BaseWindow[source]
This function opens a window. For ease-of-use we assume there will only be one window, and the programmer does not need to keep a handle to the window. This isn’t the best architecture, because the window handle is stored in a global, but it makes things easier for programmers if they don’t have to track a window pointer.

Args:
window_title:	Title of the window.
width:	Width of the window.
height:	Height of the window.
resizable:	Whether the window can be user-resizable.
Returns:
pyglet.window.Window
Geometry Module
Functions for calculating geometry.

arcade.geometry.are_polygons_intersecting(poly_a: Union[Tuple[Union[Tuple[float, float], List[float]], ...], List[Union[Tuple[float, float], List[float]]]], poly_b: Union[Tuple[Union[Tuple[float, float], List[float]], ...], List[Union[Tuple[float, float], List[float]]]]) → bool[source]
Return True if two polygons intersect.

Args:
poly_a (tuple):	List of points that define the first polygon.
poly_b (tuple):	List of points that define the second polygon.
Returns:
bool
Raises:
None
arcade.geometry.check_for_collision(sprite1: arcade.sprite.Sprite, sprite2: arcade.sprite.Sprite) → bool[source]
Check for a collision between two sprites.

arcade.geometry.check_for_collision_with_list(sprite1: arcade.sprite.Sprite, sprite_list: arcade.sprite_list.SpriteList) → List[arcade.sprite.Sprite][source]
Check for a collision between a sprite, and a list of sprites.

Sprite Module
This module manages all of the code around Sprites.

For information on Spatial Hash Maps, see: https://www.gamedev.net/articles/programming/general-and-gameplay-programming/spatial-hashing-r2697/

class arcade.sprite.AnimatedTimeSprite(scale: float = 1, image_x: float = 0, image_y: float = 0, center_x: float = 0, center_y: float = 0)[source]
Bases: arcade.sprite.Sprite

Sprite for platformer games that supports animations.

update_animation()[source]
Logic for selecting the proper texture to use.

class arcade.sprite.AnimatedWalkingSprite(scale: float = 1, image_x: float = 0, image_y: float = 0, center_x: float = 0, center_y: float = 0)[source]
Bases: arcade.sprite.Sprite

Sprite for platformer games that supports animations.

update_animation()[source]
Logic for selecting the proper texture to use.

class arcade.sprite.Sprite(filename: str = None, scale: float = 1, image_x: float = 0, image_y: float = 0, image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0, repeat_count_x=1, repeat_count_y=1)[source]
Bases: object

Class that represents a ‘sprite’ on-screen.

Attributes:
alpha:	Transparency of sprite. 0 is invisible, 255 is opaque.
angle:	Rotation angle in degrees.
bottom:	Set/query the sprite location by using the bottom coordinate. This will be the ‘y’ of the bottom of the sprite.
boundary_left:	Used in movement. Left boundary of moving sprite.
boundary_right:	Used in movement. Right boundary of moving sprite.
boundary_top:	Used in movement. Top boundary of moving sprite.
boundary_bottom:
 	Used in movement. Bottom boundary of moving sprite.
center_x:	X location of the center of the sprite
center_y:	Y location of the center of the sprite
change_x:	Movement vector, in the x direction.
change_y:	Movement vector, in the y direction.
change_angle:	Change in rotation.
color:	Color tint the sprite
collision_radius:
 	Used as a fast-check to see if this item is close enough to another item. If this check works, we do a slower more accurate check.
cur_texture_index:
 	Index of current texture being used.
guid:	Unique identifier for the sprite. Useful when debugging.
height:	Height of the sprite.
force:	Force being applied to the sprite. Useful when used with Pymunk for physics.
left:	Set/query the sprite location by using the left coordinate. This will be the ‘x’ of the left of the sprite.
points:	Points, in relation to the center of the sprite, that are used for collision detection. Arcade defaults to creating points for a rectangle that encompass the image. If you are creating a ramp or making better hit-boxes, you can custom-set these.
position:	A list with the (x, y) of where the sprite is.
repeat_count_x:	
repeat_count_y:	
right:	Set/query the sprite location by using the right coordinate. This will be the ‘y=x’ of the right of the sprite.
sprite_lists:	List of all the sprite lists this sprite is part of.
texture:	Texture class with the current texture.
textures:	List of textures associated with this sprite.
top:	Set/query the sprite location by using the top coordinate. This will be the ‘y’ of the top of the sprite.
scale:	Scale the image up or down. Scale of 1.0 is original size, 0.5 is 1/2 height and width.
velocity:	Change in x, y expressed as a list. (0, 0) would be not moving.
width:	Width of the sprite
It is common to over-ride the update method and provide mechanics on movement or other sprite updates.

Example:	
add_spatial_hashes()[source]
alpha
Return the RGB color associated with the sprite.

angle
Get the angle of the sprite’s rotation.

append_texture(texture: arcade.draw_commands.Texture)[source]
Appends a new texture to the list of textures that can be applied to this sprite.

bottom
Return the y coordinate of the bottom of the sprite.

center_x
Get the center x coordinate of the sprite.

center_y
Get the center y coordinate of the sprite.

change_x
Get the velocity in the x plane of the sprite.

change_y
Get the velocity in the y plane of the sprite.

clear_spatial_hashes()[source]
collision_radius
Get the collision radius. Note: Final collision checking is done via geometry that was set in get_points/set_points. These points are used in the check_for_collision function. This collision_radius variable is used as a “pre-check.” We do a super-fast check with collision_radius and see if the sprites are close. If they are, then we look at the geometry and figure if they really are colliding.

color
Return the RGB color associated with the sprite.

draw()[source]
Draw the sprite.

get_points() → Tuple[Tuple[float, float]][source]
Get the corner points for the rect that makes up the sprite.

height
Get the center x coordinate of the sprite.

kill()[source]
Alias of remove_from_sprite_lists

left
Left-most coordinate.

points
Get the corner points for the rect that makes up the sprite.

position
Get the center x coordinate of the sprite.

register_sprite_list(new_list)[source]
Register this sprite as belonging to a list. We will automatically remove ourselves from the the list when kill() is called.

remove_from_sprite_lists()[source]
Remove the sprite from all sprite lists.

right
Return the x coordinate of the right-side of the sprite.

set_points(points: Sequence[Sequence[float]])[source]
Set a sprite’s position

set_position(center_x: float, center_y: float)[source]
Set a sprite’s position

set_texture(texture_no: int)[source]
top
Return the y coordinate of the top of the sprite.

update()[source]
Update the sprite.

update_animation()[source]
Override this to add code that will change what image is shown, so the sprite can be animated.

width
Get the center x coordinate of the sprite.

arcade.sprite.get_distance_between_sprites(sprite1: arcade.sprite.Sprite, sprite2: arcade.sprite.Sprite) → float[source]
Returns the distance between the two given sprites

Sprite List Module
This module provides functionality to manage Sprites.

class arcade.sprite_list.SpatialHash(cell_size)[source]
Bases: object

Structure for fast collision checking.

See: https://www.gamedev.net/articles/programming/general-and-gameplay-programming/spatial-hashing-r2697/

get_objects_for_box(check_object: arcade.sprite.Sprite) → List[arcade.sprite.Sprite][source]
Returns colliding Sprites.

insert_object_for_box(new_object: arcade.sprite.Sprite)[source]
Insert a sprite.

remove_object(sprite_to_delete: arcade.sprite.Sprite)[source]
Remove a Sprite.

class arcade.sprite_list.SpriteList(use_spatial_hash=True, spatial_hash_cell_size=128, is_static=False)[source]
Bases: typing.Generic

append(item: T)[source]
Add a new sprite to the list.

calculate_sprite_buffer()[source]
draw()[source]
move(change_x: float, change_y: float)[source]
Moves all contained Sprites.

next_texture_id = 0
pop() → arcade.sprite.Sprite[source]
Pop off the last sprite in the list.

preload_textures(texture_names)[source]
recalculate_spatial_hash(item: T)[source]
remove(item: T)[source]
Remove a specific sprite from the list.

update()[source]
Call the update() method on each sprite in the list.

update_angle(sprite)[source]
update_animation()[source]
Call the update_animation() method on each sprite in the list.

update_location(sprite)[source]
update_position(sprite)[source]
update_positions()[source]
update_texture(sprite)[source]
arcade.sprite_list.get_closest_sprite(sprite1: arcade.sprite.Sprite, sprite_list: arcade.sprite_list.SpriteList) -> (<class 'arcade.sprite.Sprite'>, <class 'float'>)[source]
Given a Sprite and SpriteList, returns the closest sprite, and its distance.

Physics Engines Module
Physics engines for top-down or platformers.

class arcade.physics_engines.PhysicsEnginePlatformer(player_sprite: arcade.sprite.Sprite, platforms: arcade.sprite_list.SpriteList, gravity_constant: float = 0.5)[source]
Bases: object

This class will move everything, and take care of collisions.

can_jump() → bool[source]
Method that looks to see if there is a floor under the player_sprite. If there is a floor, the player can jump and we return a True.

update()[source]
Move everything and resolve collisions.

class arcade.physics_engines.PhysicsEngineSimple(player_sprite: arcade.sprite.Sprite, walls: arcade.sprite_list.SpriteList)[source]
Bases: object

This class will move everything, and take care of collisions.

update()[source]
Move everything and resolve collisions.

Sound Module
Sound library. From https://github.com/TaylorSMarks/playsound/blob/master/playsound.py

exception arcade.sound.PlaysoundException[source]
Bases: Exception

class arcade.sound.Sound(file_name: str)[source]
Bases: object

play()[source]
arcade.sound.load_sound(file_name: str)[source]
Load a sound

arcade.sound.play_sound(sound)[source]
Play a sound

arcade.sound.stop_sound(sound: pyglet.media.codecs.base.Source)[source]
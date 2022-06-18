from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)
    draw_sky()
    draw_ground(canvas)
    draw_fence(canvas, scene_width, scene_height, 50)
    finish_drawing(canvas)


def draw_sky():
    return


def draw_ground(canvas):
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)
    return


def draw_fence(canvas, width, height, interval, color="brown"):
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)
    return


def draw_pine_tree(canvas, center_x, bottom, height):
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
                   trunk_left, trunk_top, trunk_right, bottom,
                   outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    draw_polygon(canvas, center_x, skirt_top,
                 skirt_right, trunk_top,
                 skirt_left, trunk_top,
                 outline="gray20", width=1, fill="dark green")
    return
# Define your functions such as
# draw_sky and draw_ground here.


# Call the main function so that
# this program will start executing.
main()

from os import O_TEMPORARY
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    scene_width = 800
    scene_height = 500
    canvas = start_drawing("Scene", scene_width, scene_height)
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    finish_drawing(canvas)


def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3, scene_width,
                   scene_height, width=0, fill="sky blue")
    draw_cloud(canvas)


def draw_cloud(canvas):
    draw_oval(canvas, 450, 300, 700, 450,
              width=1, outline="white", fill="white")
    draw_oval(canvas, 550, 400, 725, 475,
              width=1, outline="white", fill="white")
    draw_oval(canvas, 350, 375, 500, 450,
              width=1, outline="white", fill="white")
    draw_oval(canvas, 400, 275, 500, 350,
              width=1, outline="white", fill="white")


def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width,
                   scene_height / 3, width=0, fill="tan4")

    # Draw a pine tree.
    tree_center_x = 670
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,
                   tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 590
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
                   tree_bottom, tree_height)

    draw_house(canvas, scene_width, scene_height)
    draw_grass(canvas, scene_width, scene_height)


def draw_grass(canvas, scene_width, scene_height):
    space = 100
    interval = space
    x = 0

    for x in range(500):
        draw_rectangle(canvas, 0, 0, 500,
                       scene_height / 3, outline="black",
                       fill="green")
        x += interval


def draw_house(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 400, scene_width / 3,
                   scene_height / 3, width=0, outline="white", fill="white")


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

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
                 skirt_right, trunk_top,
                 skirt_left, trunk_top,
                 outline="gray20", width=1, fill="dark green")


main()

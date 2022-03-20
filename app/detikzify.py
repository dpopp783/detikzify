import datetime

import pygame
import pygame_gui
from typing import List, Union

from tikz_elements.NodeType import NodeType
from tikz_picture.TikzPicture import TikzPicture
from tikz_elements.DefaultNodeTypes import DefaultNodeTypes
from gui.DraggableNode import DraggableNode
from tikz_picture.TikzPictureCodeGenerator import TikzPictureCodeGenerator


def run(screen_width: int, screen_height: int):

    pygame.init()

    pygame.display.set_caption("detikzify")

    window = pygame.display.set_mode((screen_width, screen_height))

    background = pygame.Surface((screen_width, screen_height))
    background.fill(pygame.Color("#A0A0A0"))

    button_panel = pygame.Rect((screen_width * 3 // 4, 0), (screen_width // 4, screen_height))
    button_panel_color = pygame.Color("#909090")

    canvas = pygame.surface.Surface((screen_width * 5 // 8, screen_height * 5 // 6))
    canvas_color = pygame.Color("#FFFFFF")

    tikz_picture: TikzPicture = TikzPicture()

    available_node_types = DefaultNodeTypes.default_node_types
    nodes: List[DraggableNode] = []
    active_node = None

    button_manager = pygame_gui.UIManager((screen_width, screen_height))

    buttons = dict()

    create_node_type_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((625, 25), (150, 50)),
                                            text='Create Node Type',
                                            manager=button_manager)

    generate_code_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((625, 525), (150, 50)),
                                            text='Generate Code',
                                            manager=button_manager)

    hand_draw_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((625, 325), (150, 50)),
                                                    text= 'Hand Draw',
                                                    manager=button_manager
                                                    )

    row = 0
    col = 0
    for node_type in available_node_types:
        split_name = node_type.name.split("_")
        node_text = split_name[0][0] + split_name[1][0]
        create_node_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((button_panel.left + 25 + 50*col, button_panel.top + 100 + 50 * (row + 1)),(50, 50)),
                                                          text=node_text,
                                                          manager=button_manager
                                                          )
        buttons[node_type.name] = create_node_button
        col = (col + 1) % 3
        if col == 0:
            row = (row + 1) % 3

    buttons["create_node_type"] = create_node_type_button
    buttons["generate_code"] = generate_code_button
    buttons["hand_draw"] = hand_draw_button



    clock = pygame.time.Clock()

    while True:

        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == buttons["create_node_type"]:
                    print("Clicked Create Node Type")
                elif event.ui_element == buttons["generate_code"]:
                    file_name = str(datetime.datetime.now())[:-7].replace(":","-")
                    generator: TikzPictureCodeGenerator = TikzPictureCodeGenerator(tikz_picture)
                    generator.generate_tikz_code()
                    generator.create_tex_file(file_name)
                elif event.ui_element == buttons["hand_draw"]:
                    print("Clicked Hand Draw")
                elif event.ui_element == buttons["cnode_small"]:
                    cnode_small = DraggableNode([0, 0, 25, 25], canvas, "circle")
                    nodes.append(cnode_small)
                elif event.ui_element == buttons["cnode_med"]:
                    cnode_med = DraggableNode([0, 0, 50, 50], canvas, "circle")
                    nodes.append(cnode_med)
                elif event.ui_element == buttons["cnode_large"]:
                    cnode_large = DraggableNode([0, 0, 100, 100], canvas, "circle")
                    nodes.append(cnode_large)
                elif event.ui_element == buttons["sqnode_small"]:
                    sqnode_small = DraggableNode([0, 0, 25, 25], canvas, "rect")
                    nodes.append(sqnode_small)
                elif event.ui_element == buttons["sqnode_med"]:
                    sqnode_med = DraggableNode([0, 0, 50, 50], canvas, "rect")
                    nodes.append(sqnode_med)
                elif event.ui_element == buttons["sqnode_large"]:
                    sqnode_large = DraggableNode([0, 0, 100, 100], canvas, "rect")
                    nodes.append(sqnode_large)

            # checks whether the rectangle has been clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_x_rel_to_canvas = event.pos[0] - 50
                click_y_rel_to_canvas = event.pos[1] - 50

                if event.button == 1:
                    for node in nodes:
                        if node.get_node().collidepoint(click_x_rel_to_canvas, click_y_rel_to_canvas):
                            active_node = node

                    if active_node:
                        active_node.enter_dragging_mode(event)

            # checks whether done dragging
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if active_node:
                        active_node.set_dragging(False)
                        active_node = None

            # keeps the active DraggableNode at the mouse location
            elif event.type == pygame.MOUSEMOTION:
                if active_node:
                    if active_node.get_dragging():
                        active_node.move_to_cursor(event)

            button_manager.process_events(event)

        button_manager.update(time_delta)

        window.blit(background, (0, 0))

        canvas.fill(canvas_color)

        for node in nodes:
            draw_func = node.draw_func()
            draw_func(node.surface, pygame.color.Color("#000000"), node.rect, 2)
        window.blit(canvas, (50, 50))

        pygame.draw.rect(background, button_panel_color, button_panel)
        button_manager.draw_ui(background)

        pygame.display.update()

if __name__ == "__main__":

    run(800,600)
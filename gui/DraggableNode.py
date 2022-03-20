import pygame
from typing import List, Callable


class DraggableNode:
    def __init__(self, node_rect: List[int], surface: pygame.surface.Surface, shape: str):
        self.rect = pygame.rect.Rect(node_rect)
        # stores whether the node is being dragged
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        self.surface = surface
        self.shape = shape

    def get_dragging(self):
        return self.dragging

    def get_node(self):
        return self.rect

    # figures out where the mouse is relative to the rectangle center
    def get_mouse_offset(self, event):
        mouse_x, mouse_y = event.pos
        self.offset_x = self.rect.x - mouse_x
        self.offset_y = self.rect.y - mouse_y

    def move_to_cursor(self, event):
        if self.surface.get_rect().collidepoint(event.pos):
            self.update_location(event)

    # updates the location to the new event location
    def update_location(self, event):
        mouse_x, mouse_y = event.pos
        self.rect.x = mouse_x + self.offset_x
        self.rect.y = mouse_y + self.offset_y
        self.constrict_to_surface()

    def constrict_to_surface(self):
        surface_rect = self.surface.get_rect()
        if self.rect.left < surface_rect.left:
            self.rect.left = surface_rect.left
        elif self.rect.right > surface_rect.right:
            self.rect.right = surface_rect.right

        if self.rect.top < surface_rect.top:
            self.rect.top = surface_rect.top
        elif self.rect.bottom > surface_rect.bottom:
            self.rect.bottom = surface_rect.bottom

    def set_dragging(self, mode):
        self.dragging = mode

    def enter_dragging_mode(self, event):
        self.set_dragging(True)
        self.get_mouse_offset(event)

    def draw_func(self) -> Callable:
        if self.shape == "rect":
            return pygame.draw.rect
        elif self.shape == "circle":
            return pygame.draw.ellipse


def main():
    screen_width = 430
    screen_height = 410

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255,   0,   0)

    fps = 120

    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Tracking System")

    canvas = pygame.surface.Surface((screen_width, screen_height))
    sqnode = DraggableNode([100, 100, 50, 50], canvas, "rect")
    cnode = DraggableNode([200, 100, 26, 26], canvas, "circle")

    nodes = [cnode, sqnode]
    active_node = None

    clock = pygame.time.Clock()

    running = True

    # drives the window
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # checks whether the rectangle has been clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for node in nodes:
                        if node.get_node().collidepoint(event.pos):
                            active_node = node

                    if active_node:
                        active_node.enter_dragging_mode(event)

            # checks whether done dragging
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if active_node:
                        active_node.set_dragging(False)
                        active_node = None

            # keeps the rectangle at the mouse location
            elif event.type == pygame.MOUSEMOTION:
                if active_node:
                    if active_node.get_dragging():
                        active_node.move_to_cursor(event)

        # updates the window to test in
        screen.fill(white)
        canvas.fill(white)
        for node in nodes:
            draw_func = node.draw_func()
            draw_func(node.surface, pygame.color.Color("#000000"), node.rect, 2)
        screen.blit(canvas, (0,0))
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()


if __name__ == "__main__":
    main()
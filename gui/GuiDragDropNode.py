import pygame


class Node:
    def __init__(self, location):
        self.rectangle = pygame.rect.Rect(176, 134, 17, 17)
        # stores whether the node is being dragged
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0

    def get_dragging(self):
        return self.dragging

    def get_node(self):
        return self.rectangle

    # figures out where the mouse is relative to the rectangle center
    def get_mouse_orientation(self, event):
        self.set_dragging(True)
        mouse_x, mouse_y = event.pos
        self.offset_x = self.rectangle.x - mouse_x
        self.offset_y = self.rectangle.y - mouse_y

    # updates the location to the new event location
    def update_location(self, event):
        mouse_x, mouse_y = event.pos
        self.rectangle.x = mouse_x + self.offset_x
        self.rectangle.y = mouse_y + self.offset_y

    def set_dragging(self, mode):
        self.dragging = mode


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
    rectangle = Node([176, 134, 17, 17])
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
                    if rectangle.get_node().collidepoint(event.pos):
                        rectangle.get_mouse_orientation(event)

            # checks whether done dragging
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    rectangle.set_dragging(False)

            # keeps the rectangle at the mouse location
            elif event.type == pygame.MOUSEMOTION:
                if rectangle.get_dragging():
                    rectangle.update_location(event)

        # updates the window to test in
        screen.fill(white)
        pygame.draw.rect(screen, red, rectangle.get_node())
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()


if __name__ == "__main__":
    main()
import pygame


class Node:
    def __init__(self, location, bounds):
        self.rect = pygame.rect.Rect(location)
        # stores whether the node is being dragged
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        self.bounds = pygame.rect.Rect(bounds)

    def get_dragging(self):
        return self.dragging

    def get_node(self):
        return self.rect

    # figures out where the mouse is relative to the rectangle center
    def get_mouse_orientation(self, event):
        self.set_dragging(True)
        mouse_x, mouse_y = event.pos
        self.offset_x = self.rect.x - mouse_x
        self.offset_y = self.rect.y - mouse_y

    def move_to_cursor(self, event):
        if self.bounds.collidepoint(event.pos):
            self.update_location(event)

    # updates the location to the new event location
    def update_location(self, event):
        mouse_x, mouse_y = event.pos
        self.rect.x = mouse_x + self.offset_x
        self.rect.y = mouse_y + self.offset_y
        self.constrict_to_bounds()

    def constrict_to_bounds(self):
        if self.rect.left < self.bounds.left:
            self.rect.left = self.bounds.left
        elif self.rect.right > self.bounds.right:
            self.rect.right = self.bounds.right

        if self.rect.top < self.bounds.top:
            self.rect.top = self.bounds.top
        elif self.rect.bottom > self.bounds.bottom:
            self.rect.bottom = self.bounds.bottom

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
    bounds = [0, 0, screen_width, screen_height]
    rectangle = Node([176, 134, 25, 25], bounds)
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
                    rectangle.move_to_cursor(event)

        # updates the window to test in
        screen.fill(white)
        pygame.draw.rect(screen, black, rectangle.get_node(), 3)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()


if __name__ == "__main__":
    main()
import pygame
from typing import List, Callable

class GUI:

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    class Button:

        def __init__(self, x, y, width, height, color, label, label_color, apply_func: Callable, surface):
            self.rect = pygame.Rect(x, y, width, height)
            self.color = color
            self.apply = apply_func
            self.surface = surface

        def click(self, mouse_pos: List[int]):
            # check if mouse_pos is in the button, then apply whatever effects we need
            if (self.rect.collidepoint(mouse_pos)):
                self.apply()

        def highlight(self):
            mouse_pos: List[int] = pygame.mouse.get_pos()
            if (self.rect.collidepoint(mouse_pos)):
                pygame.draw.rect(self.surface, GUI.WHITE, self.rect, 2)


    screen_width: int
    screen_height: int
    buttons: List[Button]

    def __init__(self, width: int, height: int):
        self.screen_width = width
        self.screen_height = height
        self.window = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen = pygame.Surface((self.screen_width, self.screen_height))

    def run(self):
        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos: List[int] = pygame.mouse.get_pos()

                    # click button if over one
                    for button in self.buttons:
                        button.click(mouse_pos)

            pygame.display.update()

def start(screen_width: int, screen_height: int):
    pygame.init()
    gui: GUI = GUI(screen_width, screen_height)
    gui.run()

if __name__ == "__main__":
    start(800,600)
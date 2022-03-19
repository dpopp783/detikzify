import pygame
from typing import List

class GUI:

    class Button:

        def __init__(self, x, y, width, height, color, label, label_color):
            self.rect = pygame.Rect(x, y, width, height)
            self.color = color

        def pos_in_button(self, List[int]):
            pass

    screen_width: int
    screen_height: int

    def __init__(self, width: int, height: int):
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

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


def start(screen_width: int, screen_height: int):
    pygame.init()
    gui: GUI = GUI(screen_width, screen_height)
    gui.run()

if __name__ == "__main__":
    start(800,600)
import pygame
from typing import List, Callable
from button import Button

class GUI:

    screen_width: int
    screen_height: int
    buttons: List[Button]

    def __init__(self, width: int, height: int):
        self.screen_width = width
        self.screen_height = height
        self.window = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen = pygame.Surface((self.screen_width, self.screen_height))

    def add_button(self, button: Button):
        self.buttons.append(button)

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

    create_node_type_button = Button()

    gui.run()

if __name__ == "__main__":
    start(800,600)
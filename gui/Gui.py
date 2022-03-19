import pygame

class GUI:

    screen_width: int
    screen_height: int

    def __init__(self, width: int, height: int):
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

def start(screen_width: int, screen_height: int):
    pygame.init()

    gui: GUI = GUI(screen_width, screen_height)





if __name__ == "__main__":
    start(800,600)
import pygame
from typing import List
from colors import Colors

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
            pygame.draw.rect(self.surface, Colors.WHITE, self.rect, 2)